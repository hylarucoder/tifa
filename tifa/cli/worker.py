import typer

group_worker = typer.Typer()


async def job_tonight(ctx):
    print("凌晨脚本")


async def job_noon(ctx):
    print("午间脚本")


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


@group_worker.command("test")
def test_worker():
    ...
