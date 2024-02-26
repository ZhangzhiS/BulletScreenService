
from app.core.session import async_db


async def get_user_by_id(user_id):
    records = await async_db.user_info.find_one(
            {"status": 1, "user_id": user_id}
        )
    return records


async def get_user_by_username(username):
    records = await async_db.user_info.find_one(
            {"status": 1, "username": username}
        )
    return records


async def insert_one_user(username, password):
    records = await async_db.user_info.find_one(
            {"status": 1, "user_id": username}
        )
    if records:
        return False, {"msg": "用户已存在"}
    async_db.user_info.insert_one(
        {"username": username, "password": password, "status": 1}
    )
    return True, {"msg": "注册成功"}


