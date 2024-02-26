from datetime import datetime, timedelta
from typing import Any, Optional, Union
from app.core import err
from app.crud.mg_user_crud import get_user_by_username, insert_one_user
from app.schema.user_schema import LoginParams, RegisterParams

from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


ALGORITHM = "HS256"


def create_access_token(
    subject: Union[str, Any], expires_delta: Optional[timedelta] = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


async def login(login_data: LoginParams):
    old_user_info = await get_user_by_username(login_data.username)
    if not old_user_info:
        raise err.UserNotFoundError()
    if verify_password(login_data.password, old_user_info.get("password")):
        return {
            "access_token": create_access_token(
                {"username": old_user_info.get("username")}
            )
        }
    raise err.PasswordError()


async def register(register_data: RegisterParams):
    encode_password = get_password_hash(register_data.password)
    status, msg = await insert_one_user(
        username=register_data.username, password=encode_password
    )
    if status:
        return msg
    raise err.UserAlreadyExistError()
