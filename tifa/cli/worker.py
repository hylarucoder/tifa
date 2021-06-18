import asyncio

import typer
from arq import create_pool, cron, run_worker
from arq.connections import RedisSettings

from tifa.settings import settings
from tifa.tasks import test_task

group_worker = typer.Typer()

redis_settings = RedisSettings(host=settings.REDIS_CACHE_URI)


async def job_tonight(ctx):
    print("凌晨脚本")


async def job_noon(ctx):
    print("午间脚本")


@group_worker.command("start")
def start_worker():
    """
    依据具体业务情况定制多个 worker
    """
    run_worker(
        settings_cls=dict(
            redis_settings=redis_settings,
            functions=[test_task],
        )
    )


@group_worker.command("beat")
def start_scheduler():
    """
    一般全局一个 scheduler
    """
    run_worker(
        settings_cls=dict(
            redis_settings=redis_settings,
            cron_jobs=[
                cron(job_tonight, name="凌晨脚本", hour=0, second=1),
                cron(job_noon, name="午间脚本", hour=12, second=1),
            ]
        )
    )


@group_worker.command("monitor")
def start_monitor():
    """
    TODO: 监控
    """
    ...


async def enqueue_jobs():
    pool = await create_pool(
        redis_settings
    )

    # no id, random id will be generated
    job1 = await pool.enqueue_job("test_task")
    print(job1)
    # random id again, again the job will be enqueued and a job will be returned
    job2 = await pool.enqueue_job("test_task")
    print(job2)
    # custom job id, job will be enqueued
    job3 = await pool.enqueue_job("test_task", _job_id="foobar")
    print(job3)
    # same custom job id, job will not be enqueued and enqueue_job will return None
    job4 = await pool.enqueue_job("test_task", _job_id="foobar")
    print(job4)


@group_worker.command("test")
def test_worker():
    asyncio.run(enqueue_jobs())
