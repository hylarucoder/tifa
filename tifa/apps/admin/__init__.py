import json

from fastapi import APIRouter
from fastapi import FastAPI, Request
from graphql import format_error
from starlette import status
from starlette.background import BackgroundTasks
from starlette.responses import HTMLResponse, JSONResponse

from tifa.apps.admin.graphql import graphql_schema
from tifa.contrib.graphqlapp import GRAPHIQL
from tifa.exceptions import ApiException

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


def format_graphql_error(err):
    return str(err)


@bp.get("/graphql")
async def get_graphql(request: Request):
    if "text/html" in request.headers.get("Accept", ""):
        text = GRAPHIQL.replace("{{REQUEST_PATH}}", json.dumps(request.url.path))
        return HTMLResponse(text)


@bp.post("/graphql")
async def handle_graphql(request: Request):
    content_type = request.headers.get("Content-Type", "")

    if "application/json" in content_type:
        data = await request.json()
    elif "application/graphql" in content_type:
        body = await request.body()
        text = body.decode()
        data = {"query": text}
    elif "query" in request.query_params:
        data = request.query_params
    else:
        return ApiException(
            "Unsupported Media Type",
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
        )

    try:
        query = data["query"]
        variables = data.get("variables")
        operation_name = data.get("operationName")
    except KeyError:
        return ApiException(
            "No GraphQL query found in the request",
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    context = {"request": request}

    result = await graphql_schema.execute_async(
        query, variables=variables, context=context, operation_name=operation_name
    )
    error_data = [format_error(err) for err in result.errors] if result.errors else None
    response_data = {"data": result.data}
    if error_data:
        response_data["errors"] = error_data
    status_code = status.HTTP_400_BAD_REQUEST if result.errors else status.HTTP_200_OK

    return JSONResponse(response_data, status_code=status_code)
