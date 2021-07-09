from raven import Client

from tifa.globals import celery
from tifa.settings import settings

client_sentry = Client(settings.SENTRY_DSN)


@celery.task(name="test_celery")
def test_celery(word: str) -> str:
    f = f"test task return {word}"
    print(f)
    return f
