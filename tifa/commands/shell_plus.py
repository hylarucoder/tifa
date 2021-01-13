import importlib

from tifa.commands import cli


@cli.command("ishell")
def ishell():
    from IPython import embed
    import cProfile
    import pdb

    main = importlib.import_module("__main__")

    from tifa import models

    ctx = main.__dict__
    ctx.update(
        {**models.__dict__, "ipdb": pdb, "cProfile": cProfile, }
    )
    embed(user_ns=ctx, banner2="", using="asyncio")
