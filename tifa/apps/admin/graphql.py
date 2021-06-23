import graphene as gr

from tifa.contrib.graphql import GQLRouter
from tifa.exceptions import ApiException
from tifa.globals import db
from tifa.models.blog import Post

router = GQLRouter()


class TPost(gr.ObjectType):
    id = gr.Int(description="博客ID")
    name = gr.String(required=True, description="博客标题")


@router.item("ok", output=gr.Boolean)
def test_ok():
    """
    做一个简单的 healthcheck
    """
    return True


@router.item("test_exception", output=gr.Boolean)
def test_exception():
    raise ApiException("raise an api exception")


@router.item("post", output=TPost)
async def post_by_id(id: gr.Int):
    """
    文章详情
    """
    return await Post.get(id)


@router.list("posts", output=TPost)
async def posts():
    """
    文章列表
    """
    return await Post.all()


class PPostPagination(gr.InputObjectType):
    q = gr.String(description="标题,等等")


@router.pagination("posts2", output=TPost)
def posts_pagination(params: PPostPagination):
    return {
        "items": [
            {
                "id": i,
                "name": "testName",
            }
            for i in range(10)
        ],
        "per_page": 10,
        "page": 1,
    }


class ParamsCreatePost(gr.InputObjectType):
    name = gr.String(required=True)


@router.mutation("create_post", output=TPost)
async def create_post(params: ParamsCreatePost):
    post = await Post.add(
        name=params.name
    )
    await db.session.commit()
    return post


graphql_schema = gr.Schema(
    query=router.build_query(),
    mutation=router.build_mutation(),
)
