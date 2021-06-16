from fastapi import APIRouter
from ariadne import ObjectType, QueryType, gql, make_executable_schema, MutationType
from ariadne.asgi import GraphQL

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


scalars = """
    scalar Datetime
    scalar Date
"""

type_defs = gql(
    """
type Query {
    people: [Person!]!
}

type Person {
    firstName: String
    lastName: String
    age: Int
    fullName: String
}

type Mutation {
    login: String
}
"""
)

# Map resolver functions to Query fields using QueryType
query = QueryType()


# Resolvers are simple python functions
@query.field("people")
def resolve_people(*_):
    return [
        {"firstName": "John", "lastName": "Doe", "age": 21},
        {"firstName": "Bob", "lastName": "Boberson", "age": 24},
    ]


# Map resolver functions to custom type fields using ObjectType
person = ObjectType("Person")


@person.field("fullName")
def resolve_person_fullname(person, *_):
    return "%s %s" % (person["firstName"], person["lastName"])


mutation = MutationType()


@mutation.field("login")
def resolve_person_fullname(*_):
    return [
        {"firstName": "John", "lastName": "Doe", "age": 21},
        {"firstName": "Bob", "lastName": "Boberson", "age": 24},
    ]


# Create executable GraphQL schema
schema = make_executable_schema(type_defs, query, person, mutation)

# Create an ASGI app using the schema, running in debug mode
graphql_app = GraphQL(schema, debug=True)
