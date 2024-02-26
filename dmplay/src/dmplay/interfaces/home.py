from loguru import logger
from PySide6.QtCore import QSize, Slot
from PySide6.QtGui import QIcon

from dmplay.components.home_ui import Ui_Home
from dmplay.core.config import config, save_config_to_json
from dmplay.core.window_base import WindowBase
from dmplay.core.windows_manager import window_manager


class HomeWindow(WindowBase):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Home()
        self.ui.setupUi(self)

        self.ui.closeButton.clicked.connect(self.customClose)
        self.ui.logOutButton.clicked.connect(self.log_out)
        self.ui.editUrlIDBtn.clicked.connect(self.edit_dymj_id_button)
        self.ui.dyMjStartBtn.clicked.connect(self.start_dy_mj)

        self.ui.settingsButton.clicked.connect(
            window_manager.show_settings.emit
        )

        self.ui.userInfo.mousePressEvent = self.on_mouse_press
        self.ui.userInfo.mouseMoveEvent = self.on_mouse_move


        self.ui.urlID.textChanged.connect(self.edit_dymj_id_event)
        window_manager.show_home.connect(self.customShow)
        self.edit_status = True

    def start_dy_mj(self):
        window_manager.show_dymj.emit()
        self.hide()

    @Slot()
    def customShow(self):
        logger.info("show home")
        if config.LIVE_URL_ID:
            self.ui.urlID.setText(config.LIVE_URL_ID)
        self.show()

    def customClose(self):
        save_config_to_json(config)
        self.close()

    def edit_dymj_id_event(self, text):
        config.LIVE_URL_ID = text

    def edit_dymj_id_button(self):
        logger.info(self.edit_status)
        self.ui.urlID.setEnabled(self.edit_status)
        icon = QIcon()
        icon_str = "create-outline" if not self.edit_status else "checkmark-outline"
        icon.addFile(f":/icons/icons/{icon_str}.png", QSize())
        self.ui.editUrlIDBtn.setIcon(icon)
        self.edit_status = not self.edit_status
        background_color = "transparent" if self.edit_status else "white"
        self.ui.urlID.setStyleSheet(f"""
            border-top: none;
            border-left: none;
            border-right: none;
            background-color: {background_color};
        """)
        if self.edit_status is False:
            config.LIVE_URL_ID = self.ui.urlID.text()
            save_config_to_json(config)

    def open_dy_mj(self):
        "open_dy_mj"
        # TODO: OPEN DYMJ

    def log_out(self):
        self.close()
        window_manager.show_login.emit()
        # TODO: OPEN LOGIN

    def custom_hide(self):
        self.hide()

