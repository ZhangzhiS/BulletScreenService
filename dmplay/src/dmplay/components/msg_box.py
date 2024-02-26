from typing import Optional

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QWidget


class MessageBox(QDialog):
    def __init__(self, parent: Optional[QWidget] = ...) -> None:
        super().__init__(parent)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.verticalLayout_2 = QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QWidget(self)
        self.widget.setObjectName("widget")
        self.widget.setMinimumSize(QSize(418, 181))
        self.widget.setMaximumSize(QSize(418, 181))
        self.widget.setStyleSheet(
            "background-color: rgb(231, 231, 231);\n" "border-radius: 30px;"
        )
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 30)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.msg = QLabel(self.widget)
        self.msg.setWordWrap(True)
        self.msg.setObjectName("msg")
        self.msg.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter
        )
        font = QFont()
        font.setPointSize(25)
        self.msg.setFont(font)

        self.verticalLayout_3.addWidget(self.msg, 0, Qt.AlignmentFlag.AlignHCenter)

        self.confirmButton = QPushButton(self.widget)
        self.confirmButton.setObjectName("confirmButton")
        self.confirmButton.setMinimumSize(QSize(160, 30))
        self.confirmButton.setMaximumSize(QSize(160, 30))
        self.confirmButton.setDisabled(True)
        self.confirmButton.setStyleSheet(
            "#confirmButton {\n"
            "    background-color: #57bd6a;\n"
            "    border-radius: 15px;\n"
            "}\n"
            "#confirmButton:pressed {\n"
            "    background-color: #4eaa5f;\n"
            "}"
        )

        self.verticalLayout_3.addWidget(self.confirmButton, 0, Qt.AlignHCenter)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout.addWidget(self.widget)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Dialog", None))
        self.msg.setText(QCoreApplication.translate("Dialog", "Msg", None))
        self.confirmButton.setText(
            QCoreApplication.translate(
                "Dialog",
                "\u786e\u8ba4\uff083\u79d2\u540e\u81ea\u52a8\u5173\u95ed\uff09",
                None,
            )
        )

    # retranslateUi
