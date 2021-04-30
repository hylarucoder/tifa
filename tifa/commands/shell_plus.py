import asyncio
import importlib

from tortoise import Tortoise

from tifa.app import register_tortoise_async
from tifa.commands import cli


@cli.command("ishell")
def ishell():
    from IPython import embed
    import cProfile
    import pdb

    main = importlib.import_module("__main__")
    from tifa.models.base import BaseModel

    models = {cls.__name__: cls for cls in BaseModel.__subclasses__()}
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(register_tortoise_async())

        ctx = main.__dict__
        ctx.update(
            {
                **models,
                "ipdb": pdb,
                "cProfile": cProfile,
            }
        )
        embed(user_ns=ctx, banner2="", using="asyncio", colors="neutral")
    finally:
        loop.run_until_complete(Tortoise.close_connections())
