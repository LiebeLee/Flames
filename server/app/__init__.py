from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import init_db


def create_app():
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.on_event("startup")
    async def on_startup():
        await init_db()

    return app
