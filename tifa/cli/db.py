import asyncio

import typer
from alembic import command

from tifa.globals import db
from tifa.settings import settings

group_db = typer.Typer()


async def init_models():
    async with db.engine.begin() as conn:
        # await conn.run_sync(db.drop_all)
        await conn.run_sync(db.create_all)


@group_db.command("version")
def pg_version():
    typer.echo(f"pg version")


@group_db.command("init")
def db_init():
    from tifa.app import current_app

    asyncio.run(init_models())


@group_db.command("migrate")
def db_upgrade():
    from tifa.app import current_app

    alembic_cfg = get_alembic_config()
    command.upgrade(alembic_cfg, "head")


@group_db.command("makemigration")
def db_make_migrations():
    from tifa.app import current_app

    alembic_cfg = get_alembic_config()
    command.revision(alembic_cfg, autogenerate=True)


def get_alembic_config():
    from alembic.config import Config

    alembic_cfg = Config("./migration/alembic.ini")
    alembic_cfg.set_main_option("script_location", "./migration")
    alembic_cfg.set_main_option("sqlalchemy.url", settings.POSTGRES_DATABASE_URI)
    return alembic_cfg
