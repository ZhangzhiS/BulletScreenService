from PySide6.QtWidgets import  QMainWindow
from PySide6.QtCore import Qt

class WindowBase(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.drag_position = None

    def on_mouse_press(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()

    def on_mouse_move(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            if self.drag_position is not None:
                self.move(event.globalPos() - self.drag_position)
                event.accept()

    def on_show(self):
        pass

    def on_hide(self):
        pass

    def on_close(self):
        pass
