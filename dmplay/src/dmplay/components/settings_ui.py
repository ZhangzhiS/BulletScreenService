# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (
    QFrame,
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


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(1267, 892)
        self.main = QWidget(Form)
        self.main.setObjectName("main")
        self.main.setGeometry(QRect(260, 80, 671, 651))
        self.main.setMinimumSize(QSize(671, 651))
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
        self.topBar = QWidget(self.main)
        self.topBar.setObjectName("topBar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.topBar.sizePolicy().hasHeightForWidth())
        self.topBar.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.topBar)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.settingTitle = QLabel(self.topBar)
        self.settingTitle.setObjectName("settingTitle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(30)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.settingTitle.sizePolicy().hasHeightForWidth()
        )
        self.settingTitle.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(17)
        self.settingTitle.setFont(font)

        self.horizontalLayout.addWidget(self.settingTitle, 0, Qt.AlignHCenter)

        self.closeButton = QPushButton(self.topBar)
        self.closeButton.setObjectName("closeButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy2)
        self.closeButton.setStyleSheet(
            "#closeButton {\n"
            "border: none;\n"
            "}\n"
            "#closeButton:hover{\n"
            "padding-bottom:4px;\n"
            "}"
        )
        icon = QIcon()
        icon.addFile(":/icons/icons/close-sharp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.closeButton, 0, Qt.AlignTop)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout.addWidget(self.topBar)

        self.line = QFrame(self.main)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.container = QWidget(self.main)
        self.container.setObjectName("container")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(10)
        sizePolicy3.setHeightForWidth(self.container.sizePolicy().hasHeightForWidth())
        self.container.setSizePolicy(sizePolicy3)
        self.verticalLayout_5 = QVBoxLayout(self.container)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 12)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_3 = QWidget(self.container)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName("widget_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(3)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy4)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.st1 = QLabel(self.widget_4)
        self.st1.setObjectName("st1")
        sizePolicy4.setHeightForWidth(self.st1.sizePolicy().hasHeightForWidth())
        self.st1.setSizePolicy(sizePolicy4)

        self.horizontalLayout_4.addWidget(self.st1, 0, Qt.AlignRight)

        self.horizontalLayout_2.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName("widget_5")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(7)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy5)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.imagePath = QLineEdit(self.widget_5)
        self.imagePath.setObjectName("imagePath")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(5)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.imagePath.sizePolicy().hasHeightForWidth())
        self.imagePath.setSizePolicy(sizePolicy6)

        self.horizontalLayout_5.addWidget(self.imagePath)

        self.cDownloadPath = QPushButton(self.widget_5)
        self.cDownloadPath.setObjectName("cDownloadPath")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(
            self.cDownloadPath.sizePolicy().hasHeightForWidth()
        )
        self.cDownloadPath.setSizePolicy(sizePolicy7)
        self.cDownloadPath.setStyleSheet("#cDownloadPath{\n" "}")

        self.horizontalLayout_5.addWidget(self.cDownloadPath, 0, Qt.AlignLeft)

        self.horizontalLayout_2.addWidget(self.widget_5)

        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout_4.addWidget(self.widget_3)

        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.widget_6 = QWidget(self.container)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName("widget_7")
        sizePolicy4.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy4)
        self.horizontalLayout_8 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.st2 = QLabel(self.widget_7)
        self.st2.setObjectName("st2")
        sizePolicy4.setHeightForWidth(self.st2.sizePolicy().hasHeightForWidth())
        self.st2.setSizePolicy(sizePolicy4)

        self.horizontalLayout_8.addWidget(self.st2, 0, Qt.AlignRight)

        self.horizontalLayout_7.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName("widget_8")
        sizePolicy5.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy5)
        self.horizontalLayout_9 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.dyUrlId = QLineEdit(self.widget_8)
        self.dyUrlId.setObjectName("dyUrlId")
        sizePolicy6.setHeightForWidth(self.dyUrlId.sizePolicy().hasHeightForWidth())
        self.dyUrlId.setSizePolicy(sizePolicy6)

        self.horizontalLayout_9.addWidget(self.dyUrlId)

        self.horizontalLayout_7.addWidget(self.widget_8)

        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)

        self.verticalLayout_5.addWidget(self.widget_6)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.saveButton = QPushButton(self.container)
        self.saveButton.setObjectName("saveButton")

        self.verticalLayout_5.addWidget(self.saveButton, 0, Qt.AlignHCenter)

        self.verticalLayout.addWidget(self.container)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.settingTitle.setText(
            QCoreApplication.translate("Form", "\u8bbe\u7f6e", None)
        )
        self.closeButton.setText("")
        self.st1.setText(
            QCoreApplication.translate(
                "Form", "\u56fe\u7247\u4fdd\u5b58\u4f4d\u7f6e", None
            )
        )
        self.cDownloadPath.setText(QCoreApplication.translate("Form", "...", None))
        self.st2.setText(QCoreApplication.translate("Form", "\u6296\u97f3UrlId", None))
        self.saveButton.setText(
            QCoreApplication.translate("Form", "\u4fdd\u5b58", None)
        )

    # retranslateUi
