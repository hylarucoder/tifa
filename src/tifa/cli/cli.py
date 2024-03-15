import importlib

import typer
from loguru import logger

banner = """
  _______   _    __         
 |__   __| (_)  / _|        
    | |     _  | |_    __ _ 
    | |    | | |  _|  / _` |
    | |    | | | |   | (_| |
    |_|    |_| |_|    \__,_|

    An opinionated fastapi starter-kit 
                     by @hylarucoder
"""

app = typer.Typer()


@app.command("shell_plus")
def shell_plus():
    from tifa.db import session_factory
    from tifa.utils.pkg import scan_models
    from labelsmith.settings import settings  # noqa
    from IPython import embed
    from traitlets.config import get_config
    from tifa.db import async_session_factory
    import cProfile
    import pdb

    logger.info("shell plus setup complete")

    main = importlib.import_module("__main__")
    ctx = main.__dict__
    async_session = async_session_factory()

    # async def cleanup():
    #     await async_session.close()
    #     session.close()

    session = session_factory()
    ctx.update(
        {
            "async_session": async_session,
            "session": session,
            "pdb": pdb,
            "cProfile": cProfile,
        }
    )

    models = scan_models()
    ctx.update(models)
    c = get_config()
    embed(user_ns=ctx, banner2=banner, config=c, using="asyncio")


@app.command()
def hello(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
