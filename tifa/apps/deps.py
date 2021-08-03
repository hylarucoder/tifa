from tifa.db.adal import AsyncDal
from tifa.db.dal import Dal
from tifa.globals import db


def get_dal():
    dal = Dal(db.session)
    try:
        yield dal
    finally:
        dal.session.close()


def get_async_dal():
    adal = AsyncDal(db.async_session)
    try:
        yield adal
    finally:
        adal.session.close()
