from fastapi_utils.api_model import APIModel

from . import bp
from ...globals import db, AsyncDal
from ...models.app import App


class TApp(APIModel):
    id: str
    name: str


@bp.list("/apps", out=TApp, summary="App", tags=["App"])
async def addresses_list():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(App)
    return {"items": ins}


@bp.item("/app", out=TApp, summary="App", tags=["App"])
async def app_item():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(App)
    return {"items": ins}


@bp.item("/app/fetch_manifest", out=TApp, summary="App", tags=["App"])
async def app_item():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/create", out=TApp, summary="App", tags=["App"])
async def app_create():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/update", out=TApp, summary="App", tags=["App"])
async def app_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/activate", out=TApp, summary="App", tags=["App"])
async def app_activate():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/deactivate", out=TApp, summary="App", tags=["App"])
async def app_activate():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/delete", out=TApp, summary="App", tags=["App"])
async def app_delete():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(App)
    return {"items": ins}


class TAppInstallation(APIModel):
    id: str
    name: str


@bp.list(
    "/app/installations", out=TAppInstallation, summary="AppInstallation", tags=["App"]
)
async def app_delete():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(App)
    return {"items": ins}


@bp.item(
    "/app/installation", out=TAppInstallation, summary="AppInstallation", tags=["App"]
)
async def app_delete():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(App)
    return {"items": ins}


@bp.item(
    "/app/delete_failed_installation",
    out=TAppInstallation,
    summary="AppInstallation",
    tags=["App"],
)
async def app_delete():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/install", out=TApp, summary="App", tags=["App"])
async def app_install():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/retry_install", out=TApp, summary="App", tags=["App"])
async def app_install():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(App)
    return {"items": ins}


class TAppToken(APIModel):
    id: str
    name: str


@bp.op("/app/token_create", out=TAppToken, summary="AppInstallation", tags=["App"])
async def app_delete():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/token_update", out=TAppToken, summary="AppInstallation", tags=["App"])
async def app_delete():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/token_verify", out=TAppToken, summary="AppInstallation", tags=["App"])
async def app_delete():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(App)
    return {"items": ins}
