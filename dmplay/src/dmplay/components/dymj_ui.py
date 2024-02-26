# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dymj.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QListWidget,
    QProgressBar,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from dmplay.resources import pc_rc  # noqa


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(1920, 1080)
        Form.setMinimumSize(QSize(0, 0))
        self.verticalLayout_28 = QVBoxLayout(Form)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.main = QWidget(Form)
        self.main.setObjectName("main")
        self.main.setMinimumSize(QSize(0, 0))
        self.main.setStyleSheet(
            "#main{\n" "	background-color: rgb(255, 255, 255);\n" "\n" "}"
        )
        self.verticalLayout_2 = QVBoxLayout(self.main)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.topBar = QWidget(self.main)
        self.topBar.setObjectName("topBar")
        self.topBar.setMinimumSize(QSize(0, 60))
        self.topBar.setMaximumSize(QSize(16777215, 70))
        self.topBar.setStyleSheet(
            "#topBar{\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(50, 197, 203, 255), stop:1 rgba(57, 232, 156, 255));\n"
            "}"
        )
        self.horizontalLayout_3 = QHBoxLayout(self.topBar)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, -1, 13, -1)
        self.roomInfo = QWidget(self.topBar)
        self.roomInfo.setObjectName("roomInfo")
        self.roomInfo.setStyleSheet("background-color: transparent;")
        self.horizontalLayout_5 = QHBoxLayout(self.roomInfo)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.avaImg = QLabel(self.roomInfo)
        self.avaImg.setObjectName("avaImg")
        self.avaImg.setMinimumSize(QSize(30, 30))
        self.avaImg.setMaximumSize(QSize(30, 30))
        self.avaImg.setStyleSheet(
            "#avaImg {\n"
            "	border-image: url(:/icons/icons/midjourney.png);\n"
            "             border-radius: 10px;\n"
            "}"
        )
        self.avaImg.setScaledContents(True)
        self.avaImg.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.avaImg)

        self.nickname = QLabel(self.roomInfo)
        self.nickname.setObjectName("nickname")
        self.nickname.setMaximumSize(QSize(115, 16777215))
        self.nickname.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.nickname)

        self.title = QLabel(self.roomInfo)
        self.title.setObjectName("title")

        self.horizontalLayout_4.addWidget(self.title)

        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout.addWidget(self.roomInfo)

        self.tips = QWidget(self.topBar)
        self.tips.setObjectName("tips")
        self.tips.setStyleSheet("#tips {\n" "background-color: transparent;\n" "}")
        self.horizontalLayout_6 = QHBoxLayout(self.tips)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tips_content = QLabel(self.tips)
        self.tips_content.setObjectName("tips_content")
        self.tips_content.setMinimumSize(QSize(134, 35))
        self.tips_content.setMaximumSize(QSize(16777215, 40))
        self.tips_content.setStyleSheet(
            "#tips_content{\n" "border: 1px solid gray;\n" "border-radius: 5px;\n" "}"
        )
        self.tips_content.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(
            self.tips_content, 0, Qt.AlignHCenter | Qt.AlignVCenter
        )

        self.horizontalLayout_6.addLayout(self.horizontalLayout_8)

        self.horizontalLayout.addWidget(self.tips)

        self.barAction = QWidget(self.topBar)
        self.barAction.setObjectName("barAction")
        self.barAction.setStyleSheet("background-color: transparent;")
        self.horizontalLayout_7 = QHBoxLayout(self.barAction)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.barAction)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, 2, -1)
        self.countTitle = QLabel(self.widget_6)
        self.countTitle.setObjectName("countTitle")
        self.countTitle.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.countTitle, 0, Qt.AlignRight)

        self.countNum = QLCDNumber(self.widget_6)
        self.countNum.setObjectName("countNum")
        self.countNum.setMaximumSize(QSize(46, 16777215))
        font = QFont()
        font.setPointSize(13)
        self.countNum.setFont(font)
        self.countNum.setStyleSheet(
            "#countNum {\n"
            "background-color: transparent;\n"
            "   border: none;\n"
            "            color: black;\n"
            "}"
        )

        self.horizontalLayout_9.addWidget(self.countNum, 0, Qt.AlignLeft)

        self.connectButton = QPushButton(self.widget_6)
        self.connectButton.setObjectName("connectButton")
        self.connectButton.setMinimumSize(QSize(100, 30))
        self.connectButton.setLayoutDirection(Qt.RightToLeft)
        self.connectButton.setStyleSheet(
            "QPushButton {\n"
            "\n"
            "              border-radius: 10px;\n"
            "border: 1px solid gray;\n"
            "        }\n"
            "        QPushButton:hover {\n"
            "           	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 214, 255, 255), stop:1 rgba(122, 217, 255, 255));\n"
            "        }\n"
            "        \n"
            "        QPushButton:pressed {\n"
            "\n"
            " background-color: qlineargradient(x1:0, y1:0.5, x2:1, y2:0.5, stop:0 #459ee0, stop: 1 #995da1);\n"
            "        }"
        )
        icon = QIcon()
        icon.addFile(
            ":/icons/icons/wifi-sharp-red.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.connectButton.setIcon(icon)

        self.horizontalLayout_9.addWidget(self.connectButton)

        self.closeButton = QPushButton(self.widget_6)
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setStyleSheet(
            "QPushButton{\n"
            "border: none;\n"
            "}\n"
            "QPushButton:hover{\n"
            "padding-bottom:4px;\n"
            "}"
        )
        icon1 = QIcon()
        icon1.addFile(":/icons/icons/power-sharp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon1)

        self.horizontalLayout_9.addWidget(self.closeButton, 0, Qt.AlignRight)

        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_7.addWidget(self.widget_6)

        self.horizontalLayout.addWidget(self.barAction)

        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout.addWidget(self.topBar)

        self.container = QWidget(self.main)
        self.container.setObjectName("container")
        sizePolicy = QSizePolicy(
            QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding
        )
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.container.sizePolicy().hasHeightForWidth())
        self.container.setSizePolicy(sizePolicy)
        self.container.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_3 = QVBoxLayout(self.container)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_4 = QWidget(self.container)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_5 = QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.mainContainer = QWidget(self.widget_4)
        self.mainContainer.setObjectName("mainContainer")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(19)
        sizePolicy1.setHeightForWidth(
            self.mainContainer.sizePolicy().hasHeightForWidth()
        )
        self.mainContainer.setSizePolicy(sizePolicy1)
        self.horizontalLayout_12 = QHBoxLayout(self.mainContainer)
        # ifndef Q_OS_MAC
        self.horizontalLayout_12.setSpacing(-1)
        # endif
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.leftContainer = QWidget(self.mainContainer)
        self.leftContainer.setObjectName("leftContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.leftContainer.sizePolicy().hasHeightForWidth()
        )
        self.leftContainer.setSizePolicy(sizePolicy2)
        self.leftContainer.setMinimumSize(QSize(0, 0))
        self.leftContainer.setMaximumSize(QSize(16777215, 16777215))
        self.leftContainer.setStyleSheet("\n" "border-radius: 5px;")
        self.verticalLayout_8 = QVBoxLayout(self.leftContainer)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.nextGenerate = QWidget(self.leftContainer)
        self.nextGenerate.setObjectName("nextGenerate")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(
            self.nextGenerate.sizePolicy().hasHeightForWidth()
        )
        self.nextGenerate.setSizePolicy(sizePolicy3)
        self.nextGenerate.setMinimumSize(QSize(0, 0))
        self.nextGenerate.setMaximumSize(QSize(16777215, 200))
        self.nextGenerate.setStyleSheet(
            " #nextGenerate{\n" "border: 1px solid gray;\n" "border-radius: 5px;\n" "}"
        )
        self.verticalLayout_10 = QVBoxLayout(self.nextGenerate)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget = QWidget(self.nextGenerate)
        self.widget.setObjectName("widget")
        sizePolicy3.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy3)
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label = QLabel(self.widget)
        self.label.setObjectName("label")
        font1 = QFont()
        font1.setPointSize(20)
        self.label.setFont(font1)

        self.verticalLayout_23.addWidget(self.label, 0, Qt.AlignHCenter)

        self.horizontalLayout_2.addLayout(self.verticalLayout_23)

        self.verticalLayout_9.addWidget(self.widget)

        self.widget_3 = QWidget(self.nextGenerate)
        self.widget_3.setObjectName("widget_3")
        sizePolicy3.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy3)
        self.verticalLayout_25 = QVBoxLayout(self.widget_3)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName("label_3")

        self.horizontalLayout_15.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.nextUser = QLabel(self.widget_5)
        self.nextUser.setObjectName("nextUser")
        self.nextUser.setOpenExternalLinks(False)

        self.horizontalLayout_15.addWidget(self.nextUser)

        self.horizontalLayout_16.addLayout(self.horizontalLayout_15)

        self.verticalLayout_24.addWidget(self.widget_5)

        self.widget_7 = QWidget(self.widget_3)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_5 = QLabel(self.widget_7)
        self.label_5.setObjectName("label_5")

        self.horizontalLayout_17.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(self.widget_7)
        self.label_2.setObjectName("label_2")

        self.horizontalLayout_17.addWidget(self.label_2)

        self.horizontalLayout_18.addLayout(self.horizontalLayout_17)

        self.verticalLayout_24.addWidget(self.widget_7)

        self.verticalLayout_25.addLayout(self.verticalLayout_24)

        self.verticalLayout_9.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.nextGenerate)
        self.widget_2.setObjectName("widget_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(2)
        sizePolicy4.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy4)
        self.verticalLayout_27 = QVBoxLayout(self.widget_2)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.textBrowser = QTextBrowser(self.widget_2)
        self.textBrowser.setObjectName("textBrowser")

        self.verticalLayout_26.addWidget(self.textBrowser)

        self.verticalLayout_27.addLayout(self.verticalLayout_26)

        self.verticalLayout_9.addWidget(self.widget_2)

        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.verticalLayout_7.addWidget(self.nextGenerate)

        self.rule = QWidget(self.leftContainer)
        self.rule.setObjectName("rule")
        sizePolicy4.setHeightForWidth(self.rule.sizePolicy().hasHeightForWidth())
        self.rule.setSizePolicy(sizePolicy4)
        self.rule.setStyleSheet(
            "#rule{\n" "border: 1px solid gray;\n" "border-radius: 5px;\n" "}"
        )
        self.verticalLayout_14 = QVBoxLayout(self.rule)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(2, 2, 2, 2)
        self.label_6 = QLabel(self.rule)
        self.label_6.setObjectName("label_6")
        self.label_6.setMaximumSize(QSize(16777215, 24))
        self.label_6.setFont(font1)

        self.verticalLayout_13.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.widget_9 = QWidget(self.rule)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_12 = QVBoxLayout(self.widget_9)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.partRule = QListWidget(self.widget_9)
        self.partRule.setObjectName("partRule")
        self.partRule.setStyleSheet("#partRule {\n" "line-height: 30px;\n" "}")
        self.partRule.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.partRule)

        self.verticalLayout_12.addLayout(self.verticalLayout_11)

        self.verticalLayout_13.addWidget(self.widget_9)

        self.widget_8 = QWidget(self.rule)
        self.widget_8.setObjectName("widget_8")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy5)
        self.horizontalLayout_20 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.lineEdit = QLineEdit(self.widget_8)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("border: 1px solid gray;")

        self.horizontalLayout_19.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.widget_8)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("border: 1px solid gray;")

        self.horizontalLayout_19.addWidget(self.pushButton)

        self.horizontalLayout_20.addLayout(self.horizontalLayout_19)

        self.verticalLayout_13.addWidget(self.widget_8)

        self.verticalLayout_14.addLayout(self.verticalLayout_13)

        self.verticalLayout_7.addWidget(self.rule)

        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.horizontalLayout_11.addWidget(self.leftContainer)

        self.centerContainer = QWidget(self.mainContainer)
        self.centerContainer.setObjectName("centerContainer")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(4)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(
            self.centerContainer.sizePolicy().hasHeightForWidth()
        )
        self.centerContainer.setSizePolicy(sizePolicy6)
        self.centerContainer.setStyleSheet("")
        self.verticalLayout_6 = QVBoxLayout(self.centerContainer)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15 = QVBoxLayout()
        # ifndef Q_OS_MAC
        self.verticalLayout_15.setSpacing(-1)
        # endif
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, -1, -1, 0)
        self.imagePreview = QWidget(self.centerContainer)
        self.imagePreview.setObjectName("imagePreview")
        sizePolicy7 = QSizePolicy(
            QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding
        )
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(5)
        sizePolicy7.setHeightForWidth(
            self.imagePreview.sizePolicy().hasHeightForWidth()
        )
        self.imagePreview.setSizePolicy(sizePolicy7)
        self.imagePreview.setMinimumSize(QSize(0, 0))
        self.imagePreview.setMaximumSize(QSize(16777215, 16777215))
        self.imagePreview.setSizeIncrement(QSize(1, 1))
        self.imagePreview.setStyleSheet(
            "#imagePreview{\n"
            "border: 1px solid gray;\n"
            "\n"
            "border-radius: 5px;\n"
            "}\n"
            ""
        )
        self.verticalLayout_22 = QVBoxLayout(self.imagePreview)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.image = QLabel(self.imagePreview)
        self.image.setObjectName("image")
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setStyleSheet(
            "#image{\n"
            "image: url(:/images/images/default.png);\n"
            "             border-radius: 10px;\n"
            "}"
        )
        self.image.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.image)

        self.verticalLayout_15.addWidget(self.imagePreview)

        self.progressBar = QProgressBar(self.centerContainer)
        self.progressBar.setObjectName("progressBar")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(1)
        sizePolicy8.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy8)
        self.progressBar.setMinimumSize(QSize(547, 30))
        self.progressBar.setMaximumSize(QSize(16777215, 16777215))
        self.progressBar.setStyleSheet(
            "QProgressBar {\n"
            "            border: 2px solid lightgray;\n"
            "            border-radius: 5px;\n"
            "            text-align: center;\n"
            "            color: white;\n"
            "        }\n"
            "\n"
            "QProgressBar::chunk {\n"
            "	background-color: qlineargradient(spread:pad, x1:1, y1:0.21, x2:0, y2:0.722, stop:0 rgba(207, 160, 211, 255), stop:1 rgba(255, 236, 236, 255));\n"
            "            border-radius: 4px;\n"
            "        }"
        )
        self.progressBar.setValue(100)

        self.verticalLayout_15.addWidget(self.progressBar)

        self.previewUserInfo = QWidget(self.centerContainer)
        self.previewUserInfo.setObjectName("previewUserInfo")
        sizePolicy3.setHeightForWidth(
            self.previewUserInfo.sizePolicy().hasHeightForWidth()
        )
        self.previewUserInfo.setSizePolicy(sizePolicy3)
        self.previewUserInfo.setMinimumSize(QSize(100, 0))
        self.previewUserInfo.setMaximumSize(QSize(16777215, 140))
        self.previewUserInfo.setStyleSheet(
            "#previewUserInfo{\n"
            "border-radius: 5px;\n"
            "border: 1px solid gray;\n"
            "}"
        )
        self.verticalLayout_18 = QVBoxLayout(self.previewUserInfo)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.previewInfo = QListWidget(self.previewUserInfo)
        self.previewInfo.setObjectName("previewInfo")

        self.verticalLayout_17.addWidget(self.previewInfo)

        self.verticalLayout_18.addLayout(self.verticalLayout_17)

        self.verticalLayout_15.addWidget(self.previewUserInfo)

        self.verticalLayout_6.addLayout(self.verticalLayout_15)

        self.horizontalLayout_11.addWidget(self.centerContainer)

        self.generateHistory = QWidget(self.mainContainer)
        self.generateHistory.setObjectName("generateHistory")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(1)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(
            self.generateHistory.sizePolicy().hasHeightForWidth()
        )
        self.generateHistory.setSizePolicy(sizePolicy9)
        self.generateHistory.setMinimumSize(QSize(0, 0))
        self.generateHistory.setStyleSheet(
            "#generateHistory{\n"
            "border: 1px solid gray;\n"
            "border-radius: 5px;\n"
            "}"
        )
        self.verticalLayout_21 = QVBoxLayout(self.generateHistory)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(2, -1, 2, -1)
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_8 = QLabel(self.generateHistory)
        self.label_8.setObjectName("label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_20.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.historyList = QListWidget(self.generateHistory)
        self.historyList.setObjectName("historyList")
        self.historyList.setStyleSheet("#historyList{\n" "border: none;\n" "}")

        self.verticalLayout_20.addWidget(self.historyList)

        self.verticalLayout_21.addLayout(self.verticalLayout_20)

        self.horizontalLayout_11.addWidget(self.generateHistory)

        self.rightContainer = QWidget(self.mainContainer)
        self.rightContainer.setObjectName("rightContainer")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(2)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(
            self.rightContainer.sizePolicy().hasHeightForWidth()
        )
        self.rightContainer.setSizePolicy(sizePolicy10)
        self.rightContainer.setMinimumSize(QSize(0, 0))
        self.rightContainer.setMaximumSize(QSize(16777215, 16777215))
        self.rightContainer.setStyleSheet(
            "#rightContainer{\n" "border: 1px solid gray;\n" "border-radius: 5px;\n" "}"
        )
        self.verticalLayout_16 = QVBoxLayout(self.rightContainer)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_7 = QLabel(self.rightContainer)
        self.label_7.setObjectName("label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_19.addWidget(
            self.label_7, 0, Qt.AlignHCenter | Qt.AlignBottom
        )

        self.rankScoreList = QListWidget(self.rightContainer)
        self.rankScoreList.setObjectName("rankScoreList")
        self.rankScoreList.setStyleSheet(
            "#rankScoreList:item{\n"
            "    height: 40px;\n"
            "            margin: 5px 5px 5px 5px;\n"
            "            background-color: white;\n"
            "            border-radius: 6px;\n"
            "}"
            "#rankScoreList{border: none;}"
            
        )

        self.verticalLayout_19.addWidget(self.rankScoreList)

        self.verticalLayout_16.addLayout(self.verticalLayout_19)

        self.horizontalLayout_11.addWidget(self.rightContainer)

        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)

        self.verticalLayout_5.addWidget(self.mainContainer)

        self.footBar = QWidget(self.widget_4)
        self.footBar.setObjectName("footBar")
        sizePolicy11 = QSizePolicy(
            QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding
        )
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(4)
        sizePolicy11.setHeightForWidth(self.footBar.sizePolicy().hasHeightForWidth())
        self.footBar.setSizePolicy(sizePolicy11)
        self.footBar.setMinimumSize(QSize(0, 50))
        self.footBar.setMaximumSize(QSize(16777215, 50))
        self.footBar.setStyleSheet(
            "#footBar{\n" "background-color: rgb(214, 214, 214);\n" "}"
        )
        self.horizontalLayout_14 = QHBoxLayout(self.footBar)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_4 = QLabel(self.footBar)
        self.label_4.setObjectName("label_4")
        self.label_4.setMaximumSize(QSize(100, 30))
        self.label_4.setStyleSheet(
            "image: url(:/icons/icons/warning-sharp.png);\n"
            "background-color: rgba(255, 255, 255, 0);"
        )

        self.horizontalLayout_13.addWidget(self.label_4)

        self.inputPrompt = QLabel(self.footBar)
        self.inputPrompt.setObjectName("inputPrompt")
        font2 = QFont()
        font2.setPointSize(25)
        font2.setBold(True)
        self.inputPrompt.setFont(font2)
        self.inputPrompt.setStyleSheet(
            "\n"
            "#inputPrompt{\n"
            "color: rgb(255, 126, 121);\n"
            "	background-color: rgba(255, 255, 255, 0);\n"
            "}"
        )

        self.horizontalLayout_13.addWidget(self.inputPrompt, 0, Qt.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum
        )

        self.horizontalLayout_13.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_14.addLayout(self.horizontalLayout_13)

        self.verticalLayout_5.addWidget(self.footBar)

        self.verticalLayout_4.addWidget(self.widget_4)

        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout.addWidget(self.container)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_28.addWidget(self.main)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(
            QCoreApplication.translate("Form", "\u6296\u97f3+AI\u56fe\u7247", None)
        )
        self.avaImg.setText("")
        self.nickname.setText(
            QCoreApplication.translate("Form", "\u62ef\u6551\u4e0d\u5f00\u5fc3", None)
        )
        self.title.setText(
            QCoreApplication.translate(
                "Form",
                "\u5feb\u6765\u751f\u6210\u4f60\u597d\u770b\u7684\u5934\u50cf\u5427",
                None,
            )
        )
        self.tips_content.setText(
            QCoreApplication.translate("Form", "\u672a\u8fde\u63a5", None)
        )
        self.countTitle.setText(
            QCoreApplication.translate(
                "Form", "\u76f4\u64ad\u95f4\u4eba\u6570\u4e3a\uff1a", None
            )
        )
        self.connectButton.setText(
            QCoreApplication.translate("Form", "\u8fde\u63a5\u76f4\u64ad\u95f4", None)
        )
        self.closeButton.setText("")
        self.label.setText(
            QCoreApplication.translate("Form", "\u4e0b\u6b21\u751f\u6210", None)
        )
        self.label_3.setText(
            QCoreApplication.translate("Form", "\u7528\u6237\u540d", None)
        )
        self.nextUser.setText(QCoreApplication.translate("Form", "\u6682\u65e0", None))
        self.label_5.setText(
            QCoreApplication.translate("Form", "\u63d0\u793a\u8bcd", None)
        )
        self.label_2.setText("")
        self.textBrowser.setHtml(
            QCoreApplication.translate(
                "Form",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
                None,
            )
        )
        self.label_6.setText(
            QCoreApplication.translate("Form", "\u53c2\u4e0e\u89c4\u5219", None)
        )
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate("Form", "\u8f93\u5165\u516c\u544a", None)
        )
        self.pushButton.setText(
            QCoreApplication.translate("Form", "\u6dfb\u52a0", None)
        )
        self.image.setText("")
        self.progressBar.setFormat(
            QCoreApplication.translate("Form", "\u5df2\u5b8c\u6210", None)
        )
        self.label_8.setText(QCoreApplication.translate("Form", "\u5386\u53f2", None))
        self.label_7.setText(
            QCoreApplication.translate("Form", "\u6392\u961f\u5217\u8868", None)
        )
        self.label_4.setText("")
        self.inputPrompt.setText(
            QCoreApplication.translate(
                "Form",
                '\u63d0\u793a\u8bcd\u5b9e\u4f8b\uff08\u5fc5\u987b\u4ee5"\u751f\u6210-"\u5f00\u59cb\uff09\uff1a\u751f\u6210-\u9177\u9177\u7684\u732b\u5728\u9633\u53f0\u6652\u592a\u9633',
                None,
            )
        )

    # retranslateUi
