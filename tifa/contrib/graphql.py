import inspect
import typing as t

import graphene as gr

from tifa.globals import tracer


def get_typed_signature(call: t.Callable) -> inspect.Signature:
    signature = inspect.signature(call)
    typed_params = [
        inspect.Parameter(
            name=param.name,
            kind=param.kind,
            default=param.default,
            annotation=param.annotation,
        )
        for param in signature.parameters.values()
    ]
    typed_signature = inspect.Signature(typed_params)
    return typed_signature


def parse_resolver(resolver_function, name):
    resolver_function_sig = get_typed_signature(resolver_function)
    has_root = resolver_function_sig.parameters.get("root", False)
    has_info = resolver_function_sig.parameters.get("info", False)

    param_items = {}
    for param_name, param_type in resolver_function_sig.parameters.items():
        param_items[param_name] = param_type.annotation(required=True)

    def combine_resolver(root, info, *args, **kwargs):
        extra_kwargs = {}
        if has_info:
            extra_kwargs["info"] = info
        if has_root:
            extra_kwargs["root"] = root
        with tracer.start_as_current_span(
                "gql_router",
                attributes={
                    "grl_router_name": name
                }
        ):
            return resolver_function(*args, **kwargs, **extra_kwargs)

    return ResolverResult(
        name=name,
        resolver=combine_resolver,
        parameters=resolver_function_sig.parameters,
        has_root=has_root,
        has_info=has_info,
        params=param_items,
    )


class ResolverResult(t.NamedTuple):
    name: str
    resolver: t.Callable
    parameters: t.Mapping[str, inspect.Parameter]
    has_root: bool
    has_info: bool
    params: dict

    def get_mutation_args(self):
        kwargs = {}
        params_type = self.parameters["params"].annotation
        params_type.__name__ = f"Params{self.name.title()}"
        kwargs["Arguments"] = type(
            "Arguments", (), {"params": params_type(required=True, )}
        )
        return kwargs


class GQLRouter:
    query_fields: dict[str, gr.Field]
    mutation_fields: dict[str, gr.Field]

    def __init__(self):
        self.query_fields = {}
        self.mutation_fields = {}

    def item(self, name, output):
        def decorate(resolver_function):
            resolver_result = parse_resolver(resolver_function, name)
            field = gr.Field(
                output,
                args=resolver_result.params,
                resolver=resolver_result.resolver,
                description=resolver_function.__doc__ or "",
            )
            self.query_fields[f"{name}"] = field
            return field

        return decorate

    def list(self, name, output):
        def decorate(resolver_function):
            resolver_result = parse_resolver(resolver_function, name)
            field = gr.Field(
                gr.List(output),
                args=resolver_result.params,
                resolver=resolver_result.resolver,
                description=resolver_function.__doc__ or "nops",
            )
            self.query_fields[f"{name}"] = field
            return field

        return decorate

    def pagination(self, name, output):
        def decorate(resolver_function):
            resolver_result = parse_resolver(resolver_function, name)
            field = gr.Field(
                type(
                    f"Pagination{name}",
                    (gr.ObjectType,),
                    {
                        "page": gr.Int(required=True),
                        "perPage": gr.Int(required=True),
                        "hasNextPage": gr.Boolean(required=True),
                        "items": gr.List(output),
                    },
                ),
                args=resolver_result.params,
                resolver=resolver_result.resolver,
                description=resolver_function.__doc__ or "nops",
            )
            self.query_fields[name] = field
            return field

        return decorate

    def mutation(self, name_or_fn, output=None):
        def decorate(resolver_function, name):
            resolver_result = parse_resolver(resolver_function, name)
            field = type(
                resolver_function.__name__,
                (gr.Mutation,),
                dict(
                    **{
                        "Output": output or gr.Boolean,
                        "mutate": resolver_result.resolver,
                    },
                    **resolver_result.get_mutation_args(),
                ),
            ).Field(description=resolver_function.__doc__)
            self.mutation_fields[f"{name}"] = field
            return field

        if callable(name_or_fn):
            return decorate(name_or_fn, name_or_fn.__name__)
        return lambda fn: decorate(fn, name_or_fn)

    def build_query(self):
        return type(
            "Query",
            (gr.ObjectType,),
            {name: field for name, field in self.query_fields.items()},
        )

    def build_mutation(self):
        return type(
            "Mutation",
            (gr.ObjectType,),
            {name: field for name, field in self.mutation_fields.items()},
        )
