#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from typing import List

from environs import Env
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "BulletScreen"
    DEBUG: bool = True

    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    HASHID_SALT: str = "ij1l5uogLPe7XBRXXZ3zdCSbFAi3MajG"

    MONGODB_URL: str = ""
    MONGODB_DBNAME: str = "douyin"

    # CORS 配置
    ALLOWED_HOSTS: List[str] = ["*"]
    ALLOWED_METHODS: List[str] = ["*"]
    ALLOWED_HEADERS: List[str] = ["*"]

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    SECRET_KEY: str = "XBRXXZ3zdCSbFAi3MajG"


env = Env()

try:
    env.read_env(".env")
except Exception:
    env.read_env()
settings = Settings()
