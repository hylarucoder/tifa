from fastapi_utils.api_model import APIModel

from tifa.apps.admin.local import g
from tifa.apps.admin.router import bp
from tifa.models.app import App


class TApp(APIModel):
    id: str
    name: str


@bp.list("/apps", out=TApp, summary="App", tags=["App"])
def apps_list():
    ins = g.adal.first_or_404(App)
    return {"items": ins}


@bp.item("/app", out=TApp, summary="App", tags=["App"])
def app_item():
    ins = g.adal.first_or_404(App)
    return {"items": ins}


@bp.item("/app/fetch_manifest", out=TApp, summary="App", tags=["App"])
def app_fetch_manifest():
    ins = g.adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/create", out=TApp, summary="App", tags=["App"])
def app_create():
    ins = g.adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/update", out=TApp, summary="App", tags=["App"])
def app_update():
    ins = g.adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/activate", out=TApp, summary="App", tags=["App"])
def app_activate():
    ins = g.adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/deactivate", out=TApp, summary="App", tags=["App"])
def app_deactivate():
    ins = g.adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/delete", out=TApp, summary="App", tags=["App"])
def app_delete():
    ins = g.adal.first_or_404(App)
    return {"items": ins}


class TAppInstallation(APIModel):
    id: str
    name: str


@bp.list(
    "/app/installations", out=TAppInstallation, summary="AppInstallation", tags=["App"]
)
def app_installations():
    ins = g.adal.first_or_404(App)
    return {"items": ins}


@bp.item(
    "/app/installation", out=TAppInstallation, summary="AppInstallation", tags=["App"]
)
def app_installation():
    ins = g.adal.first_or_404(App)
    return {"items": ins}


@bp.item(
    "/app/delete_failed_installation",
    out=TAppInstallation,
    summary="AppInstallation",
    tags=["App"],
)
def app_delete_failed_installation():
    ins = g.adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/install", out=TApp, summary="App", tags=["App"])
def app_install():
    ins = g.adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/retry_install", out=TApp, summary="App", tags=["App"])
def app_retry_install():
    ins = g.adal.first_or_404(App)
    return {"items": ins}


class TAppToken(APIModel):
    id: str
    name: str


@bp.op("/app/token_create", out=TAppToken, summary="AppInstallation", tags=["App"])
def app_token_create():
    ins = g.adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/token_update", out=TAppToken, summary="AppInstallation", tags=["App"])
def app_token_update():
    ins = g.adal.first_or_404(App)
    return {"items": ins}


@bp.op("/app/token_verify", out=TAppToken, summary="AppInstallation", tags=["App"])
def app_token_verify():
    ins = g.adal.first_or_404(App)
    return {"items": ins}
