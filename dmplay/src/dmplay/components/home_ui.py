# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QToolButton,
    QVBoxLayout,
    QWidget,
)
from dmplay.resources import pc_rc  # noqa


class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName("Home")
        Home.setEnabled(True)
        Home.resize(949, 740)
        self.main = QWidget(Home)
        self.main.setObjectName("main")
        self.main.setGeometry(QRect(280, 70, 472, 610))
        self.main.setMinimumSize(QSize(472, 610))
        self.main.setMaximumSize(QSize(472, 610))
        self.main.setStyleSheet(
            "#main{\n"
            "	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 214, 255, 255), stop:1 rgba(122, 217, 255, 255));\n"
            "    border-radius: 20px;\n"
            "}"
        )
        self.verticalLayout_2 = QVBoxLayout(self.main)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.topBar = QWidget(self.main)
        self.topBar.setObjectName("topBar")
        self.horizontalLayout_2 = QHBoxLayout(self.topBar)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.userInfo = QWidget(self.topBar)
        self.userInfo.setObjectName("userInfo")
        self.userInfo.setStyleSheet(
            "#userInfo{\n"
            "background-color: rgb(218, 255, 176);\n"
            " border-radius: 20px;\n"
            "}"
        )
        self.horizontalLayout_4 = QHBoxLayout(self.userInfo)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.avaImg = QLabel(self.userInfo)
        self.avaImg.setObjectName("avaImg")
        self.avaImg.setMinimumSize(QSize(111, 111))
        self.avaImg.setMaximumSize(QSize(111, 111))
        self.avaImg.setStyleSheet(
            "#avaImg {\n"
            "	border-image: url(:/images/images/ava.jpg);\n"
            "             border-radius: 55px;\n"
            "}"
        )
        self.avaImg.setScaledContents(True)
        self.avaImg.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.avaImg)

        self.widget_4 = QWidget(self.userInfo)
        self.widget_4.setObjectName("widget_4")
        self.widget_4.setMaximumSize(QSize(252, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(11, 0, 0, 0)
        self.nickname = QLabel(self.widget_4)
        self.nickname.setObjectName("nickname")
        font = QFont()
        font.setPointSize(26)
        self.nickname.setFont(font)

        self.verticalLayout_6.addWidget(self.nickname)

        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.vipLabel = QLabel(self.widget_7)
        self.vipLabel.setObjectName("vipLabel")

        self.horizontalLayout_5.addWidget(self.vipLabel)

        self.vipTime = QLabel(self.widget_7)
        self.vipTime.setObjectName("vipTime")

        self.horizontalLayout_5.addWidget(self.vipTime)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.verticalLayout_6.addWidget(self.widget_7)

        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QLabel(self.widget_6)
        self.label_5.setObjectName("label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.urlID = QLineEdit(self.widget_6)
        self.urlID.setObjectName("urlID")
        self.urlID.setEnabled(False)
        self.urlID.setStyleSheet(
            "#urlID{\n"
            "border-top: none;\n"
            "border-left: none;\n"
            "border-right: none;\n"
            "background-color:  transparent;\n"
            "}"
        )

        self.horizontalLayout_7.addWidget(self.urlID)

        self.editUrlIDBtn = QToolButton(self.widget_6)
        self.editUrlIDBtn.setObjectName("editUrlIDBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editUrlIDBtn.sizePolicy().hasHeightForWidth())
        self.editUrlIDBtn.setSizePolicy(sizePolicy)
        self.editUrlIDBtn.setStyleSheet(
            "QToolButton {\n"
            "            border: none;\n"
            "            background-color: transparent;\n"
            "        }\n"
            "\n"
            "QToolButton:hover{\n"
            "padding-bottom:4px;\n"
            "}"
        )
        icon = QIcon()
        icon.addFile(
            ":/icons/icons/create-outline.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.editUrlIDBtn.setIcon(icon)

        self.horizontalLayout_7.addWidget(self.editUrlIDBtn)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)

        self.verticalLayout_6.addWidget(self.widget_6)

        self.horizontalLayout_4.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.userInfo)
        self.widget_5.setObjectName("widget_5")
        self.widget_5.setStyleSheet(
            "QPushButton{\n"
            "border: none;\n"
            "background-color: transparent;\n"
            "}\n"
            "QPushButton:hover{\n"
            "padding-bottom:4px;\n"
            "}"
        )
        self.horizontalLayout_9 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.logOutButton = QPushButton(self.widget_5)
        self.logOutButton.setObjectName("logOutButton")
        self.logOutButton.setMinimumSize(QSize(26, 26))
        self.logOutButton.setStyleSheet("")
        icon1 = QIcon()
        icon1.addFile(
            ":/icons/icons/log-out-outline.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.logOutButton.setIcon(icon1)

        self.horizontalLayout_9.addWidget(self.logOutButton)

        self.settingsButton = QPushButton(self.widget_5)
        self.settingsButton.setObjectName("settingsButton")
        icon2 = QIcon()
        icon2.addFile(
            ":/icons/icons/settings-sharp.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.settingsButton.setIcon(icon2)

        self.horizontalLayout_9.addWidget(self.settingsButton)

        self.closeButton = QPushButton(self.widget_5)
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setMinimumSize(QSize(26, 26))
        icon3 = QIcon()
        icon3.addFile(":/icons/icons/close-sharp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon3)

        self.horizontalLayout_9.addWidget(self.closeButton)

        self.horizontalLayout_4.addWidget(self.widget_5, 0, Qt.AlignRight | Qt.AlignTop)

        self.horizontalLayout.addWidget(self.userInfo)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout.addWidget(self.topBar)

        self.menuBar = QWidget(self.main)
        self.menuBar.setObjectName("menuBar")
        self.verticalLayout_4 = QVBoxLayout(self.menuBar)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.menuItem = QWidget(self.menuBar)
        self.menuItem.setObjectName("menuItem")
        self.menuItem.setMinimumSize(QSize(400, 0))
        self.menuItem.setStyleSheet(
            "#menuItem{\n"
            "background-color: qlineargradient(x1:0, y1:0.5, x2:1, y2:0.5, stop:0 #47a7ed, stop: 1 #a967b2);\n"
            "border-radius: 20px;\n"
            "}"
        )
        self.horizontalLayout_3 = QHBoxLayout(self.menuItem)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QLabel(self.menuItem)
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet(
            "background-color: transparent;\n"
            "image: url(:/icons/icons/logo-tiktok.png);"
        )

        self.horizontalLayout_3.addWidget(self.label_6)

        self.label_8 = QLabel(self.menuItem)
        self.label_8.setObjectName("label_8")
        self.label_8.setStyleSheet(
            "background-color: transparent;\n" "image: url(:/icons/icons/add.png);"
        )

        self.horizontalLayout_3.addWidget(self.label_8)

        self.label_7 = QLabel(self.menuItem)
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet(
            "background-color: transparent;\n"
            "image: url(:/icons/icons/midjourney.png);"
        )

        self.horizontalLayout_3.addWidget(self.label_7)

        self.horizontalSpacer_3 = QSpacerItem(
            26, 26, QSizePolicy.Minimum, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.dyMjStartBtn = QPushButton(self.menuItem)
        self.dyMjStartBtn.setObjectName("dyMjStartBtn")
        self.dyMjStartBtn.setStyleSheet(
            "QPushButton{\n"
            "border: none;\n"
            "background-color: transparent;\n"
            "}\n"
            "QPushButton:hover{\n"
            "padding-bottom:4px;\n"
            "}"
        )
        icon4 = QIcon()
        icon4.addFile(
            ":/icons/icons/power-sharp-green.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.dyMjStartBtn.setIcon(icon4)
        self.dyMjStartBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.dyMjStartBtn)

        self.verticalLayout_3.addWidget(self.menuItem, 0, Qt.AlignHCenter)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.verticalLayout.addWidget(self.menuBar)

        self.footBar = QWidget(self.main)
        self.footBar.setObjectName("footBar")
        self.verticalLayout_5 = QVBoxLayout(self.footBar)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QLabel(self.footBar)
        self.label_9.setObjectName("label_9")

        self.verticalLayout_5.addWidget(self.label_9, 0, Qt.AlignHCenter)

        self.verticalLayout.addWidget(self.footBar)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)

    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", "\u9996\u9875", None))
        self.avaImg.setText("")
        self.nickname.setText(
            QCoreApplication.translate("Home", "\u62ef\u6551\u4e0d\u5f00\u5fc3", None)
        )
        self.vipLabel.setText(QCoreApplication.translate("Home", "VIP\uff1a", None))
        self.vipTime.setText(QCoreApplication.translate("Home", "2024-12-22", None))
        self.label_5.setText(
            QCoreApplication.translate("Home", "\u76f4\u64ad\u95f4ID\uff1a", None)
        )
        self.urlID.setText(QCoreApplication.translate("Home", "", None))
        self.editUrlIDBtn.setText(QCoreApplication.translate("Home", "...", None))
        self.logOutButton.setText("")
        self.settingsButton.setText("")
        self.closeButton.setText("")
        self.label_6.setText("")
        self.label_8.setText("")
        self.label_7.setText("")
        self.dyMjStartBtn.setText("")
        self.label_9.setText(
            QCoreApplication.translate(
                "Home", "\u5f39\u5e55\u76f4\u64ad\u5de5\u5177", None
            )
        )

    # retranslateUi
