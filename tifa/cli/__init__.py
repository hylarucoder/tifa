import importlib

import typer
import uvicorn

from tifa.cli.auth import group_auth
from tifa.cli.db import group_db
from tifa.cli.scaffold import group_scaffold
from tifa.app import current_app
from tifa.globals import db

banner = """
  _______   _    __         
 |__   __| (_)  / _|        
    | |     _  | |_    __ _ 
    | |    | | |  _|  / _` |
    | |    | | | |   | (_| |
    |_|    |_| |_|    \__,_|

    An opinionated fastapi starter-kit 
                     by @twocucao
"""

cli = typer.Typer()


def builtin_runserver():
    uvicorn.run("tifa.app:current_app", port=8000, reload=True, access_log=False)


@cli.command()
def start():
    typer.echo(banner)
    builtin_runserver()


@cli.command()
def runserver():
    typer.echo(banner)
    builtin_runserver()


@cli.command("shell_plus")
def shell_plus():
    # lazy import these modules as they are only used in the shell context
    from IPython import embed, InteractiveShell
    import cProfile
    import pdb

    main = importlib.import_module("__main__")

    from tifa import models

    ctx = main.__dict__
    ctx.update(
        {**models.__dict__, "session": db.session, "pdb": pdb, "cProfile": cProfile, }
    )

    InteractiveShell.colors = "Neutral"
    embed(user_ns=ctx, banner2=banner)


cli.add_typer(group_scaffold, name="g")
cli.add_typer(group_auth, name="auth")
cli.add_typer(group_db, name="db")
