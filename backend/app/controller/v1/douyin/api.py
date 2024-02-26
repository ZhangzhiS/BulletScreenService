from typing import Optional

from app.controller.deps import write_success
from fastapi import APIRouter
from pydantic import BaseModel

from . import dyws

douyin_router = APIRouter()


class CallbackSchema(BaseModel):
    id: Optional[str]
    action: Optional[str]
    status: Optional[str]
    prompt: Optional[str]
    promptEn: Optional[str]
    progress: Optional[str]
    imageUrl: Optional[str]


@douyin_router.post("/callback/douyin")
async def mj_callback(callback: CallbackSchema):
    print(callback)
    await dyws.parse_mj_callback(callback)
    return write_success({"code": "1"})


@douyin_router.get("/mj/images")
async def mj_images(
    page: int = 1,
    limit: int = 20,
):
    res = await dyws.get_mj_dy_images(page, limit)
    return write_success(res)
