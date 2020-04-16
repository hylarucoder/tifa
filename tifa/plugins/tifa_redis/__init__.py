from tifa.api import TifaFastApi


class TifaRedisPlugin:
    def __init__(self):
        pass

    def setup_plugin(self, app: TifaFastApi):
        app.plugins["redis"] = {}
        print("redis", {})
