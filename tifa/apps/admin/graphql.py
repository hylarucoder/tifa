import graphene as gr
from starlette.graphql import GraphQLApp

from tifa.contrib.graphql import GQLRouter

router = GQLRouter()


class TPost(gr.ObjectType):
    id = gr.Int()
    name = gr.String(required=True)


@router.item("ok", output=gr.Boolean)
def test_ok():
    """
    "test ok"
    """
    return True


@router.item("post", output=TPost)
def post_by_id(id: gr.Int):
    """
    "test ok id"
    """
    return {
        "id": id,
        "name": "testName",
    }


@router.list("posts", output=TPost)
def posts():
    return [{
        "id": i,
        "name": "testName",
    } for i in range(10)]


class PPostPagination(gr.InputObjectType):
    q = gr.String()


@router.pagination("post_pagination", output=TPost)
def posts_pagination(params: PPostPagination):
    return {
        "items": [{
            "id": i,
            "name": "testName",
        } for i in range(10)],
        "per_page": 10,
        "page": 1,
    }


class ParamsCreatePost(gr.InputObjectType):
    id = gr.Int(required=True)
    name = gr.String(required=True)


@router.mutation("create_post", output=TPost)
def create_post(params: ParamsCreatePost):
    return TPost(
        id=params.id,
        name=params.name,
    )


graphql_app = GraphQLApp(schema=gr.Schema(
    query=router.build_query(),
    mutation=router.build_mutation(),
))
