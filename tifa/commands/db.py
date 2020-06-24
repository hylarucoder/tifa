import typer

group_db = typer.Typer()


@group_db.command("version")
def pg_version():
    typer.echo(f"pg version")


@group_db.command("init")
def db_init():
    typer.echo(f"init")
