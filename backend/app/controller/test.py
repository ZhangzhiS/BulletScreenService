#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import APIRouter
from app.controller import deps

test_route = APIRouter()


@test_route.get("/test")
async def async_login(
):
    return deps.write_success()
