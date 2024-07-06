# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'indexLatest.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCalendarWidget, QComboBox,
    QDateEdit, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1271, 888)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(13, 11, 1251, 862))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.widget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(71, 860))
        self.icon_only_widget.setMaximumSize(QSize(71, 860))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(14, 13, 106);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton{\n"
"	border: none;\n"
"	height: 30px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #52452a;\n"
"	border-radius: 3px;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(17, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.icon_only_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setPixmap(QPixmap(u":/Icons/school (6).png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(17, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 30, -1, -1)
        self.home_1 = QPushButton(self.icon_only_widget)
        self.home_1.setObjectName(u"home_1")
        icon = QIcon()
        icon.addFile(u":/Icons/home (6).png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/Icons/home (3).png", QSize(), QIcon.Normal, QIcon.On)
        self.home_1.setIcon(icon)
        self.home_1.setIconSize(QSize(20, 16))
        self.home_1.setCheckable(True)
        self.home_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.home_1)

        self.students_1 = QPushButton(self.icon_only_widget)
        self.students_1.setObjectName(u"students_1")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/education (6).png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/Icons/education (3).png", QSize(), QIcon.Normal, QIcon.On)
        self.students_1.setIcon(icon1)
        self.students_1.setIconSize(QSize(20, 20))
        self.students_1.setCheckable(True)
        self.students_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.students_1)

        self.classMonitoring_1 = QPushButton(self.icon_only_widget)
        self.classMonitoring_1.setObjectName(u"classMonitoring_1")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/classroom (6).png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/Icons/classroom (3).png", QSize(), QIcon.Normal, QIcon.On)
        self.classMonitoring_1.setIcon(icon2)
        self.classMonitoring_1.setIconSize(QSize(20, 20))
        self.classMonitoring_1.setCheckable(True)
        self.classMonitoring_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.classMonitoring_1)

        self.attendance_monitoring_1 = QPushButton(self.icon_only_widget)
        self.attendance_monitoring_1.setObjectName(u"attendance_monitoring_1")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/pen (1).png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/Icons/pen (2).png", QSize(), QIcon.Normal, QIcon.On)
        self.attendance_monitoring_1.setIcon(icon3)
        self.attendance_monitoring_1.setIconSize(QSize(20, 20))
        self.attendance_monitoring_1.setCheckable(True)
        self.attendance_monitoring_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.attendance_monitoring_1)

        self.attendance_1 = QPushButton(self.icon_only_widget)
        self.attendance_1.setObjectName(u"attendance_1")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/calendar (6).png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/Icons/calendar (3).png", QSize(), QIcon.Normal, QIcon.On)
        self.attendance_1.setIcon(icon4)
        self.attendance_1.setIconSize(QSize(18, 18))
        self.attendance_1.setCheckable(True)
        self.attendance_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.attendance_1)

        self.reports_1 = QPushButton(self.icon_only_widget)
        self.reports_1.setObjectName(u"reports_1")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/report (6).png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/Icons/report (3).png", QSize(), QIcon.Normal, QIcon.On)
        self.reports_1.setIcon(icon5)
        self.reports_1.setIconSize(QSize(20, 20))
        self.reports_1.setCheckable(True)
        self.reports_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.reports_1)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 463, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_text_widget = QWidget(self.widget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setMinimumSize(QSize(0, 860))
        self.icon_text_widget.setMaximumSize(QSize(16777215, 860))
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(14, 13, 106);\n"
"	color: #bbbbbc;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	height: 30px;\n"
"	border: none;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.icon_text_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/Icons/school (6).png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_text_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(15)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 30, -1, -1)
        self.home_2 = QPushButton(self.icon_text_widget)
        self.home_2.setObjectName(u"home_2")
        font1 = QFont()
        font1.setBold(True)
        self.home_2.setFont(font1)
        self.home_2.setStyleSheet(u"QPushButton{\n"
"	padding-left: -70px;\n"
"	font-weight: bold;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #52452a;\n"
"	border-radius: 3px;\n"
"	color: #fec701;\n"
"	font-weight: bold;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/home (6).png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/Icons/home (3).png", QSize(), QIcon.Active, QIcon.On)
        self.home_2.setIcon(icon6)
        self.home_2.setIconSize(QSize(20, 16))
        self.home_2.setCheckable(True)
        self.home_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_2)

        self.students_2 = QPushButton(self.icon_text_widget)
        self.students_2.setObjectName(u"students_2")
        self.students_2.setFont(font1)
        self.students_2.setStyleSheet(u"QPushButton{\n"
"	padding-left: -55px;\n"
"	font-weight: bold\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #52452a;\n"
"	border-radius: 3px;\n"
"	color: #fec701;\n"
"	font: bold;\n"
"	/*font-color: #fec701;*/\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/education (6).png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/Icons/education (3).png", QSize(), QIcon.Normal, QIcon.On)
        icon7.addFile(u":/Icons/education (3).png", QSize(), QIcon.Active, QIcon.On)
        self.students_2.setIcon(icon7)
        self.students_2.setIconSize(QSize(20, 20))
        self.students_2.setCheckable(True)
        self.students_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.students_2)

        self.classMonitoring_2 = QPushButton(self.icon_text_widget)
        self.classMonitoring_2.setObjectName(u"classMonitoring_2")
        self.classMonitoring_2.setFont(font1)
        self.classMonitoring_2.setStyleSheet(u"QPushButton{\n"
"	padding-left: -10px;\n"
"	font-weight: bold\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #52452a;\n"
"	border-radius: 3px;\n"
"	color: #fec701;\n"
"	font: bold;\n"
"}")
        self.classMonitoring_2.setIcon(icon2)
        self.classMonitoring_2.setIconSize(QSize(20, 20))
        self.classMonitoring_2.setCheckable(True)
        self.classMonitoring_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.classMonitoring_2)

        self.attendance_monitoring_2 = QPushButton(self.icon_text_widget)
        self.attendance_monitoring_2.setObjectName(u"attendance_monitoring_2")
        self.attendance_monitoring_2.setStyleSheet(u"QPushButton{\n"
"	padding-left: 20px;\n"
"	font-weight: bold\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #52452a;\n"
"	border-radius: 3px;\n"
"	color: #fec701;\n"
"	font: bold;\n"
"}")
        self.attendance_monitoring_2.setIcon(icon3)
        self.attendance_monitoring_2.setIconSize(QSize(20, 20))
        self.attendance_monitoring_2.setCheckable(True)
        self.attendance_monitoring_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.attendance_monitoring_2)

        self.attendance_2 = QPushButton(self.icon_text_widget)
        self.attendance_2.setObjectName(u"attendance_2")
        self.attendance_2.setFont(font1)
        self.attendance_2.setStyleSheet(u"QPushButton{\n"
"	padding-left: 5px;\n"
"	font-weight: bold\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #52452a;\n"
"	border-radius: 3px;\n"
"	color: #fec701;\n"
"	font: bold;\n"
"}")
        self.attendance_2.setIcon(icon4)
        self.attendance_2.setIconSize(QSize(18, 18))
        self.attendance_2.setCheckable(True)
        self.attendance_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.attendance_2)

        self.reports_2 = QPushButton(self.icon_text_widget)
        self.reports_2.setObjectName(u"reports_2")
        self.reports_2.setFont(font1)
        self.reports_2.setStyleSheet(u"QPushButton{\n"
"	padding-left: -20px;\n"
"	font-weight: bold\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #52452a;\n"
"	border-radius: 3px;\n"
"	color: #fec701;\n"
"	font: bold;\n"
"	/*font-color: #fec701;*/\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/Icons/report (6).png", QSize(), QIcon.Normal, QIcon.Off)
        icon8.addFile(u":/Icons/report (3).png", QSize(), QIcon.Normal, QIcon.On)
        icon8.addFile(u":/Icons/report (3).png", QSize(), QIcon.Active, QIcon.On)
        self.reports_2.setIcon(icon8)
        self.reports_2.setIconSize(QSize(20, 20))
        self.reports_2.setCheckable(True)
        self.reports_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.reports_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(17, 599, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.icon_text_widget, 0, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.header_widget = QWidget(self.widget)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setMinimumSize(QSize(841, 71))
        self.header_widget.setMaximumSize(QSize(16777215, 16777215))
        self.header_widget.setStyleSheet(u"background-color: rgb(14, 13, 106);\n"
"border-radius: 15px;")
        self.horizontalLayout_6 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_3 = QPushButton(self.header_widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"border:none;")
        icon9 = QIcon()
        icon9.addFile(u":/Icons/burger-bar (6).png", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u":/Icons/burger-bar (3).png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_3.setIcon(icon9)
        self.pushButton_3.setIconSize(QSize(29, 35))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setAutoExclusive(False)

        self.horizontalLayout_6.addWidget(self.pushButton_3)

        self.horizontalSpacer_4 = QSpacerItem(386, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, 25, -1)
        self.lineEdit_2 = QLineEdit(self.header_widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 31))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 31))
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"	padding-left:15px;\n"
"	border: 1px solid #bbbbbc;\n"
"	border-radius: 15px;\n"
"	color: #ffffff;\n"
"	/*background-color: rgb(187, 187, 188);*/\n"
"}")

        self.horizontalLayout_7.addWidget(self.lineEdit_2)

        self.pushButton_4 = QPushButton(self.header_widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"border: none;\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/Icons/magnifying-glass (3).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon10)
        self.pushButton_4.setIconSize(QSize(25, 25))
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setAutoExclusive(False)

        self.horizontalLayout_7.addWidget(self.pushButton_4)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)


        self.verticalLayout_3.addWidget(self.header_widget)

        self.main_sceen_widget = QWidget(self.widget)
        self.main_sceen_widget.setObjectName(u"main_sceen_widget")
        self.main_sceen_widget.setEnabled(True)
        self.main_sceen_widget.setMinimumSize(QSize(841, 780))
        self.main_sceen_widget.setMaximumSize(QSize(16777215, 780))
        font2 = QFont()
        font2.setFamilies([u"Sans Serif Collection"])
        self.main_sceen_widget.setFont(font2)
        self.main_sceen_widget.setStyleSheet(u"background-color: #ffffff;\n"
"border-radius: 15px;")
        self.stackedWidget = QStackedWidget(self.main_sceen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 941, 751))
        self.stackedWidget.setMinimumSize(QSize(0, 751))
        self.stackedWidget.setMaximumSize(QSize(16777215, 751))
        font3 = QFont()
        font3.setPointSize(11)
        self.stackedWidget.setFont(font3)
        self.stackedWidget.setStyleSheet(u"/*background-color: rgb(236, 236, 236);*/\n"
"/*background-color: rgb(236, 236, 236);*/\n"
"color: white;")
        self.stackedWidget.setFrameShape(QFrame.StyledPanel)
        self.page_0 = QWidget()
        self.page_0.setObjectName(u"page_0")
        self.page_0.setStyleSheet(u"/*background-color: #f5f5f5;*/\n"
"background-color: rgb(255, 255, 255);")
        self.label_8 = QLabel(self.page_0)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(60, 10, 91, 51))
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(True)
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"color: rgb(14, 13, 106);")
        self.label_24 = QLabel(self.page_0)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(20, 20, 31, 31))
        self.label_24.setPixmap(QPixmap(u":/Icons/home (1).png"))
        self.label_24.setScaledContents(True)
        self.widget1 = QWidget(self.page_0)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 90, 921, 261))
        self.horizontalLayout_3 = QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.widget1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(212, 212, 212);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_16 = QLabel(self.frame_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 40, 251, 211))
        self.label_16.setStyleSheet(u"")
        self.label_16.setPixmap(QPixmap(u":/Icons/Untitled design5.png"))
        self.label_16.setScaledContents(True)
        self.label_17 = QLabel(self.frame_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(60, 10, 221, 21))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.label_17.setFont(font5)
        self.label_17.setStyleSheet(u"color: rgb(82, 69, 42);")
        self.label_21 = QLabel(self.frame_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(20, 0, 31, 31))
        self.label_21.setPixmap(QPixmap(u":/Icons/bar-chart.png"))
        self.label_21.setScaledContents(True)
        self.label_17.raise_()
        self.label_16.raise_()
        self.label_21.raise_()

        self.horizontalLayout_3.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.widget1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"/*background-color: rgb(212, 212, 212);*/ \n"
