from tifa.cli.auth import group_auth
from tifa.cli.db import group_db
from tifa.cli.scaffold import group_scaffold
from tifa.cli.worker import group_worker
from tifa.cli.web import group_web
from .base import cli

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

cli.add_typer(group_scaffold, name="g")
cli.add_typer(group_auth, name="auth")
cli.add_typer(group_db, name="db")
cli.add_typer(group_worker, name="worker")
cli.add_typer(group_web, name="web")

from .shell_plus import *  # noqa
