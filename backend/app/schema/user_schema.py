#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from typing import Optional

from pydantic import BaseModel

from typing import Optional


class Code2SessionParams(BaseModel):
    code: str
    errMsg: str


class UserSchemaBase(BaseModel):
    openid: str


class UserSchemaBaseCreate(UserSchemaBase):
    pass


class UserSchemaBaseUpdate(UserSchemaBase):
    merits: Optional[int]
    can_use_merits: Optional[int]


class LoginParams(BaseModel):
    username: str
    password: str


class RegisterParams(BaseModel):
    username: str
    password: str
