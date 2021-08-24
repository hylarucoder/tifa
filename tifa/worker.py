from raven import Client

from tifa.globals import celery
from tifa.conf import setting

client_sentry = Client(setting.SENTRY_DSN)


@celery.task(name="test_celery")
def test_celery(word: str) -> str:
    f = f"test task return {word}"
    print(f)
    return f
