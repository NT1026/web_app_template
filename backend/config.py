from orjson import dumps, loads, OPT_INDENT_2
from pydantic import BaseModel

from os.path import isfile


# Default config
class Config(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8080
    jwt_secret: str = "secret"


if isfile("config.json"):
    with open("config.json", "rb") as config_file:
        config = Config(**loads(config_file.read()))
else:
    config = Config()

HOST = config.host
PORT = config.port
JWT_SECRET = config.jwt_secret

with open("config.json", "wb") as config_file:
    config_file.write(dumps(config.model_dump(), option=OPT_INDENT_2))
