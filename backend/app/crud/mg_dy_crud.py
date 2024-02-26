#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from app.core.session import async_db


async def get_page_info(room_id, user_id):
    """
    获取页面需要的数据
    {
        room_id: 1, 直播间id
        url_room_id: 1, 直播间urlid
        status: True, 直播间连接状态
        user_id: 1, 用户id
        info: {
            rank_info: [
                {
                    user_id: 1,观众id
                    nickname: 哆啦A梦,
                    rank_score: 排名积分,
                    prompt: 生成提示词,
                }
            ],
            last_generate_info: {
                user_id: 1,观众id
                nickname: 哆啦A梦,
                rank_score: 排名积分,
                prompt: 生成提示词,
                image_code: 获取图片的code,
                image_url: 获取图片的url,
            }
        },
        datetime: YYYY-MM-DD,
        generate_count: 生成次数
    }
    """
    pass


async def insert_generate_history(room_id, user_id, generate_data):
    """
    插入生成记录
    {
        room_id: 1,
        url_room_id: 1,
        user_id: 1,
        info: {
            user_id: 1,
            nickname: 哆啦A梦,
            rank_score: 积分,
            prompt: 生成提示词,
            image_code: 获取图片的code,
            image_url: 获取图片的url,
        }
    }
    """


async def insert_gift_record(data):
    """
    插入送礼记录
    """
    record = await async_db.gift_record.count_documents(
        {
            "trace_id": data["trace_id"],
        }
    )
    if not record:
        data["create_time"] = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        await async_db.gift_record.insert_one(data)
        return True
    else:
        return False


async def insert_or_update_rank_info(data):
    """
    data = {
        user_id: 1,
        nickname: 2,
        rank_score: 4,
        create_time: "date",
        update_time: "date",
        delete_time: "date",
        status: 1,
        prompt: "",
        sys_user_id: 1,
    }
    """
    record = await async_db.rank_info.count_documents(
        {"user_id": data["user_id"], "room_id": data["room_id"], "status": 1}
    )
    if not record:
        data["create_time"] = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        data["status"] = 1
        await async_db.rank_info.insert_one(data)
    else:
        await async_db.rank_info.update_one(
            {"user_id": data["user_id"], "status": 1},
            {
                "$inc": {
                    "rank_score": data["rank_score"],
                },
                "$set": {
                    "update_time": datetime.now().strftime("%Y-%m-%d-%H:%M:%S"),
                },
            },
        )


async def find_all_rank_info(sys_user_id, room_id):
    """
    获取当前直播用户的所有排队信息
    """
    records = (
        async_db.rank_info.find(
            {"sys_user_id": sys_user_id, "status": 1, "room_id": room_id}
        )
        .sort("rank_score", -1)
        .limit(10)
    )
    return records


async def update_prompt(data):
    """
    更新提示词
    """
    record = await async_db.rank_info.count_documents(
        {"room_id": data["room_id"], "user_id": data["user_id"], "status": 1}
    )
    if not record:
        data["rank_score"] = 0
        data["status"] = 1
        data["create_time"] = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        await async_db.rank_info.insert_one(data)
    else:
        await async_db.rank_info.update_one(
            {"user_id": data["user_id"], "status": 1, "room_id": data["room_id"]},
            {
                "$set": {
                    "update_time": datetime.now().strftime("%Y-%m-%d-%H:%M:%S"),
                    "prompt": data["prompt"],
                },
            },
        )


async def delete_rank_info(sys_user_id, user_id, room_id):
    """
    软删除某次排队信息，相当于清空上次生成的积分
    """
    await async_db.rank_info.update_one(
        {
            "user_id": user_id,
            "status": 1,
            "sys_user_id": sys_user_id,
            "room_id": room_id,
        },
        {
            "$set": {
                "status": 0,
                "delete_time": datetime.now().strftime("%Y-%m-%d-%H:%M:%S"),
            }
        },
    )


async def check_generate_task_done(sys_user_id, room_id):
    """
    获取是否有未完成的生成任务
    """
    not_done_task = await async_db.dy_mj_task.find_one(
        {"sys_user_id": sys_user_id, "status": 0, "room_id": room_id}
    )
    return not_done_task


async def new_dy_mj_task(sys_user_id, prompt, user_id, task_id, room_id, nickname):
    """
    新建mj任务
    """
    exeist_data = await async_db.dy_mj_task.count_documents({"task_id": task_id})
    if not exeist_data:
        insert_data = {
            "sys_user_id": sys_user_id,
            "prompt": prompt,
            "room_id": room_id,
            "user_id": user_id,
            "nickname": nickname,
            "status": 0,
            "task_id": task_id,
            "create_time": datetime.now().strftime("%Y-%m-%d-%H:%M"),
            "progress": 0,
        }
        await async_db.dy_mj_task.insert_one(insert_data)
        await delete_rank_info(sys_user_id, user_id, room_id)


async def update_dy_mj_task(task_id, data):
    """
    更新mj任务
    """
    data["update_time"] = datetime.now().strftime("%Y-%m-%d-%H:%M")
    if "100" in str(data["progress"]):
        data["status"] = 1

    await async_db.dy_mj_task.update_one({"task_id": task_id}, {"$set": data})


async def insert_split_images(task_id, data):
    """
    data = {
        "split_images": ["url"]
    }
    """
    await async_db.dy_mj_task.update_one({"task_id": task_id}, {"$set": data})


async def get_dy_mj_task_by_id(task_id):
    info = await async_db.dy_mj_task.find_one(
        {
            "task_id": task_id,
        }
    )
    return info


async def get_dy_mj_images_list(page, limit):
    records = async_db.dy_mj_task.find(
            {"status": 1}
        ).skip((page - 1) * limit).limit(12)
    return records
