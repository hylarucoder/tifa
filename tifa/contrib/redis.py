import logging

import aioredis

from tifa.settings import settings

logger = logging.getLogger(__name__)


class MyRedis:
    def __init__(self, pool):
        self.pool = pool

    @classmethod
    async def create(cls):
        _pool = await aioredis.Redis(host=settings.REDIS_CACHE_URI)
        return cls(pool=_pool)


redis = MyRedis.create()
