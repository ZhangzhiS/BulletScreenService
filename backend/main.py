#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
import asyncio
from fastapi import FastAPI, Request
from loguru import logger

from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from starlette.types import Receive, Scope, Send

from app.core.config import settings
from app.core.err import BaseError
from app.controller.test import test_route
from app.controller.v1.user.api import user_route
from app.controller.v1.douyin.api import douyin_router
from app.controller.v1.douyin import dyws
from starlette.endpoints import WebSocketEndpoint

# from app.controller.v1.merits.api import merits_route


def create_app() -> FastAPI:
    fast_app = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        debug=True,
    )
    register_middleware(fast_app)
    register_route(fast_app)
    rewrite_err(fast_app)
    return fast_app


def register_middleware(fast_app):
    fast_app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=settings.ALLOWED_METHODS,
        allow_headers=settings.ALLOWED_HEADERS,
    )


def register_route(fast_app):
    fast_app.include_router(test_route, prefix=settings.API_V1_STR, tags=["test"])
    fast_app.include_router(user_route, prefix=settings.API_V1_STR, tags=["user"])
    fast_app.include_router(douyin_router, prefix=settings.API_V1_STR, tags=["douyin"])


def err_handler(request: Request, exc: BaseError):  # noqa
    return JSONResponse(
        status_code=200, content={"code": exc.code, "msg": exc.msg, "data": exc.data}
    )


def rewrite_err(fast_app: FastAPI):
    fast_app.add_exception_handler(BaseError, err_handler)


app = create_app()


@app.websocket_route("/douyin/{room_id}/ws")
class DouyinWebsocket(WebSocketEndpoint):
    encoding = "json"

    def __init__(self, scope: Scope, receive: Receive, send: Send) -> None:
        super().__init__(scope, receive, send)
        self.url_room_id = scope.get("path_params", {}).get("room_id")
        self.tasks = {}
        headers = dict(scope.get("headers", []))
        self.token = headers.get(b"token", b"").decode("utf-8")

    async def on_connect(self, websocket):
        await websocket.accept()
        logger.info(self.token)
        if not self.token:
            await websocket.send_json(
                {
                    "msg_type": "close_connect",
                    "data": {"msg": "权限异常，请重新登录", "tips": "error"},
                }
            )
            return
        task = asyncio.create_task(dyws.proxy_douyin(self.url_room_id, websocket, 0))
        self.tasks[websocket] = task

    async def on_receive(self, websocket, data):
        await dyws.parse_web_message(websocket, data)

    async def on_disconnect(self, websocket, close_code):
        # if websocket
        logger.info(websocket)
        logger.info(close_code)
        task = self.tasks.get(websocket)
        if task:
            task.cancel()
            del self.tasks[websocket]
        # await websocket.close()


if __name__ == "__main__":
    pass
