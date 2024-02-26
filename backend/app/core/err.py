#! /usr/bin/env python
# -*- coding: utf-8 -*-
from app.core.config import settings


class BaseError(Exception):
    """异常基类"""

    def __init__(self, code: int, msg: str, data):
        self.status = False
        self.code = code
        self.msg = msg
        self.data = data


class UsernameError(BaseError):

    def __init__(self):
        self.status = False
        self.code = 40000
        self.msg = "用户名错误"
        self.data = None


class PasswordError(BaseError):
    """用户id错误"""

    def __init__(self):
        self.status = False
        self.code = 40000
        self.msg = "密码错误，请输入正确的密码"
        self.data = None


class ParamsError(BaseError):
    """参数错误"""

    def __init__(self, param="参数"):
        self.code = 40001
        self.msg = "请求参数异常" if settings.DEBUG else f"{param}异常"
        self.data = None


class UserNotFoundError(BaseError):
    """用户不存在"""

    def __init__(self):
        self.code = 40400
        self.msg = "用户不存在"
        self.data = None


class UserActiveError(BaseError):
    """用户被禁用"""

    def __init__(self):
        self.code = 40100
        self.msg = "账户已被禁用，请联系管理员"
        self.data = None


class UserAlreadyExistError(BaseError):
    """用户已存在"""

    def __init__(self):
        self.code = 40110
        self.msg = "用户已存在"
        self.data = None

class PermissionsError(BaseError):
    """权限错误"""

    def __init__(self):
        self.code = 40300
        self.msg = "权限异常"
        self.data = None


class AddError(BaseError):
    """新增数据失败"""

    def __init__(self):
        self.code = 40500
        self.msg = "新增失败"
        self.data = None


class WechatHttpApiError(BaseError):
    """微信机器人返回异常"""

    def __init__(self, msg: str):
        self.code = 51000
        self.msg = msg
        self.data = None


class GetStartIdErr(BaseError):
    def __init__(self):
        self.code = 52000
        self.msg = "not head id"
        self.data = None


class DBErr(BaseError):
    def __init__(self):
        self.code = 52001
        self.msg = "DB error"
        self.data = None
