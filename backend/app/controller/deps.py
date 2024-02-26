#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Any

# from app.core.session import SessionLocal


# def get_db() -> Generator:
#     # db: SessionLocal
#     try:
#         with SessionLocal() as db:
#             yield db
#     except Exception:
#         raise err.DBErr()


def write_success(
    data: Any = None,
    code: int = 20000,
    msg: str = "success",
) -> dict:
    if not data:
        return {"data": None, "code": code, "msg": msg}
    return {"data": data, "code": code, "msg": msg}
