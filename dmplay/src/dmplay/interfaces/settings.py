from PySide6.QtWidgets import QFileDialog

from dmplay.components.settings_ui import Ui_Form
from dmplay.core.config import config, save_config_to_json
from dmplay.core.window_base import WindowBase
from dmplay.core.windows_manager import window_manager


class SettingsWindow(WindowBase):

    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.closeButton.clicked.connect(self.customClose)
        self.ui.cDownloadPath.clicked.connect(self.select_path)

        self.ui.topBar.mousePressEvent = self.on_mouse_press
        self.ui.topBar.mouseMoveEvent = self.on_mouse_move

        window_manager.show_settings.connect(self.customShow)

        self.ui.closeButton.clicked.connect(self.customClose)
        self.ui.saveButton.clicked.connect(self.save_config)

    def customClose(self):
        self.close()

    def customShow(self):
        self.ui.imagePath.setText(config.DOWNLOAD_PATH or "")
        self.ui.dyUrlId.setText(config.LIVE_URL_ID or "")
        self.show()

    def select_path(self):
        # 使用系统文件窗口选择路径
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        if dialog.exec():
            selected_path = dialog.selectedFiles()[0]
            config.DOWNLOAD_PATH = selected_path
            self.ui.imagePath.setText(selected_path)

    def save_config(self):
        config.DOWNLOAD_PATH = self.ui.imagePath.text()
        config.LIVE_URL_ID = self.ui.dyUrlId.text()
        save_config_to_json(config)
        self.close()
