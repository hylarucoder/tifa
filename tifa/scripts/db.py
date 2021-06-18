from tifa.globals import db


async def init_models():
    async with db.engine.begin() as conn:
        # await conn.run_sync(db.drop_all)
        await conn.run_sync(db.create_all)
