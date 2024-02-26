# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    QSize,
    Qt,
)
from PySide6.QtGui import (
    QFont,
    QIcon,
)
from PySide6.QtWidgets import (
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)
from dmplay.resources import pc_rc  # noqa


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName("Login")
        Login.resize(805, 665)
        Login.setMinimumSize(QSize(191, 51))
        Login.setMaximumSize(QSize(16777215, 16777215))
        Login.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        Login.setStyleSheet("")
        self.main = QWidget(Login)
        self.main.setObjectName("main")
        self.main.setGeometry(QRect(220, 40, 380, 580))
        self.main.setMinimumSize(QSize(380, 580))
        self.main.setMaximumSize(QSize(380, 580))
        self.main.setStyleSheet(
            "#main {\n"
            "background-color: rgb(255, 255, 255);\n"
            "border-radius: 20px;\n"
            "}\n"
            ""
        )
        self.verticalLayout_2 = QVBoxLayout(self.main)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.top = QWidget(self.main)
        self.top.setObjectName("top")
        self.top.setMinimumSize(QSize(0, 160))
        self.verticalLayout_5 = QVBoxLayout(self.top)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_2 = QWidget(self.top)
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setStyleSheet("border: none;")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.hideButton = QPushButton(self.widget_2)
        self.hideButton.setObjectName("hideButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hideButton.sizePolicy().hasHeightForWidth())
        self.hideButton.setSizePolicy(sizePolicy)
        self.hideButton.setStyleSheet(
            "#hideButton:hover{\n" "padding-bottom:4px;\n" "}"
        )
        icon = QIcon()
        icon.addFile(":/icons/icons/remove-sharp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hideButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.hideButton, 0, Qt.AlignTop)

        self.closeButton = QPushButton(self.widget_2)
        self.closeButton.setObjectName("closeButton")
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setStyleSheet(
            "#closeButton:hover{\n" "padding-bottom:4px;\n" "}"
        )
        icon1 = QIcon()
        icon1.addFile(":/icons/icons/close-sharp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.closeButton, 0, Qt.AlignTop)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_4.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.top)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_6 = QVBoxLayout(self.widget_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName("label")
        font = QFont()
        font.setPointSize(35)
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.verticalLayout_4.addWidget(self.widget_3)

        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout.addWidget(self.top)

        self.inputContain = QWidget(self.main)
        self.inputContain.setObjectName("inputContain")
        self.verticalLayout_8 = QVBoxLayout(self.inputContain)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.widget_4 = QWidget(self.inputContain)
        self.widget_4.setObjectName("widget_4")
        self.widget_4.setMinimumSize(QSize(0, 200))
        self.verticalLayout_12 = QVBoxLayout(self.widget_4)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.username = QLineEdit(self.widget_4)
        self.username.setObjectName("username")
        self.username.setMinimumSize(QSize(200, 40))
        self.username.setStyleSheet(
            "border: 1px solid gray;\n"
            "            border-radius: 5px;\n"
            "            padding-top: 14px;\n"
            "            padding-left: 2px;\n"
            "            padding-right: 2px;"
        )
        self.username.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )

        self.verticalLayout_11.addWidget(
            self.username, 0, Qt.AlignmentFlag.AlignHCenter
        )

        self.password = QLineEdit(self.widget_4)
        self.password.setObjectName("password")
        self.password.setMinimumSize(QSize(200, 40))
        self.password.setStyleSheet(
            "border: 1px solid gray;\n"
            "            border-radius: 5px;\n"
            "            padding-top: 14px;\n"
            "            padding-left: 2px;\n"
            "            padding-right: 2px;"
        )
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )

        self.verticalLayout_11.addWidget(
            self.password, 0, Qt.AlignmentFlag.AlignHCenter
        )

        self.tips = QLabel(self.widget_4)
        self.tips.setObjectName("tips")
        self.tips.setStyleSheet("color: rgb(255, 0, 7);")

        self.verticalLayout_11.addWidget(self.tips, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_12.addLayout(self.verticalLayout_11)

        self.verticalLayout_7.addWidget(self.widget_4)

        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.verticalLayout.addWidget(self.inputContain)

        self.widget = QWidget(self.main)
        self.widget.setObjectName("widget")
        self.widget.setMinimumSize(QSize(0, 100))
        self.widget.setMaximumSize(QSize(354, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.widget)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName("checkBox")

        self.verticalLayout_9.addWidget(
            self.checkBox, 0, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop
        )

        self.loginButton = QPushButton(self.widget)
        self.loginButton.setObjectName("loginButton")
        self.loginButton.setMinimumSize(QSize(150, 40))
        self.loginButton.setStyleSheet(
            "#loginButton{\n"
            "	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(50, 197, 203, 255), stop:1 rgba(57, 232, 156, 255));\n"
            "            color: #f9ffff;\n"
            "            font-size: 20px;\n"
            "            font-weight: bold;\n"
            "            border-radius: 5px;\n"
            "}\n"
            "#loginButton:pressed {\n"
            "	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 214, 255, 255), stop:1 rgba(122, 217, 255, 255));\n"
            "        }"
        )

        self.verticalLayout_9.addWidget(
            self.loginButton, 0, Qt.AlignHCenter | Qt.AlignTop
        )

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName("label_2")

        self.verticalLayout_9.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.verticalLayout.addWidget(self.widget)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)

    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", "\u767b\u5f55", None))
        # if QT_CONFIG(tooltip)
        Login.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.hideButton.setText("")
        self.closeButton.setText("")
        self.label.setText(
            QCoreApplication.translate(
                "Login", "\u5f39\u5e55\u4e92\u52a8\u5de5\u5177", None
            )
        )
        self.username.setPlaceholderText(
            QCoreApplication.translate("Login", "\u7528\u6237\u540d", None)
        )
        self.password.setPlaceholderText(
            QCoreApplication.translate("Login", "\u5bc6\u7801", None)
        )
        self.tips.setText("")
        self.checkBox.setText(
            QCoreApplication.translate("Login", "\u8bb0\u4f4f\u5bc6\u7801", None)
        )
        self.loginButton.setText(
            QCoreApplication.translate("Login", "\u767b\u5f55", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("Login", "\u5fae\u4fe1\uff1a o_x-Oncemore", None)
        )

    # retranslateUi
