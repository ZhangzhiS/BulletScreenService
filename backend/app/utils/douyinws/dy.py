import json
import re
import urllib.parse

import requests
from google.protobuf import json_format

from .douyin_pb2 import (
    ChatMessage,
    CommonTextMessage,
    GiftMessage,
    LikeMessage,
    MatchAgainstScoreMessage,
    MemberMessage,
    ProductChangeMessage,
    RoomUserSeqMessage,
    SocialMessage,
    UpdateFanTicketMessage,
)


def unPackWebcastCommonTextMessage(data):
    commonTextMessage = CommonTextMessage()
    commonTextMessage.ParseFromString(data)
    data = json_format.MessageToDict(
        commonTextMessage, preserving_proto_field_name=True
    )
    return data


def WebcastProductChangeMessage(data):
    commonTextMessage = ProductChangeMessage()
    commonTextMessage.ParseFromString(data)
    data = json_format.MessageToDict(
        commonTextMessage, preserving_proto_field_name=True
    )
    return data


def unPackWebcastUpdateFanTicketMessage(data):
    updateFanTicketMessage = UpdateFanTicketMessage()
    updateFanTicketMessage.ParseFromString(data)
    data = json_format.MessageToDict(
        updateFanTicketMessage, preserving_proto_field_name=True
    )
    return data


def unPackWebcastRoomUserSeqMessage(data):
    roomUserSeqMessage = RoomUserSeqMessage()
    roomUserSeqMessage.ParseFromString(data)
    data = json_format.MessageToDict(
        roomUserSeqMessage, preserving_proto_field_name=True
    )
    return data


def unPackWebcastSocialMessage(data):
    socialMessage = SocialMessage()
    socialMessage.ParseFromString(data)
    data = json_format.MessageToDict(socialMessage, preserving_proto_field_name=True)
    return data


# 普通消息
def unPackWebcastChatMessage(data):
    chatMessage = ChatMessage()
    chatMessage.ParseFromString(data)
    data = json_format.MessageToDict(chatMessage, preserving_proto_field_name=True)
    return data


# 礼物消息
def unPackWebcastGiftMessage(data):
    giftMessage = GiftMessage()
    giftMessage.ParseFromString(data)
    data = json_format.MessageToDict(giftMessage, preserving_proto_field_name=True)
    return data


# xx成员进入直播间消息
def unPackWebcastMemberMessage(data):
    memberMessage = MemberMessage()
    memberMessage.ParseFromString(data)
    data = json_format.MessageToDict(memberMessage, preserving_proto_field_name=True)
    return data


# 点赞
def unPackWebcastLikeMessage(data):
    likeMessage = LikeMessage()
    likeMessage.ParseFromString(data)
    data = json_format.MessageToDict(likeMessage, preserving_proto_field_name=True)
    return data


# 解析WebcastMatchAgainstScoreMessage消息包体
def unPackMatchAgainstScoreMessage(data):
    matchAgainstScoreMessage = MatchAgainstScoreMessage()
    matchAgainstScoreMessage.ParseFromString(data)
    data = json_format.MessageToDict(
        matchAgainstScoreMessage, preserving_proto_field_name=True
    )
    return data


def parse_live_room(url):
    h = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",  # noqa
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",  # noqa
        "cookie": "__ac_nonce=0638733a400869171be51",
    }
    res = requests.get(url=url, headers=h)
    data = res.cookies.get_dict()
    ttwid = data["ttwid"]
    res = res.text
    render_data = re.findall(
        r'>self.__pace_f.push\((.*?)\)</script>', res
    )
    render_data = json.loads(render_data[-1])[-1]
    data = json.loads(render_data[2:])[-1]
    # data_str = urllib.parse.unquote(render_data, encoding="utf-8", errors="replace")
    # print(555, data_str)
    # roomStore = data["app"]["initialState"]["roomStore"]
    roomStore = data.get("state", {}).get("roomStore", {})
    if not roomStore:
        return {}
    liveRoomId = roomStore["roomInfo"]["roomId"]
    liveRoomTitle = roomStore["roomInfo"]["room"]["title"]
    live_anchor_nickname = roomStore["roomInfo"]["anchor"]["nickname"]
    # return data
    live_status = roomStore["roomInfo"]["room"]["status"]
    socia_count = -1
    if live_status == 2:
        socia_count = (
            roomStore["roomInfo"]["room"]
            .get("room_view_stats", {})
            .get("display_value", -1)
        )
    return dict(
        ttwid=ttwid,
        live_room_id=liveRoomId,
        live_room_title=liveRoomTitle,
        live_room_anchor_nickname=live_anchor_nickname,
        socia_count=socia_count,
    )
