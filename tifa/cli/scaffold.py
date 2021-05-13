import typer

group_scaffold = typer.Typer()


@group_scaffold.command("create")
def items_create(item: str):
    typer.echo(f"Creating item: {item}")


@group_scaffold.command("delete")
def items_delete(item: str):
    typer.echo(f"Deleting item: {item}")


@group_scaffold.command("sell")
def items_sell(item: str):
    typer.echo(f"Selling item: {item}")
