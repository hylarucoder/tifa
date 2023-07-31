import asyncio

from asgiref.sync import async_to_sync
from raven import Client

from tifa.globals import celery
from tifa.settings import settings

client_sentry = Client(settings.SENTRY_DSN)


@celery.task(name="test_celery")
def test_celery(word: str) -> str:
    f = f"test_celery {word}"
    print(f)
    return f


def task_cpu_bound():
    return "good result"


@celery.task(name="test_celery_asyncio_cpu_bound")
def test_celery_asyncio_cpu_bound():
    # assume cpu bound
    return task_cpu_bound()


async def task_io_bound():
    await asyncio.sleep(1)
    return "good result"


@celery.task(name="test_celery_asyncio_io_bound")
def test_celery_asyncio_io_bound():
    async_to_sync(task_io_bound)()