"background-color: rgb(14, 13, 106);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 10, 221, 31))
        self.label_9.setFont(font5)
        self.label_9.setStyleSheet(u"/*color: rgb(82, 69, 42);*/\n"
"color: white;\n"
"")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 40, 251, 201))
        self.label_5.setStyleSheet(u"")
        self.label_5.setPixmap(QPixmap(u":/Icons/Untitled design7.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.frame_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_3 = QFrame(self.widget1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"/*background-color: rgb(212, 212, 212);*/\n"
"background-color: rgb(14, 13, 106);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.frame_3.setLineWidth(1)
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(110, 0, 141, 33))
        font6 = QFont()
        font6.setPointSize(15)
        font6.setBold(True)
        self.label_12.setFont(font6)
        self.label_12.setStyleSheet(u"/*color: rgb(14, 13, 106);*/\n"
"color: white;")
        self.label_12.setFrameShadow(QFrame.Plain)
        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 20, 81, 81))
        self.label_14.setFont(font4)
        self.label_14.setStyleSheet(u"")
        self.label_14.setPixmap(QPixmap(u":/Icons/report (3).png"))
        self.label_14.setScaledContents(True)
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(140, 40, 91, 71))
        self.label_15.setMinimumSize(QSize(0, 0))
        self.label_15.setMaximumSize(QSize(100, 100))
        font7 = QFont()
        font7.setPointSize(25)
        font7.setBold(True)
        self.label_15.setFont(font7)
        self.label_15.setLayoutDirection(Qt.LeftToRight)
        self.label_15.setStyleSheet(u"color:#fe4f51;\n"
"background-color: #8ba9d0;")
        self.label_15.setLineWidth(1)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.widget1)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(212, 212, 212);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.frame_5.setLineWidth(1)
        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(160, 0, 51, 33))
        self.label_18.setFont(font6)
        self.label_18.setStyleSheet(u"color: rgb(14, 13, 106);")
        self.label_18.setFrameShadow(QFrame.Plain)
        self.label_19 = QLabel(self.frame_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 20, 81, 91))
        self.label_19.setFont(font4)
        self.label_19.setStyleSheet(u"")
        self.label_19.setPixmap(QPixmap(u":/Icons/multiple-users-silhouette.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_20 = QLabel(self.frame_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(140, 40, 91, 71))
        self.label_20.setMinimumSize(QSize(0, 0))
        self.label_20.setMaximumSize(QSize(100, 100))
        self.label_20.setFont(font7)
        self.label_20.setLayoutDirection(Qt.LeftToRight)
        self.label_20.setStyleSheet(u"color:#fe4f51;\n"
"background-color: #8ba9d0;")
        self.label_20.setLineWidth(1)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.frame_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.widget2 = QWidget(self.page_0)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 380, 921, 311))
        self.horizontalLayout_8 = QHBoxLayout(self.widget2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.widget2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"/*background-color: rgb(212, 212, 212);*/\n"
"background-color: rgb(14, 13, 106);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_22 = QLabel(self.frame_6)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(20, 40, 421, 251))
        self.label_22.setStyleSheet(u"")
        self.label_22.setPixmap(QPixmap(u":/Icons/Untitled design6.png"))
        self.label_22.setScaledContents(True)
        self.label_23 = QLabel(self.frame_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(90, 0, 261, 33))
        self.label_23.setFont(font5)
        self.label_23.setStyleSheet(u"/*color: rgb(14, 13, 106);*/\n"
"color: white;")
        self.label_23.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_8.addWidget(self.frame_6)

        self.frame = QFrame(self.widget2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(14, 13, 106);\n"
"/*background-color: rgb(212, 212, 212);*/\n"
"/*background-color: rgb(233, 233, 233);*/")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.calendarWidget = QCalendarWidget(self.frame)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(20, 50, 421, 241))
        self.calendarWidget.setStyleSheet(u"background-color: #8ba9d0;\n"
"")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 10, 31, 31))
        self.label.setPixmap(QPixmap(u":/Icons/event.png"))
        self.label.setScaledContents(True)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(180, 15, 141, 21))
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"/*color: rgb(82, 69, 42);*/\n"
"color: white;")

        self.horizontalLayout_8.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_0)
        self.frame_2.raise_()
        self.frame.raise_()
        self.frame_3.raise_()
        self.frame_5.raise_()
        self.frame_6.raise_()
        self.label_8.raise_()
        self.label_24.raise_()
        self.frame_4.raise_()
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.label_7 = QLabel(self.page_1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 10, 311, 51))
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"color: rgb(14, 13, 106);")
        self.studentInfo_table = QTableWidget(self.page_1)
        if (self.studentInfo_table.columnCount() < 9):
            self.studentInfo_table.setColumnCount(9)
        font8 = QFont()
        font8.setFamilies([u"MS Shell Dlg 2"])
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font8);
        self.studentInfo_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        if (self.studentInfo_table.rowCount() < 6):
            self.studentInfo_table.setRowCount(6)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.studentInfo_table.setVerticalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.studentInfo_table.setVerticalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.studentInfo_table.setVerticalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.studentInfo_table.setVerticalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.studentInfo_table.setVerticalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.studentInfo_table.setVerticalHeaderItem(5, __qtablewidgetitem14)
        self.studentInfo_table.setObjectName(u"studentInfo_table")
        self.studentInfo_table.setGeometry(QRect(-10, 140, 821, 291))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studentInfo_table.sizePolicy().hasHeightForWidth())
        self.studentInfo_table.setSizePolicy(sizePolicy)
        self.studentInfo_table.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: #0e0d6a;\n"
