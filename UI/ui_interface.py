# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceOhdFFO.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
import Icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(773, 511)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"@font-face{\n"
"			font-family: NovaFlat;\n"
"			src: url(:/fonts/Nova_Flat/NovaFlat-Regular.ttf) format(\"truetype\");\n"
"}\n"
"*{\n"
"color: #fff;\n"
"font-family: NovaFlat;\n"
"font-size: 12px;\n"
"border: nine;\n"
"background: none;\n"
"}\n"
"\n"
"QWidget{\n"
"	background-color: rgb(45, 46, 76);\n"
"}\n"
"\n"
"left_menu_widget, #percentage_bar_chart, #nested_donuts, \n"
"#line_charts, #bar_charts, #temperature_bar_chart, #stackedWidget QFrame\n"
"{\n"
"background-color: rgb(50, 68, 85);\n"
"}\n"
"#frame_2, #frame_9{\n"
"	background-color: rgb(33, 35, 49);\n"
"}\n"
"\n"
"#frame_4 QPushButton{\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"background-color: rgba(33, 42, 51, 100);\n"
"}\n"
"#header_nav QPushButton{\n"
"background-color: rgb(54, 66, 147);\n"
"border-radius: 15px;\n"
"\n"
"}\n"
"#header_nav QPushButton:hover{\n"
"background-color: rgb(120, 157, 186);\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_widget = QWidget(self.centralwidget)
        self.left_menu_widget.setObjectName(u"left_menu_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_menu_widget.sizePolicy().hasHeightForWidth())
        self.left_menu_widget.setSizePolicy(sizePolicy)
        self.left_menu_widget.setMinimumSize(QSize(0, 0))
        self.left_menu_widget.setMaximumSize(QSize(16777215, 11677215))
        self.left_menu_widget.setStyleSheet(u"#left_menu_widget{\n"
"background-color: rgb(50, 68, 85);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.left_menu_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.left_menu_widget)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setMinimumSize(QSize(0, 52))
        self.frame_6.setMaximumSize(QSize(16777215, 41))
        self.frame_6.setStyleSheet(u"#frame_6, #label, #label_15{\n"
"background-color: rgb(54, 66, 147);\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 0, 0, 0)
        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)
        self.label_15.setMinimumSize(QSize(36, 36))
        self.label_15.setMaximumSize(QSize(36, 36))
        self.label_15.setPixmap(QPixmap(u":/Buttons/analysis.png"))
        self.label_15.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_15)

        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.left_menu_widget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QSize(0, 306))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setStyleSheet(u"#frame_3{\n"
"background-color: rgb(50, 68, 85);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.percent_bar_chart_button = QPushButton(self.frame_3)
        self.percent_bar_chart_button.setObjectName(u"percent_bar_chart_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.percent_bar_chart_button.sizePolicy().hasHeightForWidth())
        self.percent_bar_chart_button.setSizePolicy(sizePolicy2)
        self.percent_bar_chart_button.setMaximumSize(QSize(200, 33))
        self.percent_bar_chart_button.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/Buttons/analytics.png", QSize(), QIcon.Normal, QIcon.Off)
        self.percent_bar_chart_button.setIcon(icon)
        self.percent_bar_chart_button.setIconSize(QSize(23, 23))

        self.verticalLayout_2.addWidget(self.percent_bar_chart_button)

        self.temperature_chart_button = QPushButton(self.frame_3)
        self.temperature_chart_button.setObjectName(u"temperature_chart_button")
        sizePolicy2.setHeightForWidth(self.temperature_chart_button.sizePolicy().hasHeightForWidth())
        self.temperature_chart_button.setSizePolicy(sizePolicy2)
        self.temperature_chart_button.setMaximumSize(QSize(16777215, 33))
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/hot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.temperature_chart_button.setIcon(icon1)
        self.temperature_chart_button.setIconSize(QSize(23, 23))

        self.verticalLayout_2.addWidget(self.temperature_chart_button)

        self.nested_donuts_button = QPushButton(self.frame_3)
        self.nested_donuts_button.setObjectName(u"nested_donuts_button")
        sizePolicy2.setHeightForWidth(self.nested_donuts_button.sizePolicy().hasHeightForWidth())
        self.nested_donuts_button.setSizePolicy(sizePolicy2)
        self.nested_donuts_button.setMaximumSize(QSize(16777215, 33))
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/pie-chart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nested_donuts_button.setIcon(icon2)
        self.nested_donuts_button.setIconSize(QSize(23, 23))

        self.verticalLayout_2.addWidget(self.nested_donuts_button)

        self.line_chart_button = QPushButton(self.frame_3)
        self.line_chart_button.setObjectName(u"line_chart_button")
        sizePolicy2.setHeightForWidth(self.line_chart_button.sizePolicy().hasHeightForWidth())
        self.line_chart_button.setSizePolicy(sizePolicy2)
        self.line_chart_button.setMaximumSize(QSize(16777215, 33))
        icon3 = QIcon()
        icon3.addFile(u":/Buttons/line-chart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.line_chart_button.setIcon(icon3)
        self.line_chart_button.setIconSize(QSize(23, 23))

        self.verticalLayout_2.addWidget(self.line_chart_button)

        self.bar_chart_button = QPushButton(self.frame_3)
        self.bar_chart_button.setObjectName(u"bar_chart_button")
        sizePolicy2.setHeightForWidth(self.bar_chart_button.sizePolicy().hasHeightForWidth())
        self.bar_chart_button.setSizePolicy(sizePolicy2)
        self.bar_chart_button.setMaximumSize(QSize(16777215, 33))
        icon4 = QIcon()
        icon4.addFile(u":/Buttons/analytics (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.bar_chart_button.setIcon(icon4)

        self.verticalLayout_2.addWidget(self.bar_chart_button)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.left_menu_widget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMaximumSize(QSize(16777215, 54))
        self.frame_4.setStyleSheet(u"#frame_4, #label_16, #label_2{\n"
"	background-color: rgb(54, 66, 147);\n"
"}\n"
"\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(6, 0, 6, 0)
        self.label_16 = QLabel(self.frame_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(26, 29))
        self.label_16.setPixmap(QPixmap(u":/Buttons/python-logo-only.png"))
        self.label_16.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_16)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QSize(265, 25))

        self.horizontalLayout_8.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.left_menu_widget)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setStyleSheet(u"#frame_5, QLabel{\n"
"background-color: rgb(50, 68, 85);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 4, -1, -1)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.label_6)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.label_5)


        self.verticalLayout.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.left_menu_widget)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 16777214))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 1, -1, -1)
        self.header_frame = QFrame(self.frame_2)
        self.header_frame.setObjectName(u"header_frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy4)
        self.header_frame.setMinimumSize(QSize(566, 0))
        self.header_frame.setMaximumSize(QSize(16777215, 232))
        self.header_frame.setStyleSheet(u"#frame_7{\n"
"background-color: rgb(54, 66, 147);\n"
"}")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.header_menu_nav = QFrame(self.header_frame)
        self.header_menu_nav.setObjectName(u"header_menu_nav")
        self.header_menu_nav.setMinimumSize(QSize(109, 0))
        self.header_menu_nav.setMaximumSize(QSize(152, 249))
        self.header_menu_nav.setStyleSheet(u"#header_menu_nav, QPushButton{\n"
"background-color: rgb(54, 66, 147);\n"
"}")
        self.header_menu_nav.setFrameShape(QFrame.StyledPanel)
        self.header_menu_nav.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_menu_nav)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menu_button = QPushButton(self.header_menu_nav)
        self.menu_button.setObjectName(u"menu_button")
        sizePolicy.setHeightForWidth(self.menu_button.sizePolicy().hasHeightForWidth())
        self.menu_button.setSizePolicy(sizePolicy)
        self.menu_button.setMaximumSize(QSize(28, 127))
        self.menu_button.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/Buttons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_button.setIcon(icon5)
        self.menu_button.setIconSize(QSize(46, 21))

        self.horizontalLayout_4.addWidget(self.menu_button)

        self.label_7 = QLabel(self.header_menu_nav)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(96, 0))
        self.label_7.setMaximumSize(QSize(113, 16777215))
        self.label_7.setStyleSheet(u"#label_7{\n"
"background-color: rgb(54, 66, 147);\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_7)


        self.horizontalLayout_3.addWidget(self.header_menu_nav)

        self.title_bar = QFrame(self.header_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setStyleSheet(u"#title_bar{\n"
"background-color: rgb(54, 66, 147);\n"
"}")
        self.title_bar.setFrameShape(QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.title_bar)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.title_bar)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"#label_8{\n"
"background-color: rgb(54, 66, 147);\n"
"}")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_8)


        self.horizontalLayout_3.addWidget(self.title_bar)

        self.header_nav = QFrame(self.header_frame)
        self.header_nav.setObjectName(u"header_nav")
        sizePolicy1.setHeightForWidth(self.header_nav.sizePolicy().hasHeightForWidth())
        self.header_nav.setSizePolicy(sizePolicy1)
        self.header_nav.setMinimumSize(QSize(106, 0))
        self.header_nav.setMaximumSize(QSize(148, 16777215))
        self.header_nav.setStyleSheet(u"#header_nav{\n"
"background-color: rgb(54, 66, 147);\n"
"}")
        self.header_nav.setFrameShape(QFrame.StyledPanel)
        self.header_nav.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.header_nav)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.minimize_window_button = QPushButton(self.header_nav)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        self.minimize_window_button.setMinimumSize(QSize(30, 30))
        self.minimize_window_button.setMaximumSize(QSize(30, 30))
        self.minimize_window_button.setStyleSheet(u"#pushButton8{\n"
"background-color: rgb(54, 66, 147);\n"
"	border-color: rgb(97, 165, 255);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/Buttons/minus-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon6)
        self.minimize_window_button.setIconSize(QSize(23, 23))

        self.horizontalLayout_6.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.header_nav)
        self.restore_window_button.setObjectName(u"restore_window_button")
        self.restore_window_button.setMaximumSize(QSize(30, 30))
        icon7 = QIcon()
        icon7.addFile(u":/Buttons/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon7)
        self.restore_window_button.setIconSize(QSize(23, 23))

        self.horizontalLayout_6.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.header_nav)
        self.close_window_button.setObjectName(u"close_window_button")
        self.close_window_button.setMaximumSize(QSize(30, 30))
        icon8 = QIcon()
        icon8.addFile(u":/Buttons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon8)
        self.close_window_button.setIconSize(QSize(29, 29))

        self.horizontalLayout_6.addWidget(self.close_window_button)


        self.horizontalLayout_3.addWidget(self.header_nav)


        self.verticalLayout_4.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setMaximumSize(QSize(16777215, 16777215))
        self.frame_8.setStyleSheet(u"#frame_8{\n"
"background-color: rgb(50, 68, 85);\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.stackedWidget = QStackedWidget(self.frame_8)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.percentage_bar_chart = QWidget()
        self.percentage_bar_chart.setObjectName(u"percentage_bar_chart")
        self.verticalLayout_6 = QVBoxLayout(self.percentage_bar_chart)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_16 = QFrame(self.percentage_bar_chart)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.frame_16)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setLayoutDirection(Qt.LeftToRight)
        self.label_10.setAutoFillBackground(False)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_10, 0, Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.percentage_bar_chart)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_17)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_18, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_17)

        self.stackedWidget.addWidget(self.percentage_bar_chart)
        self.temperature_bar_chart = QWidget()
        self.temperature_bar_chart.setObjectName(u"temperature_bar_chart")
        self.verticalLayout_7 = QVBoxLayout(self.temperature_bar_chart)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_19 = QFrame(self.temperature_bar_chart)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.frame_19)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_11, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.frame_19, 0, Qt.AlignTop)

        self.frame_20 = QFrame(self.temperature_bar_chart)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_20)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_21, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_20)

        self.stackedWidget.addWidget(self.temperature_bar_chart)
        self.nested_donuts = QWidget()
        self.nested_donuts.setObjectName(u"nested_donuts")
        self.verticalLayout_8 = QVBoxLayout(self.nested_donuts)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_22 = QFrame(self.nested_donuts)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_12 = QLabel(self.frame_22)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_12, 0, Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.frame_22, 0, Qt.AlignTop)

        self.frame_23 = QFrame(self.nested_donuts)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_23)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_24, 0, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_23)

        self.stackedWidget.addWidget(self.nested_donuts)
        self.line_charts = QWidget()
        self.line_charts.setObjectName(u"line_charts")
        self.line_charts.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.line_charts)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_25 = QFrame(self.line_charts)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_13 = QLabel(self.frame_25)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_13, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.frame_25, 0, Qt.AlignTop)

        self.frame_26 = QFrame(self.line_charts)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy)
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.frame_26)

        self.stackedWidget.addWidget(self.line_charts)
        self.bar_charts = QWidget()
        self.bar_charts.setObjectName(u"bar_charts")
        self.verticalLayout_10 = QVBoxLayout(self.bar_charts)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_28 = QFrame(self.bar_charts)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"#frame_28{\n"
