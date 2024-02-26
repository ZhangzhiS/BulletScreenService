from typing import Optional

from PySide6.QtCore import QMetaObject, QSize, QThreadPool, Qt, Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QWidget,
)

from dmplay.utils.download_thread import DownloadThread

t = "http://p3-webcast.douyinpic.com/img/webcast/mystery_man_thumb_avatar.png~tplv-obj.image"


class RankItem(QWidget):
    def __init__(
        self,
        nickname: str,
        score: int,
        prompt: Optional[str],
        thread_pool: QThreadPool,
        avatar_url: Optional[str] = None,
        parent: Optional[QWidget] = None,
    ) -> None:
        super().__init__(parent)
        self.horizontalLayout_2 = QHBoxLayout(self)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QWidget(self)
        self.widget.setObjectName("widget")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(40, 40))
        self.widget.setMaximumSize(QSize(40, 40))
        self.horizontalLayout_10 = QHBoxLayout(self.widget)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.avatar = QLabel(self.widget)
        self.avatar.setObjectName("avatar")
        # self.avatar.setMinimumSize(QSize(40, 40))
        # self.avatar.setStyleSheet("image: url(:/images/images/ava.jpg);")
        render_avatar = DownloadThread(
            avatar_url if avatar_url is not None else t, status=-1, name=""
        )
        render_avatar.signal.finished.connect(self.set_avatar)
        thread_pool.start(render_avatar)

        self.horizontalLayout_9.addWidget(self.avatar)

        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)

        self.horizontalLayout.addWidget(self.widget)

        self.widget_3 = QWidget(self)
        self.widget_3.setObjectName("widget_3")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.nickname = QLabel(self.widget_3)
        self.nickname.setObjectName("nickname")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.nickname.sizePolicy().hasHeightForWidth())
        self.nickname.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.nickname, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self)
        self.widget_4.setObjectName("widget_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy3)
        self.widget_4.setMinimumSize(QSize(56, 56))
        self.widget_4.setMaximumSize(QSize(56, 56))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.score = QLabel(self.widget_4)
        self.score.setObjectName("score")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.score.sizePolicy().hasHeightForWidth())
        self.score.setSizePolicy(sizePolicy4)
        self.score.setMinimumSize(QSize(30, 0))
        self.score.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_5.addWidget(self.score, 0, Qt.AlignmentFlag.AlignRight)

        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout.addWidget(self.widget_4)

        self.widget_2 = QWidget(self)
        self.widget_2.setObjectName("widget_2")
        sizePolicy5 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy5)
        self.widget_2.setMinimumSize(QSize(50, 50))
        self.widget_2.setMaximumSize(QSize(50, 50))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.has_prompt = QCheckBox(self.widget_2)
        self.has_prompt.setObjectName("has_prompt")

        self.horizontalLayout_7.addWidget(
            self.has_prompt, 0, Qt.AlignmentFlag.AlignRight
        )

        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalLayout.addWidget(self.widget_2)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        QMetaObject.connectSlotsByName(self)

        self.nickname.setText(nickname)
        self.score.setText(str(score))
        self.has_prompt.setText("")
        if prompt:
            self.has_prompt.setChecked(True)

    @Slot(bytes)
    def set_avatar(self, content):
        image = QPixmap()
        image.loadFromData(content)
        image.scaled(
            QSize(30, 30),
            # Qt.AspectRatioMode.KeepAspectRatio,
        )
        self.avatar.setScaledContents(True)
        self.avatar.setPixmap(image)
        self.avatar.setAlignment(Qt.AlignmentFlag.AlignCenter)
