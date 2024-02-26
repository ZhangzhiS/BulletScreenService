import json
import websocket

from PySide6.QtCore import QObject, QRunnable, Signal, Slot
from loguru import logger

from dmplay.core.config import config


# BACKEND_DOMAIN = "hello.zzs7.top"
BACKEND_DOMAIN = "127.0.0.1:8081"


class WebSocketWorderSignals(QObject):
    refresh_rank_list = Signal(list)  # 更新积分排名
    refresh_room_info = Signal(dict)
    refresh_generating_info = Signal(dict)
    refresh_start_task = Signal(dict)
    do_alt_msg = Signal(str)
    on_open_connect = Signal(bool)


class WebSocketWorker(QRunnable):
    def __init__(self) -> None:
        super().__init__()
        self.signals = WebSocketWorderSignals()
        self.url = f"ws://{BACKEND_DOMAIN}/douyin/{config.LIVE_URL_ID}/ws"

    def on_message(self, ws, message):
        message = json.loads(message)
        logger.info(message)
        msg_type = message.get("msg_type")
        if msg_type == "refresh_room_info":
            self.signals.refresh_room_info.emit(message["data"])
        elif msg_type == "refresh_rank_list":
            rank_info = message.get("data", [])
            self.signals.refresh_rank_list.emit(rank_info)
        elif msg_type == "refresh_last_generating_info":
            data = message.get("data", {})
            self.signals.refresh_generating_info.emit(data)
        elif msg_type == "alt_msg":
            msg = message.get("data", {}).get("msg")
            self.signals.do_alt_msg.emit(msg)
        elif msg_type == "start_task":
            data = message.get("data", {})
            self.signals.refresh_start_task.emit(data)
        elif msg_type == "close_connect":
            msg = message.get("data", {}).get("msg")
            self.signals.do_alt_msg.emit(msg)
            self.signals.on_open_connect.emit(False)
            ws.close(status=websocket.STATUS_NORMAL)

    def on_open(self, ws):
        self.signals.on_open_connect.emit(True)

    def on_error(self, ws_client, msg):
        logger.info(f"error: {msg}")
        self.signals.on_open_connect.emit(False)

    def on_close(self, ws, close_status_code, close_msg):
        logger.info(f"close_status_code: {close_status_code}")
        logger.info(f"close_msg: {close_msg}")

    def close_websocket(self):
        if self.client is not None:
            self.client.close()

    def send(self, data):
        data = json.dumps(data)
        self.client.send(data)

    @Slot()
    def run(self):
        self.client = websocket.WebSocketApp(
            self.url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open,
            header={"token": config.ACCESS_TOKEN},
        )
        self.client.run_forever()
