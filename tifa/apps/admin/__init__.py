from fastapi import APIRouter

AUD_ADMIN = "AUD_ADMIN"

bp = APIRouter()


@bp.get("/users")
async def users():
    def serialize(user):
        return {"id": user.id, "name": user.name}

    return [serialize(user) for user in users]


@bp.post("/login")
async def login(name):
    pass
