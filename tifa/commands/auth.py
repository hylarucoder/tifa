import typer

group_auth = typer.Typer()


@group_auth.command("create")
def users_create(user_name: str):
    typer.echo(f"Creating user: {user_name}")


@group_auth.command("delete")
def users_delete(user_name: str):
    typer.echo(f"Deleting user: {user_name}")
