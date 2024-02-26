"""
弹幕互动机
"""
import sys
from importlib import metadata as importlib_metadata

from PySide6 import QtWidgets

from dmplay.interfaces.dy_mj import DYMJWindow
from dmplay.interfaces.home import HomeWindow
from dmplay.interfaces.login import LoginWindow
from dmplay.interfaces.settings import SettingsWindow


def main():
    # Linux desktop environments use app's .desktop file to integrate the app
    # to their application menus. The .desktop file of this app will include
    # StartupWMClass key, set to app's formal name, which helps associate
    # app's windows to its menu item.
    #
    # For association to work any windows of the app must have WMCLASS
    # property set to match the value set in app's desktop file. For PySide2
    # this is set with setApplicationName().

    # Find the name of the module that was used to start the app
    app_module = sys.modules["__main__"].__package__ or ""
    # Retrieve the app's metadata
    metadata = importlib_metadata.metadata(app_module)

    QtWidgets.QApplication.setApplicationName(metadata["Formal-Name"])

    app = QtWidgets.QApplication(sys.argv)
    login = LoginWindow()  # noqa
    home = HomeWindow()  # noqa
    dymj = DYMJWindow()  # noqa
    settings = SettingsWindow()  # noqa
    # dymj.show()
    sys.exit(app.exec())