"background-color: rgb(50, 68, 85);\n"
"}")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_28)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_14 = QLabel(self.frame_28)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"#label_14{\n"
"background-color: rgb(50, 68, 85);\n"
"}")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_14, 0, Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.frame_28, 0, Qt.AlignTop)

        self.frame_27 = QFrame(self.bar_charts)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy)
        self.frame_27.setStyleSheet(u"#frame_27{\n"
"background-color: rgb(50, 68, 85);\n"
"}")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_27)

        self.stackedWidget.addWidget(self.bar_charts)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 0))
        self.frame_9.setMaximumSize(QSize(16777215, 200))
        self.frame_9.setStyleSheet(u"#frame_13{\n"
"background-color: rgb(50, 68, 85);\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 9, -1, 4)
        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"#frame_13{\n"
"	background-color: rgb(33, 35, 49);\n"
"\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.frame_13)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"#label_9{\n"
"	background-color: rgb(33, 35, 49);\n"
"}")

        self.horizontalLayout_9.addWidget(self.label_9)


        self.horizontalLayout_7.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"#frame_14{\n"
"	background-color: rgb(33, 35, 49);\n"
"}")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame_14)


        self.verticalLayout_4.addWidget(self.frame_9)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_15.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"  CHART DATA", None))
        self.percent_bar_chart_button.setText(QCoreApplication.translate("MainWindow", u"  Percentage Bar Chart", None))
        self.temperature_chart_button.setText(QCoreApplication.translate("MainWindow", u"  Temperature Chart", None))
        self.nested_donuts_button.setText(QCoreApplication.translate("MainWindow", u"  Nested Donuts", None))
        self.line_chart_button.setText(QCoreApplication.translate("MainWindow", u"   Line Charts", None))
        self.bar_chart_button.setText(QCoreApplication.translate("MainWindow", u"   Bar Charts", None))
        self.label_16.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"  Engineering 1100 Final Project", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Jacob Sprouse", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"James Allison", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Francis Collopy", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Huayadian Sun", None))
        self.menu_button.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Percentage Bar Chart", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Temperature Bar Chart", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Nested Donut Chart", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Line Charts", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Bar Chart", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Auburn University", None))
    # retranslateUi

