from fastapi import FastAPI

bp = FastAPI()


@bp.get("/users")
async def list_users():
    def serialize(user):
        return {"id": user.id, "name": user.name}

    return [serialize(user) for user in []]


@bp.post("/login")
async def login(name):
    pass
