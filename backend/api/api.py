from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import Config, Server

from config import HOST, PORT

from .routers import (
    auth_router,
    info_router,
    user_router
)

app = FastAPI()

app.include_router(auth_router)
app.include_router(info_router)
app.include_router(user_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def api_run():
    config = Config(
        app=app,
        host=HOST,
        port=PORT
    )
    server = Server(config=config)

    await server.serve()
