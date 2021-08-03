import importlib

from tifa.cli import cli
from tifa.globals import db
from tifa.db.adal import AsyncDal
from tifa.db.dal import Dal
from tifa.utils.pkg import import_submodules


@cli.command("shell_plus")
def shell_plus():
    from IPython import embed
    import cProfile
    import pdb

    import_submodules("tifa.models")
    models = {cls.__name__: cls for cls in db.Model.__subclasses__()}
    dal = Dal(db.session)
    adal = AsyncDal(db.async_session)
    main = importlib.import_module("__main__")
    ctx = main.__dict__
    ctx.update(
        {
            **models,
            "dal": dal,
            "adal": adal,
            "db": db,
            "ipdb": pdb,
            "cProfile": cProfile,
        }
    )
    embed(user_ns=ctx, banner2="", using="asyncio", colors="neutral")
