import typer
import uvicorn

group_web = typer.Typer()


@group_web.command("start")
def start_tifa():
    uvicorn.run(
        "tifa.app:create_app",
        factory=True,
        reload=True,
        host="0.0.0.0",
        port=8000,
        log_level="info",
    )


@group_web.command("whiteboard")
def start_whiteboard():
    uvicorn.run(
        "tifa.app:create_app",
        factory=True,
        reload=True,
        host="0.0.0.0",
        port=8001,
        log_level="info",
    )
