from fastapi import FastAPI

from tifa.app import current_app

app = FastAPI()

application = current_app
