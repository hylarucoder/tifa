import typer

group_worker = typer.Typer()


@group_worker.command("start")
def start_worker():
    """
    依据具体业务情况定制多个 worker
    """
    ...


@group_worker.command("beat")
def start_scheduler():
    """
    一般全局一个 scheduler
    """
    ...


@group_worker.command("monitor")
def start_monitor():
    """
    TODO: 监控
    """
    ...


@group_worker.command("pg_to_es")
def pg_to_es():
    ...


@group_worker.command("test")
def test_worker():
    ...
