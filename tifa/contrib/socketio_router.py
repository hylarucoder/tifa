from socketio import AsyncServer, AsyncRedisManager


def socketio_server(url) -> AsyncServer:
    _sio = AsyncServer(
        client_manager=AsyncRedisManager(url),
        async_mode="asgi",
        cors_allowed_origins=[],
    )
    return _sio
