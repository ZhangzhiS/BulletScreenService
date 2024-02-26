import enum


class SendMsg(enum.Enum):
    REFRESH_GENERATE_INFO = "1"
    START_GENERATE = "2"


class WindowState(enum.Enum):
    CLOSE = -1
    HIDE = 0
    SHOW = 1

