#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gzip
import time
import random
from loguru import logger
import websockets
import httpx
from app.crud.mg_dy_crud import (
    check_generate_task_done,
    delete_rank_info,
    find_all_rank_info,
    get_dy_mj_images_list,
    get_dy_mj_task_by_id,
    insert_gift_record,
    insert_or_update_rank_info,
    new_dy_mj_task,
    update_dy_mj_task,
    update_prompt,
)

from app.utils.douyinws import dy
from app.utils.douyinws.douyin_pb2 import PushFrame
from app.utils.douyinws.douyin_pb2 import Response

DOUYIN_URL = "https://live.douyin.com"
MJ_API = "https://mj.zsmckj.cn/mj/submit/imagine"
SPLIT_API = "https://console.jifengjituan.com/api.php/web/splitMjImage"
P = open("prompt.txt", "r").readlines()


async def generate_image(prompt):
    """
    请求生成图片的接口
    """
    logger.info(prompt)
    params = {
        "prompt": prompt,
        "notifyHook": "http://hello.zzs7.top/api/v1/callback/douyin",
    }
    headers = {"mj-api-secret": "3DMjAZS8hdCayoATVrg0Em8r"}
    async with httpx.AsyncClient() as client:
        resp = await client.post(MJ_API, json=params, headers=headers)
    logger.info(resp)
    res = resp.json()
    return res


async def sendAck(ws, logId, internalExt):
    obj = PushFrame()
    obj.payloadType = "ack"
    obj.logId = logId
    obj.payloadType = internalExt
    data = obj.SerializeToString()
    await ws.send(data)


async def ping(ws):
    ping_data = PushFrame()
    ping_data.payloadType = "hb"
    data = ping_data.SerializeToString()
    await ws.send(data)


def loadPackage(message):
    wssPackage = PushFrame()
    wssPackage.ParseFromString(message)
    logId = wssPackage.logId
    decompressed = gzip.decompress(wssPackage.payload)
    payloadPackage = Response()
    payloadPackage.ParseFromString(decompressed)
    return logId, payloadPackage


async def parse_gift_message(data, room_id):
    """
    处理礼物消息，根据礼物的抖钻价值进行计算并排队
            user_name = data["user"]["nickName"]
            level = data["user"]["payGrade"].get("level", 0)
            describe = data["gift"]["describe"]
            diamondCount = data["gift"]["diamondCount"]
    """
    logger.info(data)
    nickname = data["user"]["nickName"]
    user_id = data["user"]["id"]
    avatar_url = data["user"]["AvatarThumb"]["urlListList"][0]
    # short_id = data["user"]["shortId"]
    desc = data["gift"]["describe"]
    diamondCount = data["gift"]["diamondCount"]
    trace_id = data["traceId"]
    info = {
        "user_id": user_id,
        "nickname": nickname,
        # "short_id": short_id,
        "sys_user_id": 0,
        "rank_score": diamondCount,
        "desc": desc,
        "trace_id": trace_id,
        "room_id": room_id,
    }
    gift_status = await insert_gift_record(info)
    if gift_status:
        info = {
            "user_id": user_id,
            "nickname": nickname,
            # "short_id": short_id,
            "sys_user_id": 0,
            "rank_score": diamondCount,
            "room_id": room_id,
            "avatar_url": avatar_url
        }
        await insert_or_update_rank_info(info)


async def parse_chat_message(data, room_id):
    """
    处理普通消息
    生成指令：生成-波澜壮阔的大海上面漂浮着孤独的小船，气氛悲壮但又温馨

            user_name = data["user"]["nickName"]
            level = data["user"]["payGrade"].get("level", 0)
            describe = data["gift"]["describe"]
            diamondCount = data["gift"]["diamondCount"]
    """
    message = data["content"]
    nickname = data["user"]["nickName"]
    user_id = data["user"]["id"]

    if "生成-" in message:
        await update_prompt(
            {
                "user_id": user_id,
                "sys_user_id": 0,
                "nickname": nickname,
                "room_id": room_id,
                "prompt": message.replace("生成-", ""),
            }
        )


