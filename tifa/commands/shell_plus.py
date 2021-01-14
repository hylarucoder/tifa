import importlib

from devtools import debug

from tifa.commands import cli


@cli.command("ishell")
def ishell():
    from IPython import embed
    import cProfile
    import pdb

    main = importlib.import_module("__main__")
    from tifa.app import current_app
    from tifa.models.base import BaseModel
    models = {cls.__name__: cls for cls in BaseModel.__subclasses__()}

    ctx = main.__dict__
    ctx.update(
        {**models, "ipdb": pdb, "cProfile": cProfile, }
    )
    embed(user_ns=ctx, banner2="", using="asyncio")
