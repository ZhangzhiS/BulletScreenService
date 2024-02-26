#!/usr/bin/env python
# -*- coding: utf-8 -*-
from motor.motor_asyncio import AsyncIOMotorClient

# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from app.core.config import settings


def get_async_conn():
    conn = AsyncIOMotorClient(settings.MONGODB_URL)
    return conn[settings.MONGODB_DBNAME]


async_db = get_async_conn()


# async_engine = create_async_engine(settings.ASYNC_SQLALCHEMY_DATABASE_URI)
#
# # 创建session元类
# async_session_local = sessionmaker(
#     class_=AsyncSession,
#     autocommit=False,
#     autoflush=False,
#     bind=async_engine,
# )
