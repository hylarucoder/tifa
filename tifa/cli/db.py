import typer
from alembic import command

from tifa.settings import settings

group_db = typer.Typer()


@group_db.command("version")
def pg_version():
    typer.echo(f"pg version")


@group_db.command("init")
def init():
    alembic_cfg = get_alembic_config()
    command.init(alembic_cfg, "./migration")


@group_db.command("migrate")
def db_upgrade():
    alembic_cfg = get_alembic_config()
    command.upgrade(alembic_cfg, "head")


@group_db.command("makemigrations")
def db_make_migrations():
    alembic_cfg = get_alembic_config()
    command.revision(alembic_cfg, autogenerate=True)


def get_alembic_config():
    from alembic.config import Config

    alembic_cfg = Config("./migration/alembic.ini")
    alembic_cfg.set_main_option("script_location", "./migration")
    alembic_cfg.set_main_option("sqlalchemy.url", settings.POSTGRES_DATABASE_URI)
    return alembic_cfg