async def parsePackageMessage(payloadPackage, ws, room_id):
    """
    消息处理规则
        1. 点赞
        2. 普通消息，判断是否是生成图片的提示词
        3. 礼物消息，获取积分价值，修改排队列表
    """
    for msg in payloadPackage.messagesList:
        if msg.method == "WebcastMatchAgainstScoreMessage":
            # data = dy.unPackMatchAgainstScoreMessage(msg.payload)
            pass

        elif msg.method == "WebcastLikeMessage":
            # 点赞
            data = dy.unPackWebcastLikeMessage(msg.payload)

            # await ws.send_json(data)

        elif msg.method == "WebcastMemberMessage":
            # xx成员进入直播间消息
            data = dy.unPackWebcastMemberMessage(msg.payload)
            # await ws.send_json(data)
        elif msg.method == "WebcastGiftMessage":
            # 礼物消息
            data = dy.unPackWebcastGiftMessage(msg.payload)
            # await ws.send_json(data)
            await parse_gift_message(data, room_id)
        elif msg.method == "WebcastChatMessage":
            # 普通消息
            data = dy.unPackWebcastChatMessage(msg.payload)
            # await ws.send_json(data)
            await parse_chat_message(data, room_id)

        elif msg.method == "WebcastSocialMessage":
            # 用户关注
            data = dy.unPackWebcastSocialMessage(msg.payload)
            # await ws.send_json(data)

        elif msg.method == "WebcastRoomUserSeqMessage":
            # 网络广播室用户序列
            data = dy.unPackWebcastRoomUserSeqMessage(msg.payload)
            # await ws.send_json(data)
        #
        # elif msg.method == "WebcastUpdateFanTicketMessage":
        #     # 粉丝团信息
        #     data = dy.unPackWebcastUpdateFanTicketMessage(msg.payload)
        #     await ws.send_json(data)

        elif msg.method == "WebcastCommonTextMessage":
            data = dy.unPackWebcastCommonTextMessage(msg.payload)
            print(data)
        #     # continue
        # elif msg.method == "WebcastProductChangeMessage":
        #     data = dy.WebcastProductChangeMessage(msg.payload)
        # continue
        # else:
        #     data = ""


async def refresh_room_info(ws, url_room_id):
    url = f"{DOUYIN_URL}/{url_room_id}"
    room_info = dy.parse_live_room(url)
    if room_info:
        await ws.send_json({"msg_type": "refresh_room_info", "data": room_info})
        return room_info
    await ws.send_json(
        {
            "msg_type": "close_connect",
            "data": {"msg": "请检查直播间的地址配置是否正确", "tips": "error"},
        }
    )
    return {}


async def refresh_rank_list(ws, sys_user_id, room_id):
    """
    刷新排队列表数据
    """
    data = await find_all_rank_info(sys_user_id, room_id)
    res = []
    async for i in data:
        res.append(
            {
                "nickname": i["nickname"],
                "rank_score": i["rank_score"],
                "prompt": i.get("prompt", ""),
                "user_id": i["user_id"],
                "avatar_url": i["avatar_url"]
            }
        )
    await ws.send_json({"msg_type": "refresh_rank_list", "data": res})


async def start_generating_task(ws, data):
    """
    开始生成任务
    """
    logger.info(data)
    task_status = await check_generate_task_done(data["sys_user_id"], data["room_id"])
    if  task_status:
        ws.send_json(
            {
                "msg_type": "refresh_last_generating_info",
                "data": {
                    "nickname": data["nickname"],
                    "prompt": data["prompt"],
                    "user_id": data["user_id"],
                    "image_url": task_status.get("image_url", ""),
                    "image_code": task_status.get("task_id"),
                    "task_id": task_status.get("task_id"),
                    "progress": 0,
                }
            }
        )
        return
    prompt = data["prompt"]
    if not prompt:
        await ws.send_json(
            {
                "msg_type": "alt_msg",
                "data": {"msg": "还没输入生成词哦，请尽快输入，本轮轮空，生成随机", "tips": "生成失败"},
            }
        )
        # return
        prompt = random.choice(P)
        data["prompt"] = prompt
        data["user_id"] = "0"
        data["nickname"] = "系统随机"
    try:
        res = await generate_image(prompt)
    except Exception as e:
        print(e)
        res = {"code": 0}
    if res.get("code") == 1:
        task_id = res.get("result")

        await new_dy_mj_task(
            data["sys_user_id"],
            data["prompt"],
            data["user_id"],
            task_id,
            data["room_id"],
            data["nickname"],
        )

        await ws.send_json(
            {
                "msg_type": "refresh_last_generating_info",
                "data": {
                    "nickname": data["nickname"],
                    "prompt": data["prompt"],
                    "user_id": data["user_id"],
                    "image_url": res.get("image_url", ""),
                    "image_code": task_id,
                    "task_id": task_id,
                    "progress": 0,
                },
            }
        )
        await ws.send_json(
            {
                "msg_type": "start_task",
                "data": {
                    "nickname": data["nickname"],
                    "prompt": data["prompt"],
                    "task_id": task_id,
                },
            }
        )
    elif res.get("code") == 24:
        await delete_rank_info(
            sys_user_id=data["sys_user_id"],
            user_id=data["user_id"],
            room_id=data["room_id"],
        )
        await ws.send_json(
            {"msg_type": "alt_msg", "data": {"msg": "生成词有敏感词,不符合规范", "tips": "生成失败"}}
        )


