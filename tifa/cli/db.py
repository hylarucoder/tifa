import os

import typer
from alembic import __version__ as __alembic_version__
from alembic.config import Config as AlembicConfig
from alembic import command

alembic_ini_path = "./"
alembic_cfg = AlembicConfig(os.path.join(alembic_ini_path, "alembic.ini"))
alembic_cfg.set_main_option("script_location", "migrations")

group_db = typer.Typer()


@group_db.command("version")
def alembic_init():
    typer.echo(f"alembic version:{__alembic_version__}")


@group_db.command("init")
def alembic_init():
    command.init(alembic_cfg, "migrations")


@group_db.command("upgrade")
def alembic_upgrade():
    command.upgrade(alembic_cfg, "head")


# TODO: 包装一下
