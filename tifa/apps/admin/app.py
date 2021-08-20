from fastapi_utils.api_model import APIModel

from tifa.apps.admin.router import bp
from tifa.globals import db
from tifa.db.dal import Dal
from tifa.models.app import App


class TApp(APIModel):
    id: str
    name: str


@bp.list("/apps", out=TApp, summary="App", tags=["App"])
def apps_list():
    adal = Dal(db.session)
    ins = adal.first_or_404(App)
    return {"items": ins}


@bp.item("/app", out=TApp, summary="App", tags=["App"])
def app_item():
    adal = Dal(db.session)
    ins = adal.first_or_404(App)
    return {"items": ins}


@bp.item("/app/fetch_manifest", out=TApp, summary="App", tags=["App"])
def app_fetch_manifest():
    adal = Dal(db.session)
    ins = adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/create", out=TApp, summary="App", tags=["App"])
def app_create():
    adal = Dal(db.session)
    ins = adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/update", out=TApp, summary="App", tags=["App"])
def app_update():
    adal = Dal(db.session)
    ins = adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/activate", out=TApp, summary="App", tags=["App"])
def app_activate():
    adal = Dal(db.session)
    ins = adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/deactivate", out=TApp, summary="App", tags=["App"])
def app_deactivate():
    adal = Dal(db.session)
    ins = adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/delete", out=TApp, summary="App", tags=["App"])
def app_delete():
    adal = Dal(db.session)
    ins = adal.first_or_404(App)
    return {"items": ins}


class TAppInstallation(APIModel):
    id: str
    name: str


@bp.list(
    "/app/installations", out=TAppInstallation, summary="AppInstallation", tags=["App"]
)
def app_installations():
    adal = Dal(db.session)
    ins = adal.first_or_404(App)
    return {"items": ins}


@bp.item(
    "/app/installation", out=TAppInstallation, summary="AppInstallation", tags=["App"]
)
def app_installation():
    adal = Dal(db.session)
    ins = adal.first_or_404(App)
    return {"items": ins}


@bp.item(
    "/app/delete_failed_installation",
    out=TAppInstallation,
    summary="AppInstallation",
    tags=["App"],
)
def app_delete_failed_installation():
    adal = Dal(db.session)
    ins = adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/install", out=TApp, summary="App", tags=["App"])
def app_install():
    adal = Dal(db.session)
    ins = adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/retry_install", out=TApp, summary="App", tags=["App"])
def app_retry_install():
    adal = Dal(db.session)
    ins = adal.first_or_404(App)
    return {"items": ins}


class TAppToken(APIModel):
    id: str
    name: str


@bp.op("/app/token_create", out=TAppToken, summary="AppInstallation", tags=["App"])
def app_token_create():
    adal = Dal(db.session)
    ins = adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/token_update", out=TAppToken, summary="AppInstallation", tags=["App"])
def app_token_update():
    adal = Dal(db.session)
    ins = adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/token_verify", out=TAppToken, summary="AppInstallation", tags=["App"])
def app_token_verify():
    adal = Dal(db.session)
    ins = adal.first_or_404(App)
    return {"items": ins}