"	color: white;\n"
"	border-radius:2px;\n"
"\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #bdbdbd;\n"
"	background-color: #ececec;\n"
"	border-radius:2px;\n"
"	margin: auto;\n"
"   color: #0e0d6a;"
"	\n"
"/*width: 821 px;\n"
"height: 661 px;*/\n"
"}")
        self.studentInfo_table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.studentInfo_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.studentInfo_table.setAlternatingRowColors(True)
        self.studentInfo_table.horizontalHeader().setDefaultSectionSize(81)
        self.label_25 = QLabel(self.page_1)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(30, 20, 31, 31))
        self.label_25.setPixmap(QPixmap(u":/Icons/education (1).png"))
        self.label_25.setScaledContents(True)
        self.layoutWidget = QWidget(self.page_1)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 90, 741, 51))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.addStudent_button = QPushButton(self.layoutWidget)
        self.addStudent_button.setObjectName(u"addStudent_button")
        self.addStudent_button.setMinimumSize(QSize(0, 35))
        self.addStudent_button.setMaximumSize(QSize(16777215, 35))
        self.addStudent_button.setStyleSheet(u"QPushButton{\n"
"	background-color: #af8501;\n"
"	color: #ffffff;\n"
"	border-radius: 5px;\n"
"	border: none;\n"
"	font-weight: bold;\n"
"	font-size: 12px;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/Icons/add-friend2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addStudent_button.setIcon(icon11)
        self.addStudent_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_5.addWidget(self.addStudent_button)

        self.select_gender = QComboBox(self.layoutWidget)
        self.select_gender.addItem("")
        self.select_gender.addItem("")
        self.select_gender.addItem("")
        self.select_gender.setObjectName(u"select_gender")
        self.select_gender.setMinimumSize(QSize(150, 35))
        self.select_gender.setMaximumSize(QSize(16777215, 35))
        self.select_gender.setStyleSheet(u"QComboBox{\n"
"	border: 1px solid #af8501;\n"
"	border-radius: 5px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background-color: #af8501;\n"
"	color: #ffffff; \n"
"	height: 30px;\n"
"	padding-left: 15px;\n"
"	font-weight: bold;\n"
"	font-size: 12px;\n"
"	/*selection-background-color: #0192ef;*/\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"	selection-background-color: #0192ef;\n"
"}")

        self.horizontalLayout_5.addWidget(self.select_gender)

        self.select_class = QComboBox(self.layoutWidget)
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.setObjectName(u"select_class")
        self.select_class.setMinimumSize(QSize(0, 35))
        self.select_class.setMaximumSize(QSize(16777215, 35))
        self.select_class.setStyleSheet(u"QComboBox{\n"
"	border: 1px solid #af8501;\n"
"	border-radius: 5px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background-color: #af8501;\n"
"	color: #ffffff; \n"
"	height: 30px;\n"
"	padding-left: 15px;\n"
"	font-weight: bold;\n"
"	font-size: 12px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"	selection-background-color: #0192ef;\n"
"}")

        self.horizontalLayout_5.addWidget(self.select_class)

        self.search_student = QLineEdit(self.layoutWidget)
        self.search_student.setObjectName(u"search_student")
        self.search_student.setMinimumSize(QSize(150, 35))
        self.search_student.setMaximumSize(QSize(16777215, 35))
        self.search_student.setStyleSheet(u"QLineEdit{\n"
"	padding-left:15px;\n"
"	border: 1px solid #0e0d6a;\n"
"	border-radius: 15px;\n"
"	/*background-color: rgb(187, 187, 188);*/\n"
"}")

        self.horizontalLayout_5.addWidget(self.search_student)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_10 = QLabel(self.page_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(340, 280, 331, 51))
        font9 = QFont()
        font9.setPointSize(25)
        self.label_10.setFont(font9)
        self.label_10.setStyleSheet(u"color: rgb(14, 13, 106);")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_28 = QLabel(self.page_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(260, 300, 441, 51))
        self.label_28.setFont(font9)
        self.label_28.setStyleSheet(u"color: rgb(14, 13, 106);")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_26 = QLabel(self.page_4)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(20, 20, 31, 31))
        self.label_26.setPixmap(QPixmap(u":/Icons/calendar (1).png"))
        self.label_26.setScaledContents(True)
        self.label_27 = QLabel(self.page_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(60, 10, 161, 51))
        self.label_27.setFont(font4)
        self.label_27.setStyleSheet(u"color: rgb(14, 13, 106);")
        self.studentInfo_table_2 = QTableWidget(self.page_4)
        if (self.studentInfo_table_2.columnCount() < 5):
            self.studentInfo_table_2.setColumnCount(5)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.studentInfo_table_2.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font8);
        self.studentInfo_table_2.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.studentInfo_table_2.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.studentInfo_table_2.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.studentInfo_table_2.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        if (self.studentInfo_table_2.rowCount() < 6):
            self.studentInfo_table_2.setRowCount(6)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        self.studentInfo_table_2.setVerticalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        self.studentInfo_table_2.setVerticalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        self.studentInfo_table_2.setVerticalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        self.studentInfo_table_2.setVerticalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        self.studentInfo_table_2.setVerticalHeaderItem(4, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        self.studentInfo_table_2.setVerticalHeaderItem(5, __qtablewidgetitem25)
        self.studentInfo_table_2.setObjectName(u"studentInfo_table_2")
        self.studentInfo_table_2.setGeometry(QRect(200, 180, 541, 281))
        sizePolicy.setHeightForWidth(self.studentInfo_table_2.sizePolicy().hasHeightForWidth())
        self.studentInfo_table_2.setSizePolicy(sizePolicy)
        self.studentInfo_table_2.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: #0e0d6a;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius:2px;\n"
"	text-align: center;\n"
"	padding: 3px 15px\n"
"}\n"
"\n"

"QTableWidget{\n"
"	alternate-background-color: #bdbdbd;\n"
"	border: none;\n"
"	background-color: #ececec;\n"
"	border-radius:2px;\n"
"	\n"
"   color: #0e0d6a;"
"/*width: 821 px;\n"
"height: 661 px;*/\n"
"}")
        self.studentInfo_table_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.studentInfo_table_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.studentInfo_table_2.setAlternatingRowColors(True)
        self.studentInfo_table_2.horizontalHeader().setDefaultSectionSize(100)
        self.dateEdit = QDateEdit(self.page_4)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(200, 100, 131, 41))
        self.dateEdit.setStyleSheet(u"QDateEdit{\n"
"	border: 1px solid #af8501;\n"
"	border-radius: 5px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background-color: #af8501;\n"
"	color: #ffffff; \n"
"	height: 30px;\n"
"	padding-left: 15px;\n"
"	font-weight: bold;\n"
"	font-size: 12px;\n"
"	/*selection-background-color: #0192ef;*/\n"
"}")
        self.label_11 = QLabel(self.page_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(50, 110, 121, 20))
        font10 = QFont()
        font10.setPointSize(15)
        self.label_11.setFont(font10)
        self.label_11.setStyleSheet(u"color: rgb(14, 13, 106);")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.addStudent_button_2 = QPushButton(self.page_5)
        self.addStudent_button_2.setObjectName(u"addStudent_button_2")
        self.addStudent_button_2.setGeometry(QRect(30, 100, 121, 35))
        self.addStudent_button_2.setMinimumSize(QSize(0, 35))
        self.addStudent_button_2.setMaximumSize(QSize(16777215, 35))
        self.addStudent_button_2.setFont(font1)
        self.addStudent_button_2.setStyleSheet(u"QPushButton{\n"
"	background-color: #af8501;\n"
"	color: #ffffff;\n"
"	border-radius: 5px;\n"
"	border: none;\n"
"	font-weight: bold;\n"
"	font-size: 12px;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/Icons/ad-blocker (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.addStudent_button_2.setIcon(icon12)
        self.addStudent_button_2.setIconSize(QSize(16, 16))
        self.violence_reoprts_table = QTableWidget(self.page_5)
        if (self.violence_reoprts_table.columnCount() < 2):
            self.violence_reoprts_table.setColumnCount(2)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.violence_reoprts_table.setHorizontalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.violence_reoprts_table.setHorizontalHeaderItem(1, __qtablewidgetitem27)
        if (self.violence_reoprts_table.rowCount() < 7):
            self.violence_reoprts_table.setRowCount(7)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.violence_reoprts_table.setVerticalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.violence_reoprts_table.setVerticalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.violence_reoprts_table.setVerticalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.violence_reoprts_table.setVerticalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.violence_reoprts_table.setVerticalHeaderItem(4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.violence_reoprts_table.setVerticalHeaderItem(5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.violence_reoprts_table.setVerticalHeaderItem(6, __qtablewidgetitem34)
        self.violence_reoprts_table.setObjectName(u"violence_reoprts_table")
        self.violence_reoprts_table.setGeometry(QRect(30, 160, 838, 411))
        sizePolicy.setHeightForWidth(self.violence_reoprts_table.sizePolicy().hasHeightForWidth())
        self.violence_reoprts_table.setSizePolicy(sizePolicy)
        self.violence_reoprts_table.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: #0e0d6a;\n"
"	color: white;\n"
"	border-radius: 2px\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #bdbdbd;\n"
"	background-color: #ececec;\n"
"	border-radius:15px;\n"
"	width: 100%;\n"
"	\n"
"   color: #0e0d6a;"
"/*width: 821 px;\n"
"height: 661 px;*/\n"
"}")
        self.violence_reoprts_table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.violence_reoprts_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.violence_reoprts_table.setAlternatingRowColors(True)
        self.violence_reoprts_table.horizontalHeader().setDefaultSectionSize(411)
        self.label_13 = QLabel(self.page_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(80, 20, 241, 31))
        self.label_13.setFont(font4)
        self.label_13.setStyleSheet(u"color: rgb(14, 13, 106);")
        self.label_29 = QLabel(self.page_5)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(30, 20, 41, 31))
        self.label_29.setPixmap(QPixmap(u":/Icons/report (1).png"))
        self.label_29.setScaledContents(True)
        self.stackedWidget.addWidget(self.page_5)

        self.verticalLayout_3.addWidget(self.main_sceen_widget)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.home_2.toggled.connect(self.home_1.setChecked)
        self.classMonitoring_2.toggled.connect(self.classMonitoring_1.setChecked)
        self.attendance_2.toggled.connect(self.attendance_1.setChecked)
        self.students_2.toggled.connect(self.students_1.setChecked)
        self.reports_2.toggled.connect(self.reports_1.setChecked)
        self.home_1.toggled.connect(self.home_2.setChecked)
        self.students_1.toggled.connect(self.students_2.setChecked)
        self.classMonitoring_1.toggled.connect(self.classMonitoring_2.setChecked)
        self.attendance_1.toggled.connect(self.attendance_2.setChecked)
        self.reports_1.toggled.connect(self.reports_2.setChecked)
        self.pushButton_3.toggled.connect(self.icon_text_widget.setVisible)
        self.pushButton_3.toggled.connect(self.icon_only_widget.setHidden)
        self.attendance_monitoring_1.toggled.connect(self.attendance_monitoring_2.setChecked)
        self.attendance_monitoring_2.toggled.connect(self.attendance_monitoring_1.setChecked)

        self.stackedWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.home_1.setText("")
        self.students_1.setText("")
        self.classMonitoring_1.setText("")
        self.attendance_monitoring_1.setText("")
        self.attendance_1.setText("")
        self.reports_1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Smart School", None))
        self.home_2.setText(QCoreApplication.translate("MainWindow", u"  Home", None))
        self.students_2.setText(QCoreApplication.translate("MainWindow", u"  Students", None))
        self.classMonitoring_2.setText(QCoreApplication.translate("MainWindow", u"  Class Monitoring", None))
        self.attendance_monitoring_2.setText(QCoreApplication.translate("MainWindow", u" Attendance Monitoring", None))
        self.attendance_2.setText(QCoreApplication.translate("MainWindow", u"  Attendance Reports", None))
        self.reports_2.setText(QCoreApplication.translate("MainWindow", u"Violence Reports", None))
        self.pushButton_3.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Here...", None))
        self.pushButton_4.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_24.setText("")
        self.label_16.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Students Marks Bar Graph", None))
        self.label_21.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Total Students By Gender", None))
        self.label_5.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Total Courses", None))
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"48", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Staff", None))
        self.label_19.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"230", None))
        self.label_22.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Attendance of different stages", None))
        self.label.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Events Calender", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Students Information", None))
        ___qtablewidgetitem = self.studentInfo_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.studentInfo_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Student ID", None));
        ___qtablewidgetitem2 = self.studentInfo_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem3 = self.studentInfo_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem4 = self.studentInfo_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Birthdate", None));
        ___qtablewidgetitem5 = self.studentInfo_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem6 = self.studentInfo_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem7 = self.studentInfo_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Phone", None));
        ___qtablewidgetitem8 = self.studentInfo_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem9 = self.studentInfo_table.verticalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem10 = self.studentInfo_table.verticalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem11 = self.studentInfo_table.verticalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem12 = self.studentInfo_table.verticalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem13 = self.studentInfo_table.verticalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem14 = self.studentInfo_table.verticalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"5", None));
        self.label_25.setText("")
        self.addStudent_button.setText(QCoreApplication.translate("MainWindow", u"Add Student", None))
        self.select_gender.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT GENDER", None))
        self.select_gender.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.select_gender.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))

        self.select_class.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT CLASS", None))
        self.select_class.setItemText(1, QCoreApplication.translate("MainWindow", u"Kindergarten (KG) 1", None))
        self.select_class.setItemText(2, QCoreApplication.translate("MainWindow", u"Kindergarten (KG) 2", None))
        self.select_class.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.select_class.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.select_class.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.select_class.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.select_class.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.select_class.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.select_class.setItemText(9, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.select_class.setItemText(10, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.select_class.setItemText(11, QCoreApplication.translate("MainWindow", u"Grade 9", None))
        self.select_class.setItemText(12, QCoreApplication.translate("MainWindow", u"Grade 10", None))
        self.select_class.setItemText(13, QCoreApplication.translate("MainWindow", u"Grade 11", None))
        self.select_class.setItemText(14, QCoreApplication.translate("MainWindow", u"Grade 12", None))

        self.search_student.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Students...", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Class Monitoring Page", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Attendance Monitoring Page", None))
        self.label_26.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Attendance", None))
        ___qtablewidgetitem15 = self.studentInfo_table_2.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Student ID", None));
        ___qtablewidgetitem16 = self.studentInfo_table_2.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem17 = self.studentInfo_table_2.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem18 = self.studentInfo_table_2.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem19 = self.studentInfo_table_2.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem20 = self.studentInfo_table_2.verticalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem21 = self.studentInfo_table_2.verticalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem22 = self.studentInfo_table_2.verticalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem23 = self.studentInfo_table_2.verticalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem24 = self.studentInfo_table_2.verticalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem25 = self.studentInfo_table_2.verticalHeaderItem(5)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"6", None));
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Select Date", None))
        self.addStudent_button_2.setText(QCoreApplication.translate("MainWindow", u"Display Video", None))
        ___qtablewidgetitem26 = self.violence_reoprts_table.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem27 = self.violence_reoprts_table.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem28 = self.violence_reoprts_table.verticalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem29 = self.violence_reoprts_table.verticalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem30 = self.violence_reoprts_table.verticalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem31 = self.violence_reoprts_table.verticalHeaderItem(3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem32 = self.violence_reoprts_table.verticalHeaderItem(4)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem33 = self.violence_reoprts_table.verticalHeaderItem(5)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem34 = self.violence_reoprts_table.verticalHeaderItem(6)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"7", None));
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Violence Reports", None))
        self.label_29.setText("")
    # retranslateUi