async def refresh_generate_info(ws, data):
    if data.get("task_id") != "start":
        info = await get_dy_mj_task_by_id(data.get("task_id"))
        if info.get("status") == -1:
            await ws.send_json(
                {
                    "msg_type": "alt_msg",
                    "data": {"msg": "抱歉,AI认为你的生成词违反了它的规范", "tips": "生成失败"},
                }
            )
        res = {
            "nickname": info["nickname"],
            # "prompt": data["prompt"],
            "user_id": info["user_id"],
            "image_url": info.get("image_url", ""),
            "image_code": data.get("task_id"),
            "task_id": data.get("task_id"),
            "progress": info.get("progress", 0),
            "status": info.get("status", 0),
        }
        await ws.send_json(
            {"msg_type": "refresh_last_generating_info", "data": res}
        )


async def proxy_douyin(url_room_id, f_ws, sys_user_id):
    room_info = await refresh_room_info(f_ws, url_room_id)
    if not room_info:
        return
    room_id = room_info.get("live_room_id")
    await refresh_rank_list(f_ws, sys_user_id, room_id)
    room_info.get("live_room_title")
    ttwid = room_info.get("ttwid")

    webSocketUrl = f"wss://webcast3-ws-web-lq.douyin.com/webcast/im/push/v2/?app_name=douyin_web&version_code=180800&webcast_sdk_version=1.3.0&update_version_code=1.3.0&compress=gzip&internal_ext=internal_src:dim|wss_push_room_id:{room_id}|wss_push_did:7188358506633528844|dim_log_id:20230521093022204E5B327EF20D5CDFC6|fetch_time:1684632622323|seq:1|wss_info:0-1684632622323-0-0|wrds_kvs:WebcastRoomRankMessage-1684632106402346965_WebcastRoomStatsMessage-1684632616357153318&cursor=t-1684632622323_r-1_d-1_u-1_h-1&host=https://live.douyin.com&aid=6383&live_id=1&did_rule=3&debug=false&maxCacheMessageNumber=20&endpoint=live_pc&support_wrds=1&im_path=/webcast/im/fetch/&user_unique_id=7188358506633528844&device_platform=web&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh&browser_platform=MacIntel&browser_name=Mozilla&browser_version=5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_15_7)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/113.0.0.0%20Safari/537.36&browser_online=true&tz_name=Asia/Shanghai&identity=audience&room_id={room_id}&heartbeatDuration=0&signature=00000000"
    h = {
        "cookie": f"ttwid={ttwid}",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",  # noqa
    }

    # 创建一个长连接
    async with websockets.connect(webSocketUrl, extra_headers=h) as ws:
        time_step = int(time.time())

        while True:
            now_time_step = int(time.time())
            #  heartbeat 10 second
            if (now_time_step - time_step) > 10:
                time_step = now_time_step
                await refresh_rank_list(f_ws, sys_user_id, room_id)
                await ping(ws)
                continue

            response = await ws.recv()
            logId, payloadPackage = loadPackage(response)

            if payloadPackage.needAck:
                await sendAck(ws, logId, payloadPackage.internalExt)
            await parsePackageMessage(payloadPackage, f_ws, room_id)


async def parse_mj_callback(callback_data):
    """
    分割图片并更新数据库
    """

    data = {
        "progress": int(callback_data.progress.replace("%", "")),
        "image_url": callback_data.imageUrl,
        "image_code": callback_data.id,
    }

    if callback_data.status == "SUCCESS":
        data["status"] = 1
    elif callback_data.status == "FAILURE":
        data["status"] = -1
    await update_dy_mj_task(callback_data.id, data)


async def split_image(image_url):
    """
    切割四格图片为四张
    """
    data = {"imageUrl": image_url}
    async with httpx.AsyncClient() as client:
        resp = await client.post(MJ_API, data=data)
    res = resp.json()
    if res.get("errno") == 0:
        return res.get("data", {}).get("images")
    return []


async def parse_web_message(ws, data):
    logger.info(data)
    if data.get("type") == "1":
        await refresh_generate_info(ws, data)
    elif data.get("type") == "2":
        await start_generating_task(ws, data)


async def get_mj_dy_images(page, limit):
    res = await get_dy_mj_images_list(page, limit)
    data = []
    async for i in res:
        data.append(
            {
                "id": i["task_id"],
                "image_url": i["image_url"],
                "prompt": i["prompt"],
                "split_images": i.get("split_images", []),
            }
        )
    return data
