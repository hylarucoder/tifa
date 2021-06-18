import logging

import aioredis

from tifa.settings import settings

logger = logging.getLogger(__name__)


class MyRedis:
    _pool = None

    def __init__(self, dsn: str):
        self.dsn = dsn

    async def get_pool(self):
        if not self._pool:
            self._pool = await aioredis.create_redis_pool(self.dsn)
        return self._pool


redis = MyRedis(settings.REDIS_CACHE_URI)
