import importlib
import inspect
import itertools
import pkgutil


def import_submodules(package, recursive=True):
    if isinstance(package, str):
        package = importlib.import_module(package)
    results = {}
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + "." + name
        results[full_name] = importlib.import_module(full_name)
        if recursive and is_pkg:
            results.update(import_submodules(full_name))
    return results


def register_fastapi_models():
    pass


def scan_models():
    from tifa.db import Model

    models = {}
    for exc_class in itertools.chain(
            class_scanner("labelsmith.models", lambda exc: issubclass(exc, (Model)))
    ):
        models[exc_class.__name__] = exc_class
    return models


def class_scanner(pkg, filter_=lambda _: True):
    """
    :param pkg: a module instance or name of the module
    :param filter_: a function to filter matching classes
    :return: all filtered class instances
    """

    def scan_pkg_file(pkg):
        return {cls[1] for cls in inspect.getmembers(pkg, inspect.isclass) if filter_(cls[1])}

    if isinstance(pkg, str):
        pkg = importlib.import_module(pkg)
    if not hasattr(pkg, "__path__"):
        return scan_pkg_file(pkg)
    classes = scan_pkg_file(pkg)
    for _, modname, _ in pkgutil.iter_modules(pkg.__path__):
        module = importlib.import_module("." + modname, pkg.__name__)
        classes |= class_scanner(module, filter_)
    return classes
