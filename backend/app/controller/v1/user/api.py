#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.controller import deps
from app.schema import user_schema as schema
from fastapi import APIRouter

from . import ctrl

user_route = APIRouter()


@user_route.get("/user/info")
def get_user_info():
    return deps.write_success()


@user_route.post("/login")
async def login(
    *,
    login_data: schema.LoginParams,
):
    res = await ctrl.login(login_data)
    return deps.write_success(res)


@user_route.post("/registerxxxx")
async def register(
    *,
    register_data: schema.RegisterParams,
):
    res = await ctrl.register(register_data)
    return deps.write_success(res)
