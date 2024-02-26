from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)



class RuleItem(QWidget):
    def __init__(
        self,
        rule_str: str,
        parent: Optional[QWidget] = None,
    ) -> None:
        super().__init__(parent)
        main_widget = QWidget(parent)
        # self.widget.setFixedWidth(100)
        # layout = QHBoxLayout()
        # layout.setContentsMargins(0,0,0,0)
        #
        # rule_text = QLabel(rule_str)
        # rule_text.setWordWrap(True)
        # font = QFont()
        # font.setPixelSize(16)
        # rule_text.setFont(font)
        #
        # del_button = QPushButton()
        # del_button.setText("删除")
        #
        # layout.addWidget(rule_text)
        # layout.addWidget(del_button)
        # # layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        #
        # self.setLayout(layout)

        self.horizontalLayout_2 = QHBoxLayout(main_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QWidget(main_widget)
        self.widget.setObjectName("widget")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName("label")
        self.label.setStyleSheet(
            "image: url(:/images/images/ava.jpg);\n" "border-radius: 15px;"
        )

        self.verticalLayout.addWidget(self.label)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout.addWidget(self.widget)

        self.nickname = QLabel(main_widget)
        self.nickname.setObjectName("nickname")
        sizePolicy.setHeightForWidth(self.nickname.sizePolicy().hasHeightForWidth())
        self.nickname.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.nickname, 0, Qt.AlignmentFlag.AlignHCenter)

        self.score = QLabel(main_widget)
        self.score.setObjectName("score")
        sizePolicy.setHeightForWidth(self.score.sizePolicy().hasHeightForWidth())
        self.score.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.score, 0, Qt.AlignmentFlag.AlignHCenter)

        self.has_prompt = QCheckBox(main_widget)
        self.has_prompt.setObjectName("has_prompt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.has_prompt.sizePolicy().hasHeightForWidth())
        self.has_prompt.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(
            self.has_prompt, 0, Qt.AlignmentFlag.AlignHCenter
        )

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        # self.retranslateUi(main_widget)
        #
        # QMetaObject.connectSlotsByName(main_widget)

    # setupUi

    # def retranslateUi(self, Form):
    #     Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
    #     self.label.setText("")
    #     self.nickname.setText(QCoreApplication.translate("Form", "\u963f\u667a", None))
    #     self.score.setText(QCoreApplication.translate("Form", "1", None))
    #     self.has_prompt.setText("")
