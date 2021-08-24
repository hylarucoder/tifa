import asyncio
import json
import logging

from aiokafka import AIOKafkaProducer, AIOKafkaConsumer

from tifa.conf import setting

loop = asyncio.get_event_loop()

logger = logging.getLogger(__name__)


class MyKafka:
    producer: AIOKafkaProducer
    consumer: AIOKafkaConsumer

    def __init__(self):
        self.producer = AIOKafkaProducer(
            loop=loop, bootstrap_servers=setting.KAFKA_BOOTSTRAP_SERVERS
        )
        self.consumer = AIOKafkaConsumer(
            setting.KAFKA_TOPIC,
            loop=loop,
            bootstrap_servers=setting.KAFKA_BOOTSTRAP_SERVERS,
        )

    async def start_producer(self):
        await self.producer.start()

    async def start_consumer(self):
        await self.consumer.start()

    async def send(self, data):
        await self.producer.send(setting.KAFKA_TOPIC, json.dumps(data))


kafka = MyKafka()
