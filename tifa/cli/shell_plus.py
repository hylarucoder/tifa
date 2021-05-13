import asyncio
import importlib

from tifa.cli import cli
from tifa.globals import db


@cli.command("ishell")
def ishell():
    from IPython import embed
    import cProfile
    import pdb
    from tifa.models.base import BaseModel
    from tifa.models.user import User, SysUser

    models = {cls.__name__: cls for cls in BaseModel.__subclasses__()}
    main = importlib.import_module("__main__")
    ctx = main.__dict__
    ctx.update(
        {
            **models,
            # "session": session,
            "db": db,
            "ipdb": pdb,
            "cProfile": cProfile,
        }
    )
    embed(user_ns=ctx, banner2="", using="asyncio", colors="neutral")
