import json
import random

from fastapi import APIRouter, Request
from graphql import format_error
from starlette import status
from starlette.responses import HTMLResponse, JSONResponse

from tifa.apps.admin.graphql import graphql_schema
from tifa.contrib.graphqlapp import GRAPHIQL
from tifa.exceptions import ApiException
from tifa.globals import tracer

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
        order_id = random.randint(20, 3000)
        with tracer.start_as_current_span("get_graphql_template_render", attributes={
            "order_id": order_id
        }):
            return HTMLResponse(GRAPHIQL)


@bp.post("/graphql")
async def handle_graphql(request: Request):
    user_id = random.randint(20, 3000)
    content_type = request.headers.get("Content-Type", "")
    if "application/json" not in content_type:
        raise ApiException("Content-Type application/json required!")

    data = await request.json()
    query = data["query"]
    variables = data["variables"]
    operation_name = data["operationName"]

    context = {"request": request}

    with tracer.start_as_current_span(
            "gql_router.execute_async",
            attributes={
                "user_id": user_id
            }
    ):
        result = await graphql_schema.execute_async(
            query, variables=variables, context=context, operation_name=operation_name
        )
        error_data = [format_error(err) for err in result.errors] if result.errors else None
        response_data = {"data": result.data}
        if error_data:
            response_data["errors"] = error_data
        status_code = status.HTTP_400_BAD_REQUEST if result.errors else status.HTTP_200_OK

        return JSONResponse(response_data, status_code=status_code)
