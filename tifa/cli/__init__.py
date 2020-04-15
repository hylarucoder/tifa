import typer

from tifa.cli.auth import group_auth
from tifa.cli.db import group_db
from tifa.cli.scaffold import group_scaffold

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

cli.add_typer(group_scaffold, name="g")
cli.add_typer(group_auth, name="auth")
cli.add_typer(group_db, name="db")

from .shell_plus import *  # noqa
