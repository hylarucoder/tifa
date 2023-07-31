import datetime
from typing import Union, Any

from jose import jwt

from tifa.exceptions import ApiException
from tifa.settings import settings
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


def decode_jwt(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.JWTError:
        raise ApiException(
            status_code=403,
            message="Could not validate credentials",
        )


def gen_jwt(subject: Union[str, Any], minutes: int) -> str:
    expire = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
