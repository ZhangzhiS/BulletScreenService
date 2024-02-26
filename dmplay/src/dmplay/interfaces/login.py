import requests
from loguru import logger
from PySide6.QtCore import QObject, QRunnable, Qt, QThreadPool, Signal, Slot

from dmplay.components.login_ui import Ui_Login

from dmplay.core.config import config, save_config_to_json
from dmplay.core.window_base import WindowBase
from dmplay.core.windows_manager import window_manager

# BACKEND_DOMAIN = "127.0.0.1:8081"
BACKEND_DOMAIN = "hello.zzs7.top"


class LoginSignal(QObject):
    finished = Signal(dict)


class LoginWorker(QRunnable):
    """"""

    def __init__(self, username, password) -> None:
        super().__init__()
        self.username = username
        self.password = password
        self.signal = LoginSignal()

    def run(self):
        res = requests.post(
            f"http://{BACKEND_DOMAIN}/api/v1/login",
            json={"username": self.username, "password": self.password},
        )
        if res.status_code == 200:
            resp = res.json()
            self.signal.finished.emit(resp)
            return
        self.signal.finished.emit({"code": -1})


class LoginWindow(WindowBase):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        # 关闭原生的菜单栏以及背景透明
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.ui.closeButton.clicked.connect(self.customClose)
        self.ui.hideButton.clicked.connect(self.customHide)

        self.ui.loginButton.clicked.connect(self.login)
        self.ui.checkBox.stateChanged.connect(self.rember_password)

        self.ui.username.setText(config.USERNAME or "")

        if config.REMBER_PASSWORD:
            self.ui.checkBox.setCheckState(Qt.CheckState.Checked)
            self.ui.password.setText(config.PASSWORD or "")
        else:
            self.ui.checkBox.setCheckState(Qt.CheckState.Unchecked)
        # 自定义拖动窗口
        self.ui.main.mousePressEvent = self.on_mouse_press
        self.ui.main.mouseMoveEvent = self.on_mouse_move

        window_manager.show_login.connect(self.custom_show)

        self.threadpool = QThreadPool()

        self.show()
        logger.info("show login")

    def rember_password(self, state):
        logger.info(state)
        if state:
            config.REMBER_PASSWORD = True
            save_config_to_json(config)

    def custom_show(self):
        self.show()

    def customClose(self):
        self.close()

    def customHide(self):
        self.hide()

    @Slot(dict)
    def parse_login(self, data):
        logger.info(data)
        if data.get("code") == 20000:
            config.USERNAME = self.ui.username.text()
            if self.ui.checkBox.isChecked():
                config.PASSWORD = self.ui.password.text()
            config.ACCESS_TOKEN = data.get("data").get("access_token")
            save_config_to_json(config)
            self.hide()
            logger.info("show home")
            window_manager.show_home.emit()
        else:
            self.ui.tips.setText(data.get("msg"))

    def login(self):
        username = self.ui.username.text()
        password = self.ui.password.text()
        self.login_worker = LoginWorker(username, password)
        self.login_worker.signal.finished.connect(self.parse_login)
        self.threadpool.start(self.login_worker)
