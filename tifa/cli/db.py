import os

import typer
from alembic import __version__ as __alembic_version__
from alembic.config import Config as AlembicConfig
from alembic import command

from tifa.app import current_app

alembic_ini_path = "./"
alembic_cfg = AlembicConfig(os.path.join(alembic_ini_path, "alembic.ini"))
alembic_cfg.set_main_option("script_location", "migrations")
# 本可放在 migrations/env.py 里，但考虑到 migrations 生产环境和测试环境应该尽量保持一致，故在这里进行配置
alembic_cfg.set_main_option('sqlalchemy.url', current_app.settings.POSTGRES_DATABASE_URI)

group_db = typer.Typer()


@group_db.command("version")
def alembic_init():
    typer.echo(f"alembic version:{__alembic_version__}")


@group_db.command("init")
def alembic_init():
    command.init(alembic_cfg, "migrations")


@group_db.command("generate")
def alembic_generate():
    command.revision(alembic_cfg, autogenerate=True)


@group_db.command("upgrade")
def alembic_upgrade():
    command.upgrade(alembic_cfg, "head")

# TODO: 包装一下
