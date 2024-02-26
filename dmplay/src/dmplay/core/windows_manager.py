
from PySide6.QtCore import QObject, Signal


class WindowManager(QObject):
    show_login = Signal()
    close_login = Signal()
    hide_login = Signal()

    show_home = Signal()
    close_home = Signal()
    hide_home = Signal()

    show_dymj = Signal()
    close_dymj = Signal()
    hide_dymj = Signal()

    show_settings = Signal()
    close_settings = Signal()
    hide_settings = Signal()


window_manager = WindowManager()
