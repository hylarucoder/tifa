import asyncio
import json
import logging

from aiokafka import AIOKafkaProducer, AIOKafkaConsumer

from tifa.settings import get_settings

loop = asyncio.get_event_loop()

logger = logging.getLogger(__name__)


class MyKafka:
    def __init__(self):
        self._producer = None
        self._consumer = None

    async def get_producer(self):
        if not self._producer:
            self._producer = AIOKafkaProducer(
                loop=loop, bootstrap_servers=get_settings().KAFKA_BOOTSTRAP_SERVERS
            )
            await self._producer.start()
        return self._producer

    async def get_consumer(self):
        if not self._consumer:
            self._consumer = AIOKafkaConsumer(
                get_settings().KAFKA_TOPIC,
                loop=loop,
                group_id="group1",
                bootstrap_servers=get_settings().KAFKA_BOOTSTRAP_SERVERS,
            )
            await self._consumer.start()
        return self._consumer

    async def send(self, data):
        producer = await self.get_producer()
        await producer.send(get_settings().KAFKA_TOPIC, json.dumps(data))


kafka = MyKafka()
