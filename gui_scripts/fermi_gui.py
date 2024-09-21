# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout_form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QCommandLinkButton,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QStatusBar,
    QTabWidget, QTextBrowser, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(787, 733)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(750, 150))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(1, 1))
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.tabWidget.setStyleSheet(u"")
        self.tab_vmi_main = QWidget()
        self.tab_vmi_main.setObjectName(u"tab_vmi_main")
        sizePolicy.setHeightForWidth(self.tab_vmi_main.sizePolicy().hasHeightForWidth())
        self.tab_vmi_main.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.tab_vmi_main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.tab_vmi_main)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(400, 300))
        self.frame_3.setMaximumSize(QSize(400, 300))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.label_current_folder = QLabel(self.frame_3)
        self.label_current_folder.setObjectName(u"label_current_folder")
        self.label_current_folder.setGeometry(QRect(10, 10, 81, 16))
        self.button_stay_current_folder = QCommandLinkButton(self.frame_3)
        self.button_stay_current_folder.setObjectName(u"button_stay_current_folder")
        self.button_stay_current_folder.setGeometry(QRect(0, 160, 181, 31))
        self.button_auto_newest_folder = QCommandLinkButton(self.frame_3)
        self.button_auto_newest_folder.setObjectName(u"button_auto_newest_folder")
        self.button_auto_newest_folder.setGeometry(QRect(0, 130, 181, 31))
        self.label_files_used = QLabel(self.frame_3)
        self.label_files_used.setObjectName(u"label_files_used")
        self.label_files_used.setGeometry(QRect(200, 90, 61, 16))
        self.scrollArea = QScrollArea(self.frame_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(200, 120, 161, 161))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 159, 159))
        self.gridLayoutWidget_12 = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget_12.setObjectName(u"gridLayoutWidget_12")
        self.gridLayoutWidget_12.setGeometry(QRect(0, 0, 160, 161))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_12)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.text_browser_files = QTextBrowser(self.gridLayoutWidget_12)
        self.text_browser_files.setObjectName(u"text_browser_files")
        self.text_browser_files.setStyleSheet(u"background-color: rgb(158, 158, 158);")

        self.gridLayout_5.addWidget(self.text_browser_files, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.text_display_update_status = QTextBrowser(self.frame_3)
        self.text_display_update_status.setObjectName(u"text_display_update_status")
        self.text_display_update_status.setGeometry(QRect(90, 210, 71, 31))
        self.text_browser_num_files = QTextBrowser(self.frame_3)
        self.text_browser_num_files.setObjectName(u"text_browser_num_files")
        self.text_browser_num_files.setGeometry(QRect(260, 80, 51, 31))
        self.text_browser_num_files.setStyleSheet(u"background-color: rgb(158, 158, 158);")
        self.text_edit_current_folder = QTextEdit(self.frame_3)
        self.text_edit_current_folder.setObjectName(u"text_edit_current_folder")
        self.text_edit_current_folder.setGeometry(QRect(10, 30, 351, 41))
        self.button_stop_fetch = QCommandLinkButton(self.frame_3)
        self.button_stop_fetch.setObjectName(u"button_stop_fetch")
        self.button_stop_fetch.setGeometry(QRect(0, 270, 181, 31))
        self.test_display_folder_status = QTextBrowser(self.frame_3)
        self.test_display_folder_status.setObjectName(u"test_display_folder_status")
        self.test_display_folder_status.setGeometry(QRect(90, 100, 71, 31))
        self.label_folder_status = QLabel(self.frame_3)
        self.label_folder_status.setObjectName(u"label_folder_status")
        self.label_folder_status.setGeometry(QRect(10, 100, 91, 16))
        self.button_fetch_new_files = QCommandLinkButton(self.frame_3)
        self.button_fetch_new_files.setObjectName(u"button_fetch_new_files")
        self.button_fetch_new_files.setGeometry(QRect(0, 240, 181, 31))
        self.label_update_status = QLabel(self.frame_3)
        self.label_update_status.setObjectName(u"label_update_status")
        self.label_update_status.setGeometry(QRect(10, 210, 91, 16))

        self.horizontalLayout_2.addWidget(self.frame_3)

        self.tabWidget_2 = QTabWidget(self.frame)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.tab_7.setAutoFillBackground(False)
        self.gridLayout_16 = QGridLayout(self.tab_7)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.vmi_fore = QGridLayout()
        self.vmi_fore.setObjectName(u"vmi_fore")

        self.gridLayout_16.addLayout(self.vmi_fore, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_17 = QGridLayout(self.tab_8)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.vmi_back = QGridLayout()
        self.vmi_back.setObjectName(u"vmi_back")

        self.gridLayout_17.addLayout(self.vmi_back, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.gridLayout_18 = QGridLayout(self.tab_10)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.vmi_subt = QGridLayout()
        self.vmi_subt.setObjectName(u"vmi_subt")

        self.gridLayout_18.addLayout(self.vmi_subt, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_10, "")

        self.horizontalLayout_2.addWidget(self.tabWidget_2)

        self.horizontalLayout_2.setStretch(0, 6)
        self.horizontalLayout_2.setStretch(1, 5)

        self.verticalLayout_3.addWidget(self.frame)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.box_pes = QCheckBox(self.frame_6)
        self.box_pes.setObjectName(u"box_pes")

        self.gridLayout_4.addWidget(self.box_pes, 2, 0, 1, 1)

        self.box_beta1 = QCheckBox(self.frame_6)
        self.box_beta1.setObjectName(u"box_beta1")

        self.gridLayout_4.addWidget(self.box_beta1, 3, 0, 1, 1)

        self.box_beta2 = QCheckBox(self.frame_6)
        self.box_beta2.setObjectName(u"box_beta2")

        self.gridLayout_4.addWidget(self.box_beta2, 4, 0, 1, 1)

        self.box_beta3 = QCheckBox(self.frame_6)
        self.box_beta3.setObjectName(u"box_beta3")

        self.gridLayout_4.addWidget(self.box_beta3, 5, 0, 1, 1)

        self.box_beta4 = QCheckBox(self.frame_6)
        self.box_beta4.setObjectName(u"box_beta4")

        self.gridLayout_4.addWidget(self.box_beta4, 6, 0, 1, 1)

        self.label_abel_inversion = QLabel(self.frame_6)
        self.label_abel_inversion.setObjectName(u"label_abel_inversion")

        self.gridLayout_4.addWidget(self.label_abel_inversion, 1, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_4)

        self.vmi_abel = QVBoxLayout()
        self.vmi_abel.setObjectName(u"vmi_abel")

        self.horizontalLayout.addLayout(self.vmi_abel)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 7)

        self.verticalLayout_3.addWidget(self.frame_6)

        self.verticalLayout_3.setStretch(0, 5)
        self.verticalLayout_3.setStretch(1, 2)

        self.verticalLayout.addWidget(self.frame_2)

        self.tabWidget.addTab(self.tab_vmi_main, "")
        self.tab_image_correction = QWidget()
        self.tab_image_correction.setObjectName(u"tab_image_correction")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tab_image_correction.sizePolicy().hasHeightForWidth())
        self.tab_image_correction.setSizePolicy(sizePolicy2)
        self.verticalLayout_6 = QVBoxLayout(self.tab_image_correction)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_5 = QFrame(self.tab_image_correction)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tabWidget_4 = QTabWidget(self.frame_5)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        sizePolicy.setHeightForWidth(self.tab_4.sizePolicy().hasHeightForWidth())
        self.tab_4.setSizePolicy(sizePolicy)
        self.gridLayout_6 = QGridLayout(self.tab_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.vmi_show_raw = QGridLayout()
        self.vmi_show_raw.setObjectName(u"vmi_show_raw")

        self.gridLayout_6.addLayout(self.vmi_show_raw, 0, 0, 1, 1)

        self.tabWidget_4.addTab(self.tab_4, "")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        sizePolicy.setHeightForWidth(self.tab_15.sizePolicy().hasHeightForWidth())
        self.tab_15.setSizePolicy(sizePolicy)
        self.gridLayout_11 = QGridLayout(self.tab_15)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.vmi_show_fit = QGridLayout()
        self.vmi_show_fit.setObjectName(u"vmi_show_fit")

        self.gridLayout_11.addLayout(self.vmi_show_fit, 0, 0, 1, 1)

        self.tabWidget_4.addTab(self.tab_15, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        sizePolicy.setHeightForWidth(self.tab_5.sizePolicy().hasHeightForWidth())
        self.tab_5.setSizePolicy(sizePolicy)
        self.gridLayout_7 = QGridLayout(self.tab_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.vmi_show_inverse = QGridLayout()
        self.vmi_show_inverse.setObjectName(u"vmi_show_inverse")

        self.gridLayout_7.addLayout(self.vmi_show_inverse, 0, 0, 1, 1)

        self.tabWidget_4.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        sizePolicy.setHeightForWidth(self.tab_6.sizePolicy().hasHeightForWidth())
        self.tab_6.setSizePolicy(sizePolicy)
        self.gridLayout_8 = QGridLayout(self.tab_6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.vmi_show_radialdist = QGridLayout()
        self.vmi_show_radialdist.setObjectName(u"vmi_show_radialdist")

        self.gridLayout_8.addLayout(self.vmi_show_radialdist, 0, 0, 1, 1)

        self.tabWidget_4.addTab(self.tab_6, "")

        self.horizontalLayout_4.addWidget(self.tabWidget_4)

        self.tabWidget_5 = QTabWidget(self.frame_5)
        self.tabWidget_5.setObjectName(u"tabWidget_5")
        self.tabWidget_5.setStyleSheet(u"")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        sizePolicy.setHeightForWidth(self.tab_13.sizePolicy().hasHeightForWidth())
        self.tab_13.setSizePolicy(sizePolicy)
        self.gridLayout_9 = QGridLayout(self.tab_13)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.vmi_show_corrected = QGridLayout()
        self.vmi_show_corrected.setObjectName(u"vmi_show_corrected")

        self.gridLayout_9.addLayout(self.vmi_show_corrected, 0, 0, 1, 1)

        self.tabWidget_5.addTab(self.tab_13, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        sizePolicy.setHeightForWidth(self.tab_14.sizePolicy().hasHeightForWidth())
        self.tab_14.setSizePolicy(sizePolicy)
        self.gridLayout_10 = QGridLayout(self.tab_14)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.vmi_show_reduced = QGridLayout()
        self.vmi_show_reduced.setObjectName(u"vmi_show_reduced")

        self.gridLayout_10.addLayout(self.vmi_show_reduced, 0, 0, 1, 1)

        self.tabWidget_5.addTab(self.tab_14, "")

        self.horizontalLayout_4.addWidget(self.tabWidget_5)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout_6.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.tab_image_correction)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setMinimumSize(QSize(750, 175))
        self.frame_7.setMaximumSize(QSize(750, 200))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_4 = QGroupBox(self.frame_7)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.label_guess_ycenter = QLabel(self.groupBox_4)
        self.label_guess_ycenter.setObjectName(u"label_guess_ycenter")
        self.label_guess_ycenter.setGeometry(QRect(60, 20, 49, 16))
        self.label_guess_rotate = QLabel(self.groupBox_4)
        self.label_guess_rotate.setObjectName(u"label_guess_rotate")
        self.label_guess_rotate.setGeometry(QRect(130, 20, 49, 16))
        self.label_guess_xzoom = QLabel(self.groupBox_4)
        self.label_guess_xzoom.setObjectName(u"label_guess_xzoom")
        self.label_guess_xzoom.setGeometry(QRect(10, 80, 49, 16))
        self.label_guess_xcenter = QLabel(self.groupBox_4)
        self.label_guess_xcenter.setObjectName(u"label_guess_xcenter")
        self.label_guess_xcenter.setGeometry(QRect(10, 20, 49, 16))
        self.label_guess_yzoom = QLabel(self.groupBox_4)
        self.label_guess_yzoom.setObjectName(u"label_guess_yzoom")
        self.label_guess_yzoom.setGeometry(QRect(60, 80, 49, 16))
        self.text_display_guess_xcenter = QTextBrowser(self.groupBox_4)
        self.text_display_guess_xcenter.setObjectName(u"text_display_guess_xcenter")
        self.text_display_guess_xcenter.setGeometry(QRect(10, 40, 41, 31))
        self.text_dsplay_guess_ycenter = QTextBrowser(self.groupBox_4)
        self.text_dsplay_guess_ycenter.setObjectName(u"text_dsplay_guess_ycenter")
        self.text_dsplay_guess_ycenter.setGeometry(QRect(60, 40, 41, 31))
        self.text_display_guess_rotate = QTextBrowser(self.groupBox_4)
        self.text_display_guess_rotate.setObjectName(u"text_display_guess_rotate")
        self.text_display_guess_rotate.setGeometry(QRect(130, 40, 41, 31))
        self.text_display_guess_xzoom = QTextBrowser(self.groupBox_4)
        self.text_display_guess_xzoom.setObjectName(u"text_display_guess_xzoom")
        self.text_display_guess_xzoom.setGeometry(QRect(10, 100, 41, 31))
        self.text_diesplay_guess_yzoom = QTextBrowser(self.groupBox_4)
        self.text_diesplay_guess_yzoom.setObjectName(u"text_diesplay_guess_yzoom")
        self.text_diesplay_guess_yzoom.setGeometry(QRect(60, 100, 41, 31))
        self.button_get_guess_vmi_corrections = QCommandLinkButton(self.groupBox_4)
        self.button_get_guess_vmi_corrections.setObjectName(u"button_get_guess_vmi_corrections")
        self.button_get_guess_vmi_corrections.setGeometry(QRect(120, 100, 111, 41))

        self.horizontalLayout_3.addWidget(self.groupBox_4)

        self.frame_4 = QFrame(self.frame_7)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.groupBox_3 = QGroupBox(self.frame_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 60, 201, 91))
        self.box_ring_ellipticity = QCheckBox(self.groupBox_3)
        self.box_ring_ellipticity.setObjectName(u"box_ring_ellipticity")
        self.box_ring_ellipticity.setGeometry(QRect(10, 60, 111, 22))
        self.text_edit_show_rings = QTextEdit(self.groupBox_3)
        self.text_edit_show_rings.setObjectName(u"text_edit_show_rings")
        self.text_edit_show_rings.setGeometry(QRect(80, 30, 101, 31))
        self.label_show_rings = QLabel(self.groupBox_3)
        self.label_show_rings.setObjectName(u"label_show_rings")
        self.label_show_rings.setGeometry(QRect(10, 30, 71, 16))
        self.label_subfolder_extension_3 = QLabel(self.frame_4)
        self.label_subfolder_extension_3.setObjectName(u"label_subfolder_extension_3")
        self.label_subfolder_extension_3.setGeometry(QRect(90, 30, 31, 31))
        font = QFont()
        font.setPointSize(16)
        self.label_subfolder_extension_3.setFont(font)
        self.label_gdata_image_size = QLabel(self.frame_4)
        self.label_gdata_image_size.setObjectName(u"label_gdata_image_size")
        self.label_gdata_image_size.setGeometry(QRect(120, 10, 101, 16))
        self.label_reduce_image_size = QLabel(self.frame_4)
        self.label_reduce_image_size.setObjectName(u"label_reduce_image_size")
        self.label_reduce_image_size.setGeometry(QRect(10, 10, 101, 16))
        self.text_browser_gdata_image_size = QTextBrowser(self.frame_4)
        self.text_browser_gdata_image_size.setObjectName(u"text_browser_gdata_image_size")
        self.text_browser_gdata_image_size.setGeometry(QRect(130, 30, 51, 31))
        self.text_browser_gdata_image_size.setStyleSheet(u"background-color: rgb(144, 144, 144);")
        self.text_edit_reduce_image_size = QTextEdit(self.frame_4)
        self.text_edit_reduce_image_size.setObjectName(u"text_edit_reduce_image_size")
        self.text_edit_reduce_image_size.setGeometry(QRect(30, 30, 51, 31))

        self.horizontalLayout_3.addWidget(self.frame_4)

        self.groupBox_5 = QGroupBox(self.frame_7)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.text_edit_correct_yzoom = QTextEdit(self.groupBox_5)
        self.text_edit_correct_yzoom.setObjectName(u"text_edit_correct_yzoom")
        self.text_edit_correct_yzoom.setGeometry(QRect(60, 100, 41, 31))
        self.label_correct_ycenter = QLabel(self.groupBox_5)
        self.label_correct_ycenter.setObjectName(u"label_correct_ycenter")
        self.label_correct_ycenter.setGeometry(QRect(60, 20, 49, 16))
        self.text_edit_correct_rotate = QTextEdit(self.groupBox_5)
        self.text_edit_correct_rotate.setObjectName(u"text_edit_correct_rotate")
        self.text_edit_correct_rotate.setGeometry(QRect(130, 40, 41, 31))
        self.text_edit_correct_xcenter = QTextEdit(self.groupBox_5)
        self.text_edit_correct_xcenter.setObjectName(u"text_edit_correct_xcenter")
        self.text_edit_correct_xcenter.setGeometry(QRect(10, 40, 41, 31))
        self.text_edit_correct_xzoom = QTextEdit(self.groupBox_5)
        self.text_edit_correct_xzoom.setObjectName(u"text_edit_correct_xzoom")
        self.text_edit_correct_xzoom.setGeometry(QRect(10, 100, 41, 31))
        self.text_edit_correct_ycenter = QTextEdit(self.groupBox_5)
        self.text_edit_correct_ycenter.setObjectName(u"text_edit_correct_ycenter")
        self.text_edit_correct_ycenter.setGeometry(QRect(60, 40, 41, 31))
        self.label_correct_rotate = QLabel(self.groupBox_5)
        self.label_correct_rotate.setObjectName(u"label_correct_rotate")
        self.label_correct_rotate.setGeometry(QRect(130, 20, 49, 16))
        self.label_correct_xzoom = QLabel(self.groupBox_5)
        self.label_correct_xzoom.setObjectName(u"label_correct_xzoom")
        self.label_correct_xzoom.setGeometry(QRect(10, 80, 49, 16))
        self.label_correct_xcenter = QLabel(self.groupBox_5)
        self.label_correct_xcenter.setObjectName(u"label_correct_xcenter")
        self.label_correct_xcenter.setGeometry(QRect(10, 20, 49, 16))
        self.label_correct_yzoom = QLabel(self.groupBox_5)
        self.label_correct_yzoom.setObjectName(u"label_correct_yzoom")
        self.label_correct_yzoom.setGeometry(QRect(60, 80, 49, 16))
        self.button_apply_vmi_corrections = QCommandLinkButton(self.groupBox_5)
        self.button_apply_vmi_corrections.setObjectName(u"button_apply_vmi_corrections")
        self.button_apply_vmi_corrections.setGeometry(QRect(120, 100, 161, 41))

        self.horizontalLayout_3.addWidget(self.groupBox_5)

        self.horizontalLayout_3.setStretch(0, 5)
        self.horizontalLayout_3.setStretch(1, 5)
        self.horizontalLayout_3.setStretch(2, 6)

        self.verticalLayout_6.addWidget(self.frame_7)

        self.tabWidget.addTab(self.tab_image_correction, "")
        self.tab_calibration = QWidget()
        self.tab_calibration.setObjectName(u"tab_calibration")
        self.verticalLayout_18 = QVBoxLayout(self.tab_calibration)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_17 = QFrame(self.tab_calibration)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_15 = QFrame(self.frame_17)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_15)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.groupBox_10 = QGroupBox(self.frame_15)
        self.groupBox_10.setObjectName(u"groupBox_10")
        sizePolicy.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy)
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.pes_show_rsquare = QGridLayout()
        self.pes_show_rsquare.setObjectName(u"pes_show_rsquare")

        self.verticalLayout_14.addLayout(self.pes_show_rsquare)


        self.verticalLayout_16.addWidget(self.groupBox_10)

        self.groupBox_9 = QGroupBox(self.frame_15)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy)
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.pes_show_ke = QGridLayout()
        self.pes_show_ke.setObjectName(u"pes_show_ke")

        self.verticalLayout_13.addLayout(self.pes_show_ke)


        self.verticalLayout_16.addWidget(self.groupBox_9)


        self.horizontalLayout_6.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_17)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_16)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.groupBox_11 = QGroupBox(self.frame_16)
        self.groupBox_11.setObjectName(u"groupBox_11")
        sizePolicy.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy)
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.rsquare_show_calibration = QGridLayout()
        self.rsquare_show_calibration.setObjectName(u"rsquare_show_calibration")

        self.verticalLayout_15.addLayout(self.rsquare_show_calibration)


        self.verticalLayout_17.addWidget(self.groupBox_11)

        self.frame_14 = QFrame(self.frame_16)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy1.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy1)
        self.frame_14.setMinimumSize(QSize(300, 325))
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.label_pes_cal_constants = QLabel(self.frame_14)
        self.label_pes_cal_constants.setObjectName(u"label_pes_cal_constants")
        self.label_pes_cal_constants.setGeometry(QRect(180, 0, 91, 21))
        self.label_cal_points = QLabel(self.frame_14)
        self.label_cal_points.setObjectName(u"label_cal_points")
        self.label_cal_points.setGeometry(QRect(10, 0, 101, 21))
        self.test_edit_cal_points = QTextEdit(self.frame_14)
        self.test_edit_cal_points.setObjectName(u"test_edit_cal_points")
        self.test_edit_cal_points.setGeometry(QRect(10, 30, 91, 131))
        self.text_edit_cal_constant = QTextEdit(self.frame_14)
        self.text_edit_cal_constant.setObjectName(u"text_edit_cal_constant")
        self.text_edit_cal_constant.setGeometry(QRect(160, 30, 121, 31))
        self.label_ke_start = QLabel(self.frame_14)
        self.label_ke_start.setObjectName(u"label_ke_start")
        self.label_ke_start.setGeometry(QRect(90, 260, 51, 16))
        self.text_edit_ke_start = QTextEdit(self.frame_14)
        self.text_edit_ke_start.setObjectName(u"text_edit_ke_start")
        self.text_edit_ke_start.setGeometry(QRect(90, 280, 41, 31))
        self.label_pes_constant_alpha = QLabel(self.frame_14)
        self.label_pes_constant_alpha.setObjectName(u"label_pes_constant_alpha")
        self.label_pes_constant_alpha.setGeometry(QRect(120, 30, 61, 16))
        self.button_apply_pes_use_constants = QCommandLinkButton(self.frame_14)
        self.button_apply_pes_use_constants.setObjectName(u"button_apply_pes_use_constants")
        self.button_apply_pes_use_constants.setGeometry(QRect(150, 100, 131, 41))
        self.label_ke_end = QLabel(self.frame_14)
        self.label_ke_end.setObjectName(u"label_ke_end")
        self.label_ke_end.setGeometry(QRect(160, 260, 51, 16))
        self.label_ke_bins = QLabel(self.frame_14)
        self.label_ke_bins.setObjectName(u"label_ke_bins")
        self.label_ke_bins.setGeometry(QRect(230, 260, 51, 16))
        self.text_edit_ke_bins = QTextEdit(self.frame_14)
        self.text_edit_ke_bins.setObjectName(u"text_edit_ke_bins")
        self.text_edit_ke_bins.setGeometry(QRect(230, 280, 41, 31))
        self.button_apply_pes_calibration = QCommandLinkButton(self.frame_14)
        self.button_apply_pes_calibration.setObjectName(u"button_apply_pes_calibration")
        self.button_apply_pes_calibration.setGeometry(QRect(0, 160, 172, 41))
        self.text_edit_ke_end = QTextEdit(self.frame_14)
        self.text_edit_ke_end.setObjectName(u"text_edit_ke_end")
        self.text_edit_ke_end.setGeometry(QRect(160, 280, 41, 31))

        self.verticalLayout_17.addWidget(self.frame_14)

        self.verticalLayout_17.setStretch(0, 5)
        self.verticalLayout_17.setStretch(1, 2)

        self.horizontalLayout_6.addWidget(self.frame_16)

        self.horizontalLayout_6.setStretch(0, 5)
        self.horizontalLayout_6.setStretch(1, 2)

        self.verticalLayout_18.addWidget(self.frame_17)

        self.tabWidget.addTab(self.tab_calibration, "")
        self.tab_tof_main = QWidget()
        self.tab_tof_main.setObjectName(u"tab_tof_main")
        self.verticalLayout_5 = QVBoxLayout(self.tab_tof_main)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_9 = QFrame(self.tab_tof_main)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget_3 = QTabWidget(self.frame_9)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        sizePolicy.setHeightForWidth(self.tab_9.sizePolicy().hasHeightForWidth())
        self.tab_9.setSizePolicy(sizePolicy)
        self.tab_9.setAutoFillBackground(False)
        self.gridLayout_20 = QGridLayout(self.tab_9)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.tof_fore = QGridLayout()
        self.tof_fore.setObjectName(u"tof_fore")

        self.gridLayout_20.addLayout(self.tof_fore, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_9, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        sizePolicy.setHeightForWidth(self.tab_11.sizePolicy().hasHeightForWidth())
        self.tab_11.setSizePolicy(sizePolicy)
        self.gridLayout_21 = QGridLayout(self.tab_11)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.tof_back = QGridLayout()
        self.tof_back.setObjectName(u"tof_back")

        self.gridLayout_21.addLayout(self.tof_back, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_11, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        sizePolicy.setHeightForWidth(self.tab_12.sizePolicy().hasHeightForWidth())
        self.tab_12.setSizePolicy(sizePolicy)
        self.gridLayout_22 = QGridLayout(self.tab_12)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.tof_subt = QGridLayout()
        self.tof_subt.setObjectName(u"tof_subt")

        self.gridLayout_22.addLayout(self.tof_subt, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_12, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        sizePolicy.setHeightForWidth(self.tab_2.sizePolicy().hasHeightForWidth())
        self.tab_2.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mq_fore = QGridLayout()
        self.mq_fore.setObjectName(u"mq_fore")

        self.gridLayout.addLayout(self.mq_fore, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        sizePolicy.setHeightForWidth(self.tab_3.sizePolicy().hasHeightForWidth())
        self.tab_3.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.mq_back = QGridLayout()
        self.mq_back.setObjectName(u"mq_back")

        self.gridLayout_2.addLayout(self.mq_back, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.mq_subt = QGridLayout()
        self.mq_subt.setObjectName(u"mq_subt")

        self.gridLayout_3.addLayout(self.mq_subt, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab, "")

        self.verticalLayout_4.addWidget(self.tabWidget_3)

        self.frame_8 = QFrame(self.frame_9)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setMinimumSize(QSize(750, 160))
        self.frame_8.setMaximumSize(QSize(760, 170))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.button_auto_newest_folder_2 = QCommandLinkButton(self.frame_8)
        self.button_auto_newest_folder_2.setObjectName(u"button_auto_newest_folder_2")
        self.button_auto_newest_folder_2.setGeometry(QRect(0, 100, 181, 31))
        self.label_update_status_2 = QLabel(self.frame_8)
        self.label_update_status_2.setObjectName(u"label_update_status_2")
        self.label_update_status_2.setGeometry(QRect(200, 70, 91, 16))
        self.test_display_folder_status_2 = QTextBrowser(self.frame_8)
        self.test_display_folder_status_2.setObjectName(u"test_display_folder_status_2")
        self.test_display_folder_status_2.setGeometry(QRect(90, 70, 71, 31))
        self.button_stay_current_folder_2 = QCommandLinkButton(self.frame_8)
        self.button_stay_current_folder_2.setObjectName(u"button_stay_current_folder_2")
        self.button_stay_current_folder_2.setGeometry(QRect(0, 130, 181, 31))
        self.button_fetch_new_files_2 = QCommandLinkButton(self.frame_8)
        self.button_fetch_new_files_2.setObjectName(u"button_fetch_new_files_2")
        self.button_fetch_new_files_2.setGeometry(QRect(190, 100, 181, 31))
        self.text_display_update_status_2 = QTextBrowser(self.frame_8)
        self.text_display_update_status_2.setObjectName(u"text_display_update_status_2")
        self.text_display_update_status_2.setGeometry(QRect(280, 70, 71, 31))
        self.label_folder_status_2 = QLabel(self.frame_8)
        self.label_folder_status_2.setObjectName(u"label_folder_status_2")
        self.label_folder_status_2.setGeometry(QRect(10, 70, 91, 16))
        self.text_edit_current_folder_2 = QTextEdit(self.frame_8)
        self.text_edit_current_folder_2.setObjectName(u"text_edit_current_folder_2")
        self.text_edit_current_folder_2.setGeometry(QRect(10, 30, 341, 31))
        self.button_stop_fetch_2 = QCommandLinkButton(self.frame_8)
        self.button_stop_fetch_2.setObjectName(u"button_stop_fetch_2")
        self.button_stop_fetch_2.setGeometry(QRect(190, 130, 181, 31))
        self.combobox_tof_yscale = QComboBox(self.frame_8)
        self.combobox_tof_yscale.addItem("")
        self.combobox_tof_yscale.addItem("")
        self.combobox_tof_yscale.setObjectName(u"combobox_tof_yscale")
        self.combobox_tof_yscale.setGeometry(QRect(570, 20, 131, 21))
        self.label_current_folder_2 = QLabel(self.frame_8)
        self.label_current_folder_2.setObjectName(u"label_current_folder_2")
        self.label_current_folder_2.setGeometry(QRect(10, 10, 81, 16))

        self.verticalLayout_4.addWidget(self.frame_8)

        self.verticalLayout_4.setStretch(0, 10)
        self.verticalLayout_4.setStretch(1, 5)

        self.verticalLayout_5.addWidget(self.frame_9)

        self.tabWidget.addTab(self.tab_tof_main, "")
        self.tab_tof_calibration = QWidget()
        self.tab_tof_calibration.setObjectName(u"tab_tof_calibration")
        self.verticalLayout_12 = QVBoxLayout(self.tab_tof_calibration)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_13 = QFrame(self.tab_tof_calibration)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_10 = QFrame(self.frame_13)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_7 = QGroupBox(self.frame_10)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tof_show_raw = QGridLayout()
        self.tof_show_raw.setObjectName(u"tof_show_raw")

        self.verticalLayout_8.addLayout(self.tof_show_raw)


        self.verticalLayout_9.addWidget(self.groupBox_7)

        self.groupBox_6 = QGroupBox(self.frame_10)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tof_show_mq = QGridLayout()
        self.tof_show_mq.setObjectName(u"tof_show_mq")

        self.verticalLayout_7.addLayout(self.tof_show_mq)


        self.verticalLayout_9.addWidget(self.groupBox_6)


        self.horizontalLayout_5.addWidget(self.frame_10)

        self.frame_12 = QFrame(self.frame_13)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy2.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy2)
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_12)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.groupBox_8 = QGroupBox(self.frame_12)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy)
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.tof_show_calibration = QGridLayout()
        self.tof_show_calibration.setObjectName(u"tof_show_calibration")

        self.verticalLayout_10.addLayout(self.tof_show_calibration)


        self.verticalLayout_11.addWidget(self.groupBox_8)

        self.frame_11 = QFrame(self.frame_12)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy1.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy1)
        self.frame_11.setMinimumSize(QSize(300, 325))
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.text_edit_tof_end = QTextEdit(self.frame_11)
        self.text_edit_tof_end.setObjectName(u"text_edit_tof_end")
        self.text_edit_tof_end.setGeometry(QRect(160, 220, 41, 31))
        self.button_apply_tof_calibration = QCommandLinkButton(self.frame_11)
        self.button_apply_tof_calibration.setObjectName(u"button_apply_tof_calibration")
        self.button_apply_tof_calibration.setGeometry(QRect(0, 160, 161, 41))
        self.label_tof_constant_t0 = QLabel(self.frame_11)
        self.label_tof_constant_t0.setObjectName(u"label_tof_constant_t0")
        self.label_tof_constant_t0.setGeometry(QRect(130, 60, 31, 16))
        self.text_edit_tof_cal_points = QTextEdit(self.frame_11)
        self.text_edit_tof_cal_points.setObjectName(u"text_edit_tof_cal_points")
        self.text_edit_tof_cal_points.setGeometry(QRect(10, 30, 91, 131))
        self.text_edit_tof_constant_c = QTextEdit(self.frame_11)
        self.text_edit_tof_constant_c.setObjectName(u"text_edit_tof_constant_c")
        self.text_edit_tof_constant_c.setGeometry(QRect(150, 30, 131, 31))
        self.text_edit_tof_constant_t0 = QTextEdit(self.frame_11)
        self.text_edit_tof_constant_t0.setObjectName(u"text_edit_tof_constant_t0")
        self.text_edit_tof_constant_t0.setGeometry(QRect(150, 60, 131, 31))
        self.label_tof_cal_points = QLabel(self.frame_11)
        self.label_tof_cal_points.setObjectName(u"label_tof_cal_points")
        self.label_tof_cal_points.setGeometry(QRect(20, 0, 71, 21))
        self.label_tof_constant_c = QLabel(self.frame_11)
        self.label_tof_constant_c.setObjectName(u"label_tof_constant_c")
        self.label_tof_constant_c.setGeometry(QRect(130, 30, 31, 16))
        self.text_edit_mq_bins = QTextEdit(self.frame_11)
        self.text_edit_mq_bins.setObjectName(u"text_edit_mq_bins")
        self.text_edit_mq_bins.setGeometry(QRect(230, 280, 41, 31))
        self.text_edit_mq_start = QTextEdit(self.frame_11)
        self.text_edit_mq_start.setObjectName(u"text_edit_mq_start")
        self.text_edit_mq_start.setGeometry(QRect(90, 280, 41, 31))
        self.label_tof_end = QLabel(self.frame_11)
        self.label_tof_end.setObjectName(u"label_tof_end")
        self.label_tof_end.setGeometry(QRect(160, 200, 51, 16))
        self.label_mq_start = QLabel(self.frame_11)
        self.label_mq_start.setObjectName(u"label_mq_start")
        self.label_mq_start.setGeometry(QRect(90, 260, 51, 16))
        self.button_apply_tof_use_constants = QCommandLinkButton(self.frame_11)
        self.button_apply_tof_use_constants.setObjectName(u"button_apply_tof_use_constants")
        self.button_apply_tof_use_constants.setGeometry(QRect(150, 100, 131, 41))
        self.label_tof_bins = QLabel(self.frame_11)
        self.label_tof_bins.setObjectName(u"label_tof_bins")
        self.label_tof_bins.setGeometry(QRect(230, 200, 51, 16))
        self.label_tof_constants = QLabel(self.frame_11)
        self.label_tof_constants.setObjectName(u"label_tof_constants")
        self.label_tof_constants.setGeometry(QRect(180, 0, 91, 21))
        self.text_edit_mq_end = QTextEdit(self.frame_11)
        self.text_edit_mq_end.setObjectName(u"text_edit_mq_end")
        self.text_edit_mq_end.setGeometry(QRect(160, 280, 41, 31))
        self.text_edit_tof_bins = QTextEdit(self.frame_11)
        self.text_edit_tof_bins.setObjectName(u"text_edit_tof_bins")
        self.text_edit_tof_bins.setGeometry(QRect(230, 220, 41, 31))
        self.label_mq_end = QLabel(self.frame_11)
        self.label_mq_end.setObjectName(u"label_mq_end")
        self.label_mq_end.setGeometry(QRect(160, 260, 51, 16))
        self.label_mq_bins = QLabel(self.frame_11)
        self.label_mq_bins.setObjectName(u"label_mq_bins")
        self.label_mq_bins.setGeometry(QRect(230, 260, 51, 16))
        self.label_tof_start = QLabel(self.frame_11)
        self.label_tof_start.setObjectName(u"label_tof_start")
        self.label_tof_start.setGeometry(QRect(90, 200, 51, 16))
        self.text_edit_tof_start = QTextEdit(self.frame_11)
        self.text_edit_tof_start.setObjectName(u"text_edit_tof_start")
        self.text_edit_tof_start.setGeometry(QRect(90, 220, 41, 31))

        self.verticalLayout_11.addWidget(self.frame_11)

        self.verticalLayout_11.setStretch(1, 7)

        self.horizontalLayout_5.addWidget(self.frame_12)

        self.horizontalLayout_5.setStretch(0, 5)
        self.horizontalLayout_5.setStretch(1, 2)

        self.verticalLayout_12.addWidget(self.frame_13)

        self.tabWidget.addTab(self.tab_tof_calibration, "")
        self.tab_settings = QWidget()
        self.tab_settings.setObjectName(u"tab_settings")
        self.label_search_dir_for_newest_folder = QLabel(self.tab_settings)
        self.label_search_dir_for_newest_folder.setObjectName(u"label_search_dir_for_newest_folder")
        self.label_search_dir_for_newest_folder.setGeometry(QRect(320, 10, 211, 16))
        self.text_edit_search_dir_for_newest_folder = QTextEdit(self.tab_settings)
        self.text_edit_search_dir_for_newest_folder.setObjectName(u"text_edit_search_dir_for_newest_folder")
        self.text_edit_search_dir_for_newest_folder.setGeometry(QRect(320, 30, 271, 51))
        self.label_extract_tof_start = QLabel(self.tab_settings)
        self.label_extract_tof_start.setObjectName(u"label_extract_tof_start")
        self.label_extract_tof_start.setGeometry(QRect(20, 170, 81, 16))
        self.text_edit_extract_tof_start = QTextEdit(self.tab_settings)
        self.text_edit_extract_tof_start.setObjectName(u"text_edit_extract_tof_start")
        self.text_edit_extract_tof_start.setGeometry(QRect(20, 190, 71, 31))
        self.label_extract_tof_stop = QLabel(self.tab_settings)
        self.label_extract_tof_stop.setObjectName(u"label_extract_tof_stop")
        self.label_extract_tof_stop.setGeometry(QRect(110, 170, 81, 16))
        self.text_edit_extract_tof_stop = QTextEdit(self.tab_settings)
        self.text_edit_extract_tof_stop.setObjectName(u"text_edit_extract_tof_stop")
        self.text_edit_extract_tof_stop.setGeometry(QRect(110, 190, 71, 31))
        self.box_slu_parity = QCheckBox(self.tab_settings)
        self.box_slu_parity.setObjectName(u"box_slu_parity")
        self.box_slu_parity.setGeometry(QRect(320, 346, 21, 22))
        self.label_slu_parity = QLabel(self.tab_settings)
        self.label_slu_parity.setObjectName(u"label_slu_parity")
        self.label_slu_parity.setGeometry(QRect(350, 346, 121, 16))
        self.groupBox = QGroupBox(self.tab_settings)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 10, 181, 151))
        self.gridLayout_15 = QGridLayout(self.groupBox)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_files_per_cache = QLabel(self.groupBox)
        self.label_files_per_cache.setObjectName(u"label_files_per_cache")

        self.gridLayout_15.addWidget(self.label_files_per_cache, 0, 0, 1, 2)

        self.text_edit_files_per_cache = QTextEdit(self.groupBox)
        self.text_edit_files_per_cache.setObjectName(u"text_edit_files_per_cache")

        self.gridLayout_15.addWidget(self.text_edit_files_per_cache, 1, 0, 1, 2)

        self.box_make_cache = QCheckBox(self.groupBox)
        self.box_make_cache.setObjectName(u"box_make_cache")

        self.gridLayout_15.addWidget(self.box_make_cache, 2, 0, 1, 1)

        self.label_settings_make_cache = QLabel(self.groupBox)
        self.label_settings_make_cache.setObjectName(u"label_settings_make_cache")

        self.gridLayout_15.addWidget(self.label_settings_make_cache, 2, 1, 1, 1)

        self.box_load_from_cache = QCheckBox(self.groupBox)
        self.box_load_from_cache.setObjectName(u"box_load_from_cache")

        self.gridLayout_15.addWidget(self.box_load_from_cache, 3, 0, 1, 1)

        self.label_setting_load_from_cache = QLabel(self.groupBox)
        self.label_setting_load_from_cache.setObjectName(u"label_setting_load_from_cache")

        self.gridLayout_15.addWidget(self.label_setting_load_from_cache, 3, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab_settings)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(320, 176, 241, 147))
        self.label_fore = QLabel(self.groupBox_2)
        self.label_fore.setObjectName(u"label_fore")
        self.label_fore.setGeometry(QRect(12, 31, 23, 16))
        self.label_back = QLabel(self.groupBox_2)
        self.label_back.setObjectName(u"label_back")
        self.label_back.setGeometry(QRect(50, 32, 25, 16))
        self.box_fore_felonsluon = QCheckBox(self.groupBox_2)
        self.box_fore_felonsluon.setObjectName(u"box_fore_felonsluon")
        self.box_fore_felonsluon.setGeometry(QRect(12, 53, 16, 16))
        self.box_back_felonsluon = QCheckBox(self.groupBox_2)
        self.box_back_felonsluon.setObjectName(u"box_back_felonsluon")
        self.box_back_felonsluon.setGeometry(QRect(50, 54, 16, 16))
        self.label_felonsluon = QLabel(self.groupBox_2)
        self.label_felonsluon.setObjectName(u"label_felonsluon")
        self.label_felonsluon.setGeometry(QRect(140, 50, 84, 16))
        self.box_fore_felonsluoff = QCheckBox(self.groupBox_2)
        self.box_fore_felonsluoff.setObjectName(u"box_fore_felonsluoff")
        self.box_fore_felonsluoff.setGeometry(QRect(12, 75, 16, 16))
        self.box_back_felonsluoff = QCheckBox(self.groupBox_2)
        self.box_back_felonsluoff.setObjectName(u"box_back_felonsluoff")
        self.box_back_felonsluoff.setGeometry(QRect(50, 76, 16, 16))
        self.label_felonsluoff = QLabel(self.groupBox_2)
        self.label_felonsluoff.setObjectName(u"label_felonsluoff")
        self.label_felonsluoff.setGeometry(QRect(140, 72, 85, 16))
        self.box_fore_feloffsluon = QCheckBox(self.groupBox_2)
        self.box_fore_feloffsluon.setObjectName(u"box_fore_feloffsluon")
        self.box_fore_feloffsluon.setGeometry(QRect(12, 97, 16, 16))
        self.box_back_feloffsluon = QCheckBox(self.groupBox_2)
        self.box_back_feloffsluon.setObjectName(u"box_back_feloffsluon")
        self.box_back_feloffsluon.setGeometry(QRect(50, 98, 16, 16))
        self.label_feloffsluon = QLabel(self.groupBox_2)
        self.label_feloffsluon.setObjectName(u"label_feloffsluon")
        self.label_feloffsluon.setGeometry(QRect(140, 94, 85, 16))
        self.box_fore_feloffsluoff = QCheckBox(self.groupBox_2)
        self.box_fore_feloffsluoff.setObjectName(u"box_fore_feloffsluoff")
        self.box_fore_feloffsluoff.setGeometry(QRect(12, 119, 16, 16))
        self.box_back_feloffsluoff = QCheckBox(self.groupBox_2)
        self.box_back_feloffsluoff.setObjectName(u"box_back_feloffsluoff")
        self.box_back_feloffsluoff.setGeometry(QRect(50, 120, 16, 16))
        self.lafel_feloffsluon = QLabel(self.groupBox_2)
        self.lafel_feloffsluon.setObjectName(u"lafel_feloffsluon")
        self.lafel_feloffsluon.setGeometry(QRect(140, 116, 86, 16))
        self.box_flip_feloffsluon = QCheckBox(self.groupBox_2)
        self.box_flip_feloffsluon.setObjectName(u"box_flip_feloffsluon")
        self.box_flip_feloffsluon.setGeometry(QRect(90, 98, 16, 16))
        self.box_flip_felonsluon = QCheckBox(self.groupBox_2)
        self.box_flip_felonsluon.setObjectName(u"box_flip_felonsluon")
        self.box_flip_felonsluon.setGeometry(QRect(90, 54, 16, 16))
        self.label_back_2 = QLabel(self.groupBox_2)
        self.label_back_2.setObjectName(u"label_back_2")
        self.label_back_2.setGeometry(QRect(90, 32, 25, 16))
        self.box_flip_felonsluoff = QCheckBox(self.groupBox_2)
        self.box_flip_felonsluoff.setObjectName(u"box_flip_felonsluoff")
        self.box_flip_felonsluoff.setGeometry(QRect(90, 76, 16, 16))
        self.box_flip_feloffsluoff = QCheckBox(self.groupBox_2)
        self.box_flip_feloffsluoff.setObjectName(u"box_flip_feloffsluoff")
        self.box_flip_feloffsluoff.setGeometry(QRect(90, 120, 16, 16))
        self.applyChangesSettings = QCommandLinkButton(self.tab_settings)
        self.applyChangesSettings.setObjectName(u"applyChangesSettings")
        self.applyChangesSettings.setGeometry(QRect(420, 416, 141, 31))
        self.label_abel_inversion_data_path = QLabel(self.tab_settings)
        self.label_abel_inversion_data_path.setObjectName(u"label_abel_inversion_data_path")
        self.label_abel_inversion_data_path.setGeometry(QRect(20, 330, 131, 16))
        self.text_edit_abel_inversion_data_path = QTextEdit(self.tab_settings)
        self.text_edit_abel_inversion_data_path.setObjectName(u"text_edit_abel_inversion_data_path")
        self.text_edit_abel_inversion_data_path.setGeometry(QRect(20, 350, 171, 31))
        self.label_subfolder_extension = QLabel(self.tab_settings)
        self.label_subfolder_extension.setObjectName(u"label_subfolder_extension")
        self.label_subfolder_extension.setGeometry(QRect(320, 86, 211, 16))
        self.text_edit_subfolder_extension = QTextEdit(self.tab_settings)
        self.text_edit_subfolder_extension.setObjectName(u"text_edit_subfolder_extension")
        self.text_edit_subfolder_extension.setGeometry(QRect(350, 106, 241, 31))
        self.label_subfolder_extension_2 = QLabel(self.tab_settings)
        self.label_subfolder_extension_2.setObjectName(u"label_subfolder_extension_2")
        self.label_subfolder_extension_2.setGeometry(QRect(330, 105, 21, 31))
        self.label_subfolder_extension_2.setFont(font)
        self.text_edit_num_cores = QTextEdit(self.tab_settings)
        self.text_edit_num_cores.setObjectName(u"text_edit_num_cores")
        self.text_edit_num_cores.setGeometry(QRect(20, 412, 41, 31))
        self.label_num_cores = QLabel(self.tab_settings)
        self.label_num_cores.setObjectName(u"label_num_cores")
        self.label_num_cores.setGeometry(QRect(20, 390, 171, 16))
        self.label_max_cores = QLabel(self.tab_settings)
        self.label_max_cores.setObjectName(u"label_max_cores")
        self.label_max_cores.setGeometry(QRect(70, 410, 41, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_max_cores.setFont(font1)
        self.text_edit_search_regex = QTextEdit(self.tab_settings)
        self.text_edit_search_regex.setObjectName(u"text_edit_search_regex")
        self.text_edit_search_regex.setGeometry(QRect(600, 30, 141, 51))
        self.label_search_dir_for_newest_folder_2 = QLabel(self.tab_settings)
        self.label_search_dir_for_newest_folder_2.setObjectName(u"label_search_dir_for_newest_folder_2")
        self.label_search_dir_for_newest_folder_2.setGeometry(QRect(610, 10, 111, 16))
        self.text_browser_max_cores = QTextBrowser(self.tab_settings)
        self.text_browser_max_cores.setObjectName(u"text_browser_max_cores")
        self.text_browser_max_cores.setGeometry(QRect(90, 410, 41, 31))
        self.text_browser_max_cores.setStyleSheet(u"background-color: rgb(144, 144, 144);")
        self.label_tof_baseline_points = QLabel(self.tab_settings)
        self.label_tof_baseline_points.setObjectName(u"label_tof_baseline_points")
        self.label_tof_baseline_points.setGeometry(QRect(20, 240, 121, 16))
        self.text_edit_tof_baseline_points = QTextEdit(self.tab_settings)
        self.text_edit_tof_baseline_points.setObjectName(u"text_edit_tof_baseline_points")
        self.text_edit_tof_baseline_points.setGeometry(QRect(20, 260, 71, 31))
        self.pushButton = QPushButton(self.tab_settings)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(660, 470, 83, 29))
        self.tabWidget.addTab(self.tab_settings, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.print_browser = QTextBrowser(self.centralwidget)
        self.print_browser.setObjectName(u"print_browser")
        self.print_browser.setMinimumSize(QSize(750, 100))

        self.verticalLayout_2.addWidget(self.print_browser)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 787, 25))
        self.menuFERMI_On_line_analysis_tool = QMenu(self.menubar)
        self.menuFERMI_On_line_analysis_tool.setObjectName(u"menuFERMI_On_line_analysis_tool")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFERMI_On_line_analysis_tool.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(5)
        self.tabWidget_2.setCurrentIndex(2)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_current_folder.setText(QCoreApplication.translate("MainWindow", u"Current folder", None))
        self.button_stay_current_folder.setText(QCoreApplication.translate("MainWindow", u"Stay current folder", None))
        self.button_auto_newest_folder.setText(QCoreApplication.translate("MainWindow", u"Auto newest folder", None))
        self.label_files_used.setText(QCoreApplication.translate("MainWindow", u"Files used", None))
        self.text_display_update_status.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Stopped</p></body></html>", None))
        self.button_stop_fetch.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.test_display_folder_status.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Stay</p></body></html>", None))
        self.label_folder_status.setText(QCoreApplication.translate("MainWindow", u"Folder status:", None))
        self.button_fetch_new_files.setText(QCoreApplication.translate("MainWindow", u"Fetch new files", None))
        self.label_update_status.setText(QCoreApplication.translate("MainWindow", u"Update status:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Fore", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Back", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"Subt", None))
        self.box_pes.setText(QCoreApplication.translate("MainWindow", u"PES", None))
        self.box_beta1.setText(QCoreApplication.translate("MainWindow", u"beta1", None))
        self.box_beta2.setText(QCoreApplication.translate("MainWindow", u"beta2", None))
        self.box_beta3.setText(QCoreApplication.translate("MainWindow", u"beta3", None))
        self.box_beta4.setText(QCoreApplication.translate("MainWindow", u"beta4", None))
        self.label_abel_inversion.setText(QCoreApplication.translate("MainWindow", u"Abel inversion", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_vmi_main), QCoreApplication.translate("MainWindow", u"VMI Main", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Raw", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_15), QCoreApplication.translate("MainWindow", u"Fit", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Inverse", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Radial dist.", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"Corrected", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"Reduced", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Guess parameters", None))
        self.label_guess_ycenter.setText(QCoreApplication.translate("MainWindow", u"y-center", None))
        self.label_guess_rotate.setText(QCoreApplication.translate("MainWindow", u"rotate", None))
        self.label_guess_xzoom.setText(QCoreApplication.translate("MainWindow", u"x-zoom", None))
        self.label_guess_xcenter.setText(QCoreApplication.translate("MainWindow", u"x-center", None))
        self.label_guess_yzoom.setText(QCoreApplication.translate("MainWindow", u"y-zoom", None))
        self.text_display_guess_xcenter.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_dsplay_guess_ycenter.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_display_guess_rotate.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_display_guess_xzoom.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_diesplay_guess_yzoom.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.button_get_guess_vmi_corrections.setText(QCoreApplication.translate("MainWindow", u"Get guess", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Visual aids", None))
        self.box_ring_ellipticity.setText(QCoreApplication.translate("MainWindow", u"Ring ellipticity", None))
        self.text_edit_show_rings.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1, 2</p></body></html>", None))
        self.label_show_rings.setText(QCoreApplication.translate("MainWindow", u"Show rings", None))
        self.label_subfolder_extension_3.setText(QCoreApplication.translate("MainWindow", u"==", None))
        self.label_gdata_image_size.setText(QCoreApplication.translate("MainWindow", u"gdata image size", None))
        self.label_reduce_image_size.setText(QCoreApplication.translate("MainWindow", u"Reduce image size", None))
        self.text_edit_reduce_image_size.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Correction parameters", None))
        self.text_edit_correct_yzoom.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_correct_ycenter.setText(QCoreApplication.translate("MainWindow", u"y-center", None))
        self.text_edit_correct_rotate.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_edit_correct_xcenter.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_edit_correct_xzoom.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_edit_correct_ycenter.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_correct_rotate.setText(QCoreApplication.translate("MainWindow", u"rotate", None))
        self.label_correct_xzoom.setText(QCoreApplication.translate("MainWindow", u"x-zoom", None))
        self.label_correct_xcenter.setText(QCoreApplication.translate("MainWindow", u"x-center", None))
        self.label_correct_yzoom.setText(QCoreApplication.translate("MainWindow", u"y-zoom", None))
        self.button_apply_vmi_corrections.setText(QCoreApplication.translate("MainWindow", u"Apply correction", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_image_correction), QCoreApplication.translate("MainWindow", u"Image", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"r-squared", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Energies", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Calibration fit", None))
        self.label_pes_cal_constants.setText(QCoreApplication.translate("MainWindow", u"Cal. constant", None))
        self.label_cal_points.setText(QCoreApplication.translate("MainWindow", u"r-squared, energy", None))
        self.test_edit_cal_points.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0, 0</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_edit_cal_constant.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_ke_start.setText(QCoreApplication.translate("MainWindow", u"KE start", None))
        self.text_edit_ke_start.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_pes_constant_alpha.setText(QCoreApplication.translate("MainWindow", u"alpha", None))
        self.button_apply_pes_use_constants.setText(QCoreApplication.translate("MainWindow", u"Use constants", None))
        self.label_ke_end.setText(QCoreApplication.translate("MainWindow", u"KE end", None))
        self.label_ke_bins.setText(QCoreApplication.translate("MainWindow", u"KE bins", None))
        self.text_edit_ke_bins.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.button_apply_pes_calibration.setText(QCoreApplication.translate("MainWindow", u"Apply calibration", None))
        self.text_edit_ke_end.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_calibration), QCoreApplication.translate("MainWindow", u"Cal. (PES)", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Fore", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"Back", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"Subt", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Fore (m/q)", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Back (m/q)", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Subt (m/q)", None))
        self.button_auto_newest_folder_2.setText(QCoreApplication.translate("MainWindow", u"Auto newest folder", None))
        self.label_update_status_2.setText(QCoreApplication.translate("MainWindow", u"Update status:", None))
        self.test_display_folder_status_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Stay</p></body></html>", None))
        self.button_stay_current_folder_2.setText(QCoreApplication.translate("MainWindow", u"Stay current folder", None))
        self.button_fetch_new_files_2.setText(QCoreApplication.translate("MainWindow", u"Fetch new files", None))
        self.text_display_update_status_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Stopped</p></body></html>", None))
        self.label_folder_status_2.setText(QCoreApplication.translate("MainWindow", u"Folder status:", None))
        self.button_stop_fetch_2.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.combobox_tof_yscale.setItemText(0, QCoreApplication.translate("MainWindow", u"Linear", None))
        self.combobox_tof_yscale.setItemText(1, QCoreApplication.translate("MainWindow", u"Log", None))

        self.label_current_folder_2.setText(QCoreApplication.translate("MainWindow", u"Current folder", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tof_main), QCoreApplication.translate("MainWindow", u"TOF main", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"TOF", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Mass/Charge", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Calibration fit", None))
        self.text_edit_tof_end.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.button_apply_tof_calibration.setText(QCoreApplication.translate("MainWindow", u"Apply calibration", None))
        self.label_tof_constant_t0.setText(QCoreApplication.translate("MainWindow", u"t0", None))
        self.text_edit_tof_cal_points.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0, 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1, 1</p></body></html>", None))
        self.text_edit_tof_constant_c.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_edit_tof_constant_t0.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_tof_cal_points.setText(QCoreApplication.translate("MainWindow", u"TOF, m/q", None))
        self.label_tof_constant_c.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.text_edit_mq_bins.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_edit_mq_start.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_tof_end.setText(QCoreApplication.translate("MainWindow", u"TOF end", None))
        self.label_mq_start.setText(QCoreApplication.translate("MainWindow", u"m/q start", None))
        self.button_apply_tof_use_constants.setText(QCoreApplication.translate("MainWindow", u"Use constants", None))
        self.label_tof_bins.setText(QCoreApplication.translate("MainWindow", u"TOF bins", None))
        self.label_tof_constants.setText(QCoreApplication.translate("MainWindow", u"Cal. constants", None))
        self.text_edit_mq_end.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_edit_tof_bins.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_mq_end.setText(QCoreApplication.translate("MainWindow", u"m/q end", None))
        self.label_mq_bins.setText(QCoreApplication.translate("MainWindow", u"m/q bins", None))
        self.label_tof_start.setText(QCoreApplication.translate("MainWindow", u"TOF start", None))
        self.text_edit_tof_start.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tof_calibration), QCoreApplication.translate("MainWindow", u"Cal. (TOF)", None))
        self.label_search_dir_for_newest_folder.setText(QCoreApplication.translate("MainWindow", u"Auto-search newest folder in directory", None))
        self.label_extract_tof_start.setText(QCoreApplication.translate("MainWindow", u"TOF read start", None))
        self.text_edit_extract_tof_start.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_extract_tof_stop.setText(QCoreApplication.translate("MainWindow", u"TOF read stop", None))
        self.text_edit_extract_tof_stop.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.box_slu_parity.setText("")
        self.label_slu_parity.setText(QCoreApplication.translate("MainWindow", u"SLU@25Hz parity flip", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Cache settings", None))
        self.label_files_per_cache.setText(QCoreApplication.translate("MainWindow", u"Files per cache", None))
        self.text_edit_files_per_cache.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None))
        self.box_make_cache.setText("")
        self.label_settings_make_cache.setText(QCoreApplication.translate("MainWindow", u"Make cache", None))
        self.box_load_from_cache.setText("")
        self.label_setting_load_from_cache.setText(QCoreApplication.translate("MainWindow", u"Load from cache", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Foreground/Background definitions", None))
        self.label_fore.setText(QCoreApplication.translate("MainWindow", u"Fore", None))
        self.label_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.box_fore_felonsluon.setText("")
        self.box_back_felonsluon.setText("")
        self.label_felonsluon.setText(QCoreApplication.translate("MainWindow", u"FEL: on, SLU: on", None))
        self.box_fore_felonsluoff.setText("")
        self.box_back_felonsluoff.setText("")
        self.label_felonsluoff.setText(QCoreApplication.translate("MainWindow", u"FEL: on, SLU: off", None))
        self.box_fore_feloffsluon.setText("")
        self.box_back_feloffsluon.setText("")
        self.label_feloffsluon.setText(QCoreApplication.translate("MainWindow", u"FEL: off, SLU: on", None))
        self.box_fore_feloffsluoff.setText("")
        self.box_back_feloffsluoff.setText("")
        self.lafel_feloffsluon.setText(QCoreApplication.translate("MainWindow", u"FEL: off, SLU: off", None))
        self.box_flip_feloffsluon.setText("")
        self.box_flip_felonsluon.setText("")
        self.label_back_2.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.box_flip_felonsluoff.setText("")
        self.box_flip_feloffsluoff.setText("")
        self.applyChangesSettings.setText(QCoreApplication.translate("MainWindow", u"Apply changes", None))
        self.label_abel_inversion_data_path.setText(QCoreApplication.translate("MainWindow", u"Abel inversion data file", None))
        self.label_subfolder_extension.setText(QCoreApplication.translate("MainWindow", u"subfolder extension", None))
        self.text_edit_subfolder_extension.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">rawdata</p></body></html>", None))
        self.label_subfolder_extension_2.setText(QCoreApplication.translate("MainWindow", u"./", None))
        self.text_edit_num_cores.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.label_num_cores.setText(QCoreApplication.translate("MainWindow", u"Num. cores for multiprocess", None))
        self.label_max_cores.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.label_search_dir_for_newest_folder_2.setText(QCoreApplication.translate("MainWindow", u"Auto-search regex", None))
        self.label_tof_baseline_points.setText(QCoreApplication.translate("MainWindow", u"TOF baseline points", None))
        self.text_edit_tof_baseline_points.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuFERMI_On_line_analysis_tool.setTitle(QCoreApplication.translate("MainWindow", u"FERMI LDM On-line analysis tool", None))
    # retranslateUi







        try:
            CURRENT_SCRIPT_DIR = str(pathlib.Path(__file__).parent.resolve())
        except NameError:  # this will happen in .ipynb files
            print('not found...?')
            CURRENT_SCRIPT_DIR = os.path.abspath('')
        
        top_level_dir = resolve_path(CURRENT_SCRIPT_DIR, '..')
        print('top level dir is: ', top_level_dir)

        self.box_fore_felonsluon.setChecked(True)
        self.box_back_felonsluoff.setChecked(True)
        self.text_edit_search_dir_for_newest_folder.setText(f'{top_level_dir}/tests/_temp/TestBeamtime/Beamtime')
        self.text_edit_ke_start.setText('')
        self.text_edit_ke_end.setText('')
        self.text_edit_ke_bins.setText('')
        self.text_edit_tof_start.setText('')
        self.text_edit_tof_end.setText('')
        self.text_edit_num_cores.setText('8')
        self.box_pes.setChecked(True)
        self.text_edit_files_per_cache.setText('4')
        # self.text_edit_tof_cal_points.setText('0, 0\n1, 1')
        self.text_edit_tof_cal_points.setText('5000, 0\n10600, 14\n13000, 28')
        self.text_browser_max_cores.setText(str(os.cpu_count()))
        self.test_edit_cal_points.setText('0,0\n2500,1')

        look_in_dir = resolve_path(CURRENT_SCRIPT_DIR, '..')
        list_of_files = os.listdir(look_in_dir)

        matches = np.argwhere(np.array([True if re.match(r'G_r.*\.h5', file) else False for file in list_of_files]))
        if len(matches) > 0:
            match_filename = f'{look_in_dir}/{list_of_files[matches[0][0]]}'
        else:
            match_filename = ''
        # self.text_edit_abel_inversion_data_path.setText(f'{top_level_dir}/examples/G_r225_k57_l4_half.h5')
        self.text_edit_abel_inversion_data_path.setText(match_filename)
        self.text_edit_tof_baseline_points.setText('1000')
        self.text_edit_search_regex.setText(r'Run_(\d+)')
        self.text_edit_show_rings.setText('2, 150, 300')

    
    def __init__(self):
        self.background_key = True
        self.terminal_print = True
        self.status = {
            'num_cores' : 1,
            'auto_newest_folder' : False, 
            'fetch_new_files' : False,
            'search_in_directory' : '',
            'files_per_cache' : None,
            'make_cache' : False,
            'load_from_cache' : False,
            'current_files' : [],
            'current_folder' : '',
            'print_list' : [],
            'subfolder_extension' : '',
            'background_process_active' : False,
            'gdata_filepath' : '',
            'tof_baseline_points' : 0,
        }

        self.flags = {
            'changed_gdata_filepath' : False,
            'changed_gdata' : False,  # not implemented yet!
        }

        self._vmi_shape = (1, 1)
        self._image_vmi_shape = (1, 1)
        self._image_small_vmi_shape = (1, 1)
        self.graph_data = {
            'vmi_fore' : np.array([[np.nan,],], dtype=float),
            'vmi_back' : np.array([[np.nan,],], dtype=float),
            'vmi_subt' : np.array([[np.nan,],], dtype=float),
            'vmi_raw' : np.array([[np.nan,],], dtype=float),
            'vmi_corr' : np.array([[np.nan,],], dtype=float),
            'vmi_reduced' : np.array([[np.nan,],], dtype=float),
            'vmi_inverse' : np.array([[np.nan,],], dtype=float),
            'vmi_fit' : np.array([[np.nan,],], dtype=float),
            # 'pes_subt' : [np.array([]), np.array([])],
            'pes_subt' : [np.array([]), np.array([])],
            'betas' : [np.array([]), np.zeros(shape=(0,4))],
            'radial' : np.array([]),
            'rsquare' : np.array([]),
            'subt_rdf' : [np.array([]), np.array([])],
            # 'subt_rsdf' : [np.array([]), np.array([])],
            'subt_rsdf' : [np.array([0,]), np.array([0,])],
            'tof_start' : None,
            'tof_end' : None,
            'tof_bins' : None,
            'tof_fore' : [np.array([]), np.array([])],
            'tof_back' : [np.array([]), np.array([])],
            'tof_subt' : [np.array([]), np.array([])],
            'new_tof_fore' : [np.array([]), np.array([])],
            'new_tof_back' : [np.array([]), np.array([])],
            'new_tof_subt' : [np.array([]), np.array([])],
            'mq_fore' : [np.array([]), np.array([])],
            'mq_back' : [np.array([]), np.array([])],
            'mq_subt' : [np.array([]), np.array([])],
            'new_mq_fore' : [np.array([]), np.array([])],
            'new_mq_back' : [np.array([]), np.array([])],
            'new_mq_subt' : [np.array([]), np.array([])],
            'mq_start' : None,
            'mq_end' : None,
            'mq_bins' : None,
            'ring_guide' : [np.array([]), np.array([])],
        }
        
        self.image_correction_data = {
            'center' : (None, None),
            'zoom' : (1, 1),
            'rotate' : 0,
            'reduce_size' : None,
            'show_ellipticity' : False,
        }

        self.calibration_data = {
            'tof_mq_points' : np.array([[],[]]),
            'tof_mq_model' : np.array([[],[]]),
            'rsquare_ke_points' : np.array([[],[]]),
            'rsquare_ke_model' : np.array([[],[]]),
        }

        self.pes_calibration_constant = 1
        self.ion_tof_calibration_constants = (0, 1)

        self.run = Run([])
        self.run.num_cores = self.status['num_cores']

        self.threadpool = QThreadPool()
        if self.terminal_print: print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.vmi_data = np.zeros(shape=(4,0,0))
        self.tof_data = np.zeros(shape=(1)), np.zeros(shape=(4,1))
        self.mq_data = np.zeros(shape=(1,)), np.zeros(shape=(4,1))
        self.default_vmi_data = np.zeros(shape=(4,0,0))
        self.default_tof_data = np.zeros(shape=(1)), np.zeros(shape=(4,1))
        self.default_mq_data = np.zeros(shape=(1,)), np.zeros(shape=(4,1))
        self.gdata = None
        self.betas = [] # the existent beta values from gdata

    def setup_signals(self):
        self.button_auto_newest_folder.clicked.connect(self.click_auto_newest_folder)
        self.button_stay_current_folder.clicked.connect(self.click_stay_folder)
        self.button_fetch_new_files.clicked.connect(self.click_fetch_new_files)
        self.button_stop_fetch.clicked.connect(self.click_stop_fetch)
        self.button_auto_newest_folder_2.clicked.connect(self.click_auto_newest_folder)
        self.button_stay_current_folder_2.clicked.connect(self.click_stay_folder)
        self.button_fetch_new_files_2.clicked.connect(self.click_fetch_new_files)
        self.button_stop_fetch_2.clicked.connect(self.click_stop_fetch)
        self.box_pes.toggled.connect(self.update_pes_window)
        self.box_beta1.toggled.connect(self.update_pes_window)
        self.box_beta2.toggled.connect(self.update_pes_window)
        self.box_beta3.toggled.connect(self.update_pes_window)
        self.box_beta4.toggled.connect(self.update_pes_window)
        self.box_slu_parity.toggled.connect(self.update_main_vmi_window)
        self.button_apply_tof_calibration.clicked.connect(self.update_main_tof_window)
        self.applyChangesSettings.clicked.connect(self.apply_settings)
        self.box_make_cache.toggled.connect(self.apply_settings)
        self.box_load_from_cache.toggled.connect(self.apply_settings)
        self.combobox_tof_yscale.currentIndexChanged.connect(self.redraw_tof_data) # still need to do
        self.button_apply_vmi_corrections.clicked.connect(self.process_redraw_vmi_data)
        self.button_apply_pes_calibration.clicked.connect(self.update_pes_calibration_window)
        # self.text_edit_current_folder.textChanged.connect(self.change_folder)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data_if_change)

        self.background_process_timer = QTimer()
        self.background_process_timer.timeout.connect(self.check_background_process_status)
    
    def check_background_process_status(self):
        raise NotImplementedError
        
    def resume_timer(self):
        self.timer.start(2000)
    def stop_timer(self):
        self.timer.stop()
        

    def change_folder(self):
        current_folder = self.status['current_folder']
        if (look_folder := self.text_edit_current_folder.toPlainText()) != current_folder:
            new_folder = look_folder
        elif (look_folder := self.text_edit_current_folder_2.toPlainText()) != current_folder:
            new_folder = look_folder
        else: 
            new_folder = current_folder
        self.status['current_folder'] = new_folder
        self.text_edit_current_folder.setText(new_folder)
        self.text_edit_current_folder_2.setText(new_folder)
        
    def apply_settings(self):
        """ get all the settings from the settings tab"""
        self.status['num_cores'] = int(self.text_edit_num_cores.toPlainText())
        self.status['files_per_cache'] = int(self.text_edit_files_per_cache.toPlainText())
        self.status['search_in_directory'] = self.text_edit_search_dir_for_newest_folder.toPlainText()
        self.status['subfolder_extension'] = self.text_edit_subfolder_extension.toPlainText()
        self.status['gdata_filepath'] = self.text_edit_abel_inversion_data_path.toPlainText()
        self.status['make_cache'] = self.box_make_cache.isChecked()
        self.status['load_from_cache'] = self.box_load_from_cache.isChecked()
        self.status['tof_baseline_points'] = int(self.text_edit_tof_baseline_points.toPlainText())
        self.status['search_regex'] = self.text_edit_search_regex.toPlainText()

        time_string = strftime("%Y-%m-%d %H:%M:%S", localtime())
        self.update_print_box(f'{time_string}: settings applied')

        self.redraw_tof_data()
        self.redraw_vmi_data()
        
    def get_newest_folder(self):
        main_directory = self.status['search_in_directory']
        try:
            list_of_folders = os.listdir(main_directory)
        except FileNotFoundError:
            if self.terminal_print: print(f'search_in_directory ({main_directory}) cannot be found')
            list_of_folders = []
        number_rule = self.status['search_regex']
        # number_rule_re = re.compile(r'\d+')
        number_rule_re = re.compile(number_rule)

        numbered_folders = [name for name in list_of_folders if number_rule_re.search(name)]
        if len(numbered_folders) > 0:
            numbers = np.array([number_rule_re.search(name).group(1) for name in numbered_folders], dtype=int)
            max_index = np.argmax(numbers)
            highest_numbered_folder = numbered_folders[max_index]
        else:
            highest_numbered_folder = ''
        folderpath = f'{main_directory}/{highest_numbered_folder}'
        return folderpath
    
    def update_print_box(self, message, message_limit=20):
        if len(self.status['print_list']) > message_limit:
            self.status['print_list'] = self.status['print_list'][1:] + [message,]
        else:
            self.status['print_list'] = self.status['print_list'] + [message,]
        joined_text = '\n'.join(self.status['print_list'])
        self.print_browser.setText(joined_text)
        QApplication.processEvents()

    def check_filechange(self):
        if self.status['auto_newest_folder']:
            current_folder = self.status['current_folder']
            newest_folder = self.get_newest_folder()
            if current_folder != newest_folder:
                time_string = strftime("%Y-%m-%d %H:%M:%S", localtime())
                if self.terminal_print: print(f'{time_string}: new folder found ({newest_folder})')
                self.update_print_box(f'{time_string}: new folder found ({newest_folder})')
                self.status['current_folder'] = newest_folder
                self.text_edit_current_folder.setText(newest_folder)
                self.text_edit_current_folder_2.setText(newest_folder)
                # self.text_edit_current_folder.setReadOnly(True)
        else:
            self.change_folder()

        sorted_found_files = self.get_filechange()
        if sorted_found_files is None:
            return False
        if sorted_found_files == sorted(self.status['current_files']):
            return False
        return True

    def get_filechange(self):
        current_folder = self.status['current_folder']
        subfolder_ext = self.status['subfolder_extension']
        look_in_folder = f'{current_folder}/{subfolder_ext}'
        try:
            found_files = os.listdir(look_in_folder)
        except FileNotFoundError:
            time_string = strftime("%Y-%m-%d %H:%M:%S", localtime())
            print_message = f'{time_string}: file location ({look_in_folder}) does not exist, no update.'
            self.update_print_box(print_message)
            if self.terminal_print: print(print_message)
            return None
        return sorted(found_files)

    def update_filechange(self):
        self.status['current_files'] = self.get_filechange()
        self.text_browser_files.setText('\n'.join([filename[-20:] for filename in self.status['current_files']][::-1]))
        self.text_browser_num_files.setText(str(len(self.status['current_files'])))

    def update_data_if_change(self):
        time_string = strftime("%Y-%m-%d %H:%M:%S", localtime())
        if self.check_filechange() and not self.background_key:
            num_files = len(self.get_filechange())
            if self.terminal_print: print(f'{time_string}: new files found ({num_files}), but background process unfinished. Nothing done.')
            self.update_print_box(f'{time_string}: new files found ({num_files}), but background process unfinished. Nothing done.')

        elif self.check_filechange() and self.background_key:
            num_files = len(self.get_filechange())
            self.update_print_box(f'{time_string}: new files found ({num_files}), updating')
            if self.terminal_print: print(f'{time_string}: new files found ({num_files}), updating')

            self.update_filechange()
            self.update_data()
        else:
            if self.terminal_print: print('no change in files...')

    def get_new_vmi_data(self):
        @set_recursion_limit(1)
        def keyword_functions(keyword, aliasFunc, DictionaryObject):
            return DictionaryObject[aliasFunc(keyword)]
        alias_dict = {
            'vmi' : 'vmi/andor',
            'ion_tof' : 'digitizer/channel1',
            'slu' : 'user_laser/energy_meter/Energy2',
            }
        folderpath = self.status['current_folder'] + '/rawdata'
        filepaths = [folderpath+'/'+filename for filename in os.listdir(folderpath)[::]]
        self.run = MultithreadRun(filepaths,
            alias_dict=alias_dict, search_symbols=search_symbols,
            keyword_functions=keyword_functions)
        self.run.num_cores = self.status['num_cores']

        try:
            back_sep = True
            slu_sep = True
            make_cache = self.status['make_cache']
            load_from_cache = self.status['load_from_cache']
            num_files_per_cache = self.status['files_per_cache']

            vmi_data = self.run.average_run_data('vmi', 
                back_sep=back_sep, slu_sep=slu_sep, make_cache=make_cache,
                num_files_per_cache=num_files_per_cache, use_cache=load_from_cache)

        except (FileNotFoundError, OSError, IndexError) as e:
            # this is a race condition, where h5py is trying to open a file that is currently being written into
            # easiest solution is to wait for the next update
            if self.terminal_print: print("Can't open VMI here! Returning None")
            print("Error message: ", e)
            # vmi_data = self.vmi_data
            vmi_data = self.default_vmi_data
            return vmi_data
        # vmi_data = simplify_data(vmi_data, single_run=True, single_rule=True)
        vmi_data = [data[0] for data in vmi_data]
        self.vmi_data = vmi_data
        return vmi_data

    def get_new_tof_data(self):
        @set_recursion_limit(1)
        def keyword_functions(keyword, aliasFunc, DictionaryObject):
            return DictionaryObject[aliasFunc(keyword)]
        alias_dict = {
            'vmi' : 'vmi/andor',
            'ion_tof' : 'digitizer/channel1',
            'slu' : 'user_laser/energy_meter/Energy2',
            }
        folderpath = self.status['current_folder'] + '/rawdata'
        filepaths = [folderpath+'/'+filename for filename in os.listdir(folderpath)[::]]
        self.run = Run(filepaths,
            alias_dict=alias_dict, search_symbols=search_symbols,
            keyword_functions=keyword_functions)
        self.run.num_cores = self.status['num_cores']

        try:
            back_sep = True
            slu_sep = True
            make_cache = self.status['make_cache']
            load_from_cache = self.status['load_from_cache']
            num_files_per_cache = self.status['files_per_cache']

            tof_signal = self.run.average_run_data('ion_tof', 
                back_sep=back_sep, slu_sep=slu_sep, make_cache=make_cache,
                num_files_per_cache=num_files_per_cache, use_cache=load_from_cache)
            tof_coor = np.arange(np.shape(tof_signal)[-1])
            tof_data = tof_coor, tof_signal

        except (FileNotFoundError, OSError, IndexError):
            # this is a race condition, where h5py is trying to open a file that is currently being written into
            # easiest solution is to wait for the next update
            if self.terminal_print: print("Can't open TOF data here! Returning None")
            # tof_data = self.tof_data
            tof_data = self.default_tof_data
            return tof_data
        # vmi_data = simplify_data(vmi_data, single_run=True, single_rule=True)

        tof_data = tof_data[0], [data[0] for data in tof_data[1]]
        self.tof_data = tof_data
        return tof_data
    

    def return_background_key_start_get_tof_data_in_worker(self):
        if self.background_key is False:
            self.background_key = True
        else:
            raise Exception(f'background key was duplicated (start_get_tof_data_in_worker)!')

    def return_background_key(self):
        if self.background_key is False:
            self.background_key = True
        else:
            raise Exception(f'background key was duplicated ({message})!')
    
    def borrow_background_key(self):
        if self.background_key is True:
            self.background_key = False
            return True
        else:
            return False
    
    def start_get_tof_data_in_worker(self):
        if DEBUG: print(f'stepped in start_get_tof_data_in_worker, background_key is {self.background_key}')
        if not self.borrow_background_key():
            print('background process running, cannot execute tof data retrieval!')
            return None
        if True:
            if DEBUG: print('getting tof data!')
            if DEBUG: print(f'DEBUG: expect background_key to be False ({self.background_key})')
            assert self.background_key == False
            worker = Worker(self.get_new_tof_data)
            worker.signals.finished.connect(self.return_background_key_start_get_tof_data_in_worker)
            worker.signals.finished.connect(self.process_redraw_tof_data)
            self.threadpool.start(worker)
        else:
            if DEBUG: print('not threading here')
            self.get_new_tof_data()
            self.process_redraw_tof_data()

    def combine_process_redraw_vmi_data_and_start_get_tof_data_in_worker(self):
        if DEBUG: print(f'DEBUG: expect background_key to be True ({self.background_key})')
        assert self.background_key == True
        self.start_get_tof_data_in_worker()
        if DEBUG: print('I got here!')
        self.process_redraw_vmi_data()
        # self.return_background_key()
        assert self.background_key == False
        if DEBUG: print(f'DEBUG: expect background_key to be False ({self.background_key})')

    def update_data(self, multithreading=True):

        if multithreading:  # complicated structure, because updating the GUI is NOT thread-safe!
            # i.e. the threaded processes must not touch the GUI elements
            if DEBUG: print(f'stepped in update_data, background_key is {self.background_key}')
            self.borrow_background_key()
            worker = Worker(self.get_new_vmi_data)
            worker.signals.finished.connect(self.return_background_key)
            worker.signals.finished.connect(self.combine_process_redraw_vmi_data_and_start_get_tof_data_in_worker)
            self.threadpool.start(worker)
        else:
            self.get_new_vmi_data()
            self.get_new_tof_data()
            self.redraw_canvasses()

    def set_image_correction_from_panel(self):
        xcenter_text = self.text_edit_correct_xcenter.toPlainText()
        if xcenter_text == '':
            xcenter = None
        else:
            xcenter = int(xcenter_text)
        ycenter_text = self.text_edit_correct_ycenter.toPlainText()
        if ycenter_text == '':
            ycenter = None
        else:
            ycenter = int(ycenter_text)
        self.image_correction_data['center'] = (xcenter, ycenter)
        # reversed, because cpbasex requires polarization axis along second axis i.e. transposed
        self.image_correction_data['center'] = (ycenter, xcenter)

        xzoom_text = self.text_edit_correct_xzoom.toPlainText()
        if xzoom_text == '':
            xzoom = 1
        else:
            xzoom = float(xzoom_text)
        yzoom_text = self.text_edit_correct_yzoom.toPlainText()
        if yzoom_text == '':
            yzoom = 1
        else:
            yzoom = float(yzoom_text)
        self.image_correction_data['zoom'] = (xzoom, yzoom)
        # reversed, because cpbasex requires polarization axis along second axis i.e. transposed
        self.image_correction_data['zoom'] = (yzoom, xzoom)

        rotate_text = self.text_edit_correct_rotate.toPlainText()
        if rotate_text == '':
            rotate = 0
        else:
            rotate = float(self.text_edit_correct_rotate.toPlainText())
        self.image_correction_data['rotate'] = rotate
        reduce_image_size_text = self.text_edit_reduce_image_size.toPlainText()
        if reduce_image_size_text == '':
            reduce_image_size = None
        else:
            reduce_image_size = int(reduce_image_size_text)
        if reduce_image_size is None and self.gdata_size is not None:
            reduce_image_size = self.gdata_size
        self.image_correction_data['reduce_size'] = reduce_image_size

    def remake_vmi_data(self):
        # VMI section
        vmi_data = self.vmi_data  # obtained through the self.get_new_vmi_data() method
        if self.box_slu_parity.isChecked():
            vmi_felon_sluoff, vmi_felon_sluon, vmi_feloff_sluoff, vmi_feloff_sluon = (data for data in vmi_data)
        else:
            vmi_felon_sluon, vmi_felon_sluoff, vmi_feloff_sluon, vmi_feloff_sluoff = (data for data in vmi_data)

        vmi_fore = (
            (-1)**self.box_flip_felonsluon.isChecked() * self.box_fore_felonsluon.isChecked() * vmi_felon_sluon
            + (-1)**self.box_flip_felonsluoff.isChecked() * self.box_fore_felonsluoff.isChecked() * vmi_felon_sluoff
            + (-1)**self.box_flip_feloffsluon.isChecked() * self.box_fore_feloffsluon.isChecked() * vmi_feloff_sluon
            + (-1)**self.box_flip_feloffsluoff.isChecked() * self.box_fore_feloffsluoff.isChecked() * vmi_feloff_sluoff
        )
        vmi_back = (
            (-1)**self.box_flip_felonsluon.isChecked() * self.box_back_felonsluon.isChecked() * vmi_felon_sluon
            + (-1)**self.box_flip_felonsluoff.isChecked() * self.box_back_felonsluoff.isChecked() * vmi_felon_sluoff
            + (-1)**self.box_flip_feloffsluon.isChecked() * self.box_back_feloffsluon.isChecked() * vmi_feloff_sluon
            + (-1)**self.box_flip_feloffsluoff.isChecked() * self.box_back_feloffsluoff.isChecked() * vmi_feloff_sluoff
        )
        vmi_subt = vmi_fore - vmi_back
        self.graph_data['vmi_fore'] = vmi_fore
        self.graph_data['vmi_back'] = vmi_back
        self.graph_data['vmi_subt'] = vmi_subt
        
        self.image_correction_data['show_ellipticity'] = self.box_ring_ellipticity.isChecked()

        ### VMI INVERSION PLACE

        half_filter = [True, True]
        

        reduce_image_size = self.image_correction_data['reduce_size']
        if reduce_image_size is None:
            reduce_image_size = self.gdata_size
        raw_image_size = vmi_subt.shape[0]
        
        raw_vmi_center = self.image_correction_data['center']
        vmi_center = list(raw_vmi_center)
        if raw_vmi_center[0] is None:
            vmi_center[0] = int(raw_image_size//2)
        if vmi_center[1] is None:
            vmi_center[1] = int(raw_image_size//2)
        vmi_center = tuple(vmi_center)

        raw_vmi_zoom = self.image_correction_data['zoom']
        vmi_zoom = list(raw_vmi_zoom)
        vmi_zoom = tuple(vmi_zoom)
        
        vmi_rotation = self.image_correction_data['rotate']

        corrected = stretch(rotate(center_image(vmi_subt, vmi_center), vmi_rotation), vmi_zoom)
        vmi = resize(corrected, (reduce_image_size, reduce_image_size), axis=(0,1))
        folded = foldHalf(vmi, half_filter=half_filter)
        # resized = resizeFoldedHalf(folded, 225)
        resized = folded


        self.graph_data['vmi_raw'] = vmi_subt
        self.graph_data['vmi_corr'] = corrected
        self.graph_data['vmi_reduced'] = vmi

        if self.gdata is None: 
            gData = loadG(self.status['gdata_filepath'], make_images=True)
            self.gdata = gData
            self.betas = gData['l']

        if self.valid_inversion_condition():


            out = cpbasex_energy_inversion(resized, self.gdata, make_images=True, shape='half')
            try:
                inv = out['inv'][:,:]/2
            except KeyError:
                inv = vmi * np.nan
            try:
                fit = out['fit'][:,:]/2
            except KeyError:
                fit = vmi * np.nan

            rsquare = out['E']
            rsquare_spectrum = out['IE']
            betas = out['betas']

            slope = self.pes_calibration_constant
            rsquare_to_energy = lambda x: slope * x
            energies = rsquare_to_energy(rsquare)
            pes = rsquare_spectrum / slope # jacobian correction
            radial = self.gdata['x']
            rdf = pes * 2/radial  # radial distirubtion function w/ jacobian correction

            self.graph_data['radial'] = radial
            self.graph_data['subt_rdf'] = radial, rdf
            self.graph_data['subt_rsdf'] = rsquare, pes
            # self.graph_data['pes_subt'] = energies, pes
            self.graph_data['betas'] = rsquare, betas
            self.graph_data['vmi_inverse'] = inv
            self.graph_data['vmi_fit'] = fit
            
        xcenter, ycenter = self.image_correction_data['center']
        if xcenter is None: xcenter = np.shape(self.graph_data['vmi_raw'])[0]/2
        if ycenter is None: ycenter = np.shape(self.graph_data['vmi_raw'])[1]/2
        ring_radii = np.array(re.sub(' ', '', self.text_edit_show_rings.toPlainText()).split(','), dtype=float)
        t = np.linspace(0, 2*np.pi, num=1000)
        if self.image_correction_data['show_ellipticity']:
            xe, ye = self.image_correction_data['zoom']
            if xe is None: xe = 1
            if ye is None: ye = 1
        else:
            xe, ye = 1, 1
        x_ring = np.concatenate([np.concatenate((xcenter + 1/xe * radius * np.cos(t), [np.nan,])) for radius in ring_radii], dtype=float)
        y_ring = np.concatenate([np.concatenate((ycenter + 1/ye * radius * np.sin(t), [np.nan,])) for radius in ring_radii], dtype=float)
        self.graph_data['ring_guide'] = x_ring, y_ring
        self.graph_data['ring_guide'] = y_ring, x_ring  # transposed, because of cpbasex.


    def process_redraw_vmi_data(self):
        self.load_gdata()
        self.set_image_correction_from_panel()

        if True: # this is what I want, but if I do this, the TOF portion won't run?
            worker = Worker(self.remake_vmi_data)
            # worker.signals.finished.connect(self.redraw_vmi_data)
            worker.signals.finished.connect(self.worker_redraw_vmi_data)
            self.threadpool.start(worker)
        else:
            self.remake_vmi_data()
            self.redraw_vmi_data()

    def worker_redraw_vmi_data(self):
        worker = Worker(self.redraw_vmi_data)
        worker.signals.finished.connect(self.change_pes_calibration_constants)
        self.threadpool.start(worker)
        

    def redraw_vmi_data(self):
        
        time_start = time.time()
        self.update_pes_window()
        self.update_main_vmi_window()
        self.update_image_window()
        time_end = time.time()
        print('time elapsed (redraw_vmi_data): ', time_end-time_start)
        
    def load_gdata(self):
        if (self.gdata is None) or self.flags['changed_gdata_filepath']: 
            try:
                gData_filepath = self.status['gdata_filepath']
                gData = loadG(self.status['gdata_filepath'], make_images=True)
                self.gdata = gData
                self.betas = gData['l']
                Nx = len(gData['x'])
                image_size = Nx * 2
                self.gdata_size = image_size
                self.text_browser_gdata_image_size.setText(str(self.gdata_size))
                if self.image_correction_data['reduce_size'] is None:
                    self.image_correction_data['reduce_size'] = self.gdata_size
            except OSError:
                time_string = strftime("%Y-%m-%d %H:%M:%S", localtime())
                self.update_print_box(f'{time_string}: Could not found inversion data ({gData_filepath})')
                return None
        self.flags['changed_gdata'] = True
        
    
    def valid_inversion_condition(self):
        
        reduce_size_matches_gdata =  self.gdata_size == self.image_correction_data['reduce_size']
        return reduce_size_matches_gdata
    
    def update_main_tof_window(self):
        self.process_redraw_tof_data()

    def process_redraw_tof_data(self):
        if DEBUG: print('process redrawing tof data')
        if DEBUG: print(f'DEBUG: expect background_key to be True ({self.background_key})')
        assert self.background_key == True
        self.change_ion_tof_calibration_constants()
        worker = Worker(self.remake_tof_data)
        worker.signals.finished.connect(self.worker_redraw_tof_data)
        self.threadpool.start(worker)
    
    def remake_tof_data(self):

        if DEBUG: print('remake tof data')
        # TOF section

        tof_coor, tof_data = self.tof_data  # obtained through the self.get_new_tof_data() method
        if self.box_slu_parity.isChecked():
            tof_felon_sluoff, tof_felon_sluon, tof_feloff_sluoff, tof_feloff_sluon = tof_data
        else:
            tof_felon_sluon, tof_felon_sluoff, tof_feloff_sluon, tof_feloff_sluoff = tof_data

        tof_fore = -(
            (-1)**self.box_flip_felonsluon.isChecked() * self.box_fore_felonsluon.isChecked() * tof_felon_sluon
            + (-1)**self.box_flip_felonsluoff.isChecked() * self.box_fore_felonsluoff.isChecked() * tof_felon_sluoff
            + (-1)**self.box_flip_feloffsluon.isChecked() * self.box_fore_feloffsluon.isChecked() * tof_feloff_sluon
            + (-1)**self.box_flip_feloffsluoff.isChecked() * self.box_fore_feloffsluoff.isChecked() * tof_feloff_sluoff
        )
        tof_back = -(
            (-1)**self.box_flip_felonsluon.isChecked() * self.box_back_felonsluon.isChecked() * tof_felon_sluon
            + (-1)**self.box_flip_felonsluoff.isChecked() * self.box_back_felonsluoff.isChecked() * tof_felon_sluoff
            + (-1)**self.box_flip_feloffsluon.isChecked() * self.box_back_feloffsluon.isChecked() * tof_feloff_sluon
            + (-1)**self.box_flip_feloffsluoff.isChecked() * self.box_back_feloffsluoff.isChecked() * tof_feloff_sluoff
        )
        
        Nbaseline = self.status['tof_baseline_points']
        baseline = np.average(tof_fore[:Nbaseline])
        tof_fore -= baseline
        tof_back -= baseline

        tof_subt = tof_fore - tof_back
        self.graph_data['tof_fore'] = tof_coor, tof_fore
        self.graph_data['tof_back'] = tof_coor, tof_back
        self.graph_data['tof_subt'] = tof_coor, tof_subt

        
        self.remake_mq_data()
    
    @staticmethod
    def string_to_pairs(string, dtype=str):
        string = re.sub(' ', '', string)
        pairs = string.split('\n')
        pairs = [item for item in pairs if item != '']
        output_pairs = []
        for pair in pairs:
            output_pairs.append(list(pair.split(',')))
        output_pairs = np.array(output_pairs, dtype=dtype)
        return output_pairs


    def remake_mq_data(self):
    
        # perform calibration here!

        cal_points_string = self.text_edit_tof_cal_points.toPlainText()
        ion_tof_mq_peaks = self.string_to_pairs(cal_points_string, dtype=float)
        tof_points, mq_points = ion_tof_mq_peaks.T


        ion_calibration_dict = tof_mq_calibration(peaks=ion_tof_mq_peaks)
        (_, _, _, _, ion_constants_dict) = list(ion_calibration_dict.values())
        ion_constants = ion_constants_dict['timezero'], ion_constants_dict['C']
        tof_mq_coor_func = lambda tof: tof_mq_coordinate_func(tof, *ion_constants)
        tof_to_mq = lambda tof, spec, axis=None: tof_to_mq_conversion(tof, spec, *ion_constants, axis=axis)
        
        self.ion_tof_calibration_constants = ion_constants

        tof_coor, tof_subt = self.graph_data['tof_subt']
        if len(tof_points) > 0:
            tof_model = np.linspace(
                np.min(np.concatenate((tof_points, tof_coor))), 
                np.max(np.concatenate((tof_points, tof_coor))), 
                num=1000)
        mq_model = tof_mq_coor_func(tof_model)
        self.calibration_data['tof_mq_points'] = tof_points, mq_points
        self.calibration_data['tof_mq_model'] = tof_model, mq_model

        mq_raw_coor, mq_raw_subt = tof_to_mq(tof_coor, tof_subt)
        mq_start, mq_end, mq_bins = self.get_mq_lim_data(tof_mq_coor_func(tof_coor))

        mq_coor = np.linspace(mq_start, mq_end, num=mq_bins)
        if len(mq_raw_coor) < 2:
            mq_coor = np.array([])
            mq_subt = np.array([])
        else:
            mq_subt = rebinning(mq_coor, mq_raw_coor, mq_raw_subt)

        self.graph_data['mq_subt'] = mq_coor, mq_subt

        mq_raw_coor, mq_raw_fore = tof_to_mq(*self.graph_data['tof_fore'])
        mq_start, mq_end, mq_bins = self.get_mq_lim_data(tof_mq_coor_func(tof_coor))
        mq_coor = np.linspace(mq_start, mq_end, num=mq_bins)
        if len(mq_raw_coor) < 2:
            mq_coor = np.array([])
            mq_fore = np.array([])
        else:
            mq_fore = rebinning(mq_coor, mq_raw_coor, mq_raw_fore)
            
        mq_raw_coor, mq_raw_back = tof_to_mq(*self.graph_data['tof_back'])
        mq_start, mq_end, mq_bins = self.get_mq_lim_data(tof_mq_coor_func(tof_coor))
        mq_coor = np.linspace(mq_start, mq_end, num=mq_bins)
        if len(mq_raw_coor) < 2:
            mq_coor = np.array([])
            mq_back = np.array([])
        else:
            mq_back = rebinning(mq_coor, mq_raw_coor, mq_raw_back)

        mq_raw_coor, mq_raw_subt = tof_to_mq(*self.graph_data['tof_subt'])
        mq_start, mq_end, mq_bins = self.get_mq_lim_data(tof_mq_coor_func(tof_coor))
        mq_coor = np.linspace(mq_start, mq_end, num=mq_bins)
        if len(mq_raw_coor) < 2:
            mq_coor = np.array([])
            mq_subt = np.array([])
        else:
            mq_subt = rebinning(mq_coor, mq_raw_coor, mq_raw_subt)

        self.graph_data['mq_fore'] = mq_coor, mq_fore
        self.graph_data['mq_back'] = mq_coor, mq_back
        self.graph_data['mq_subt'] = mq_coor, mq_subt
        
    
        tof_start, tof_end, tof_bins = self.get_tof_lim_data()
        new_tof_coor = np.linspace(tof_start, tof_end, num=tof_bins)
        with IgnoreWarnings("length one"):
            new_tof_fore = rebinning(new_tof_coor, *self.graph_data['tof_fore'])
            new_tof_back = rebinning(new_tof_coor, *self.graph_data['tof_back'])
            new_tof_subt = rebinning(new_tof_coor, *self.graph_data['tof_subt'])
            
        self.graph_data['new_tof_fore'] = new_tof_coor, new_tof_fore
        self.graph_data['new_tof_back'] = new_tof_coor, new_tof_back
        self.graph_data['new_tof_subt'] = new_tof_coor, new_tof_subt

        mq_start, mq_end, mq_bins = self.get_mq_lim_data(self.graph_data['mq_subt'][0])
        new_mq_coor = np.linspace(mq_start, mq_end, num=mq_bins)
        with IgnoreWarnings("length one"):
            new_mq_fore = rebinning(new_mq_coor, *self.graph_data['mq_fore'])
            new_mq_back = rebinning(new_mq_coor, *self.graph_data['mq_back'])
            new_mq_subt = rebinning(new_mq_coor, *self.graph_data['mq_subt'])

        self.graph_data['new_mq_fore'] = new_mq_coor, new_mq_fore
        self.graph_data['new_mq_back'] = new_mq_coor, new_mq_back
        self.graph_data['new_mq_subt'] = new_mq_coor, new_mq_subt


    def worker_redraw_tof_data(self):
        worker = Worker(self.redraw_tof_data)
        self.threadpool.start(worker)
        
    def redraw_tof_data(self):
        time_start = time.time()

        new_tof_coor, new_tof_fore = self.graph_data['new_tof_fore']
        new_tof_coor, new_tof_back = self.graph_data['new_tof_back']
        new_tof_coor, new_tof_subt = self.graph_data['new_tof_subt']
        new_mq_coor, new_mq_fore = self.graph_data['new_mq_fore']
        new_mq_coor, new_mq_back = self.graph_data['new_mq_back']
        new_mq_coor, new_mq_subt = self.graph_data['new_mq_subt']

        self._line_fore_tof.set_data(new_tof_coor, new_tof_fore)
        self._line_back_tof.set_data(new_tof_coor, new_tof_back)
        self._line_subt_tof.set_data(new_tof_coor, new_tof_subt)
        yscale = self.combobox_tof_yscale.currentText().lower()
        self._fore_tof_ax.set_yscale(yscale)
        self._back_tof_ax.set_yscale(yscale)
        self._subt_tof_ax.set_yscale(yscale)
        
        self.set_new_xlim_ylim(*self.graph_data['tof_fore'], self._fore_tof_ax, 
            self.graph_data['tof_start'], self.graph_data['tof_end'], kind=yscale)
        self.set_new_xlim_ylim(*self.graph_data['tof_back'], self._back_tof_ax, 
            self.graph_data['tof_start'], self.graph_data['tof_end'], kind=yscale)
        self.set_new_xlim_ylim(*self.graph_data['tof_subt'], self._subt_tof_ax, 
            self.graph_data['tof_start'], self.graph_data['tof_end'], kind=yscale)

        self._line_fore_tof.figure.canvas.draw()
        self._line_back_tof.figure.canvas.draw()
        self._line_subt_tof.figure.canvas.draw()
        
        tof_coor, raw_tof = self.graph_data['tof_subt']
        with IgnoreWarnings("length one"):
            new_raw_tof = rebinning(new_tof_coor, tof_coor, raw_tof)
        self._line_raw_tof.set_data(new_tof_coor, new_raw_tof)

        tof_points, mq_points = self.calibration_data['tof_mq_points']
        tof_model, mq_model = self.calibration_data['tof_mq_model']

        # tof_model = np.linspace(np.min(tof_points), np.max(tof_points), num=1000)
        self._line_raw_tof_points.set_data(tof_points, raw_tof[closest(tof_points, tof_coor)])

        self._line_cal_tof.set_data(tof_model, mq_model)
        self._line_cal_tof_points.set_data(tof_points, mq_points)
        self.set_new_xlim_ylim(tof_points, mq_points, self._cal_tof_ax, None, None)


        self._line_mq_tof.set_data(self.graph_data['mq_subt'])

        
        self.set_new_xlim_ylim(*self.graph_data['tof_subt'], self._raw_tof_ax, 
            *self.get_tof_lim_data()[:2])
        self.set_new_xlim_ylim(*self.graph_data['mq_subt'], self._mq_tof_ax, 
            *self.get_mq_lim_data(self.graph_data['mq_subt'][0])[:2])
        # self._mq_tof_ax.ticklabel_format(axis='y', useOffset=False)  # setting the ylim resets the format! This is a quick fix
        
        self._line_raw_tof.figure.canvas.draw()
        self._line_raw_tof_points.figure.canvas.draw()
        self._line_cal_tof.figure.canvas.draw()
        self._line_cal_tof_points.figure.canvas.draw()
        self._line_mq_tof.figure.canvas.draw()


        self._line_fore_mq.set_data(new_mq_coor, new_mq_fore)
        self._line_back_mq.set_data(new_mq_coor, new_mq_back)
        self._line_subt_mq.set_data(new_mq_coor, new_mq_subt)
        yscale = self.combobox_tof_yscale.currentText().lower()
        self._fore_mq_ax.set_yscale(yscale)
        self._back_mq_ax.set_yscale(yscale)
        self._subt_mq_ax.set_yscale(yscale)
        
        self.set_new_xlim_ylim(*self.graph_data['mq_fore'], self._fore_mq_ax, 
            self.graph_data['mq_start'], self.graph_data['mq_end'], kind=yscale)
        self.set_new_xlim_ylim(*self.graph_data['mq_back'], self._back_mq_ax, 
            self.graph_data['mq_start'], self.graph_data['mq_end'], kind=yscale)
        self.set_new_xlim_ylim(*self.graph_data['mq_subt'], self._subt_mq_ax, 
            self.graph_data['mq_start'], self.graph_data['mq_end'], kind=yscale)

        self._line_fore_mq.figure.canvas.draw()
        self._line_back_mq.figure.canvas.draw()
        self._line_subt_mq.figure.canvas.draw()

        time_end = time.time()
        print('time elapsed (redraw_tof_data): ', time_end-time_start)


    def update_pes_window(self):
        '''
        Draw the PES window in the Main VMI tab. This function is fine.
        '''

        self.update_pes_calibration_window()

        energies, pes = self.graph_data['pes_subt']
        rsquared, betas = self.graph_data['betas']
        l_values = self.betas
        betas_to_axes = {
            1 : self._line_beta1,
            2 : self._line_beta2,
            3 : self._line_beta3,
            4 : self._line_beta4,
        }
        betas_to_boxes = {
            1 : self.box_beta1,
            2 : self.box_beta2,
            3 : self.box_beta3,
            4 : self.box_beta4,
        }
        if self.box_pes.isChecked():
            self._line_pes.set_data(energies, pes)
        else:
            self._line_pes.set_data(energies, np.zeros(np.shape(pes))*np.nan)
        possible_l_values = [l_value for l_value in l_values if l_value in [1,2,3,4]]        
        for index, l_value in enumerate(possible_l_values):
            if betas_to_boxes[l_value].isChecked():
                betas_to_axes[l_value].set_data(energies, betas[:,index])
            else:
                betas_to_axes[l_value].set_data(energies, np.zeros(np.shape(betas[:,index]))*np.nan)

        ke, pes = self.graph_data['pes_subt']
        self.set_new_xlim_ylim(energies, pes, self._pes_ax, 
            *self.get_ke_lim_data(ke)[:2])

        self._pes_ax.figure.canvas.draw()
        self._betas_ax.figure.canvas.draw()

    def update_main_vmi_window(self):
        """
        Update the VMI window in the Main VMI tab.
        """

        if do_blitting := self.graph_data['vmi_fore'].shape == self._vmi_shape:
            fore_background = self.fore_fig.canvas.copy_from_bbox(self._fore_ax.bbox)
            self.fore_fig.canvas.restore_region(fore_background)
            self._fore_ax_data.set_data(self.graph_data['vmi_fore'])
            self._fore_ax.draw_artist(self._fore_ax_data)
            # self._fore_ax_data.autoscale()
            self.fore_fig.canvas.blit(self._fore_ax.bbox)

            back_background = self.back_fig.canvas.copy_from_bbox(self._back_ax.bbox)
            self.back_fig.canvas.restore_region(back_background)
            self._back_ax_data.set_data(self.graph_data['vmi_back'])
            self._back_ax.draw_artist(self._back_ax_data)
            # self._back_ax_data.autoscale()
            self.back_fig.canvas.blit(self._back_ax.bbox)

            subt_background = self.subt_fig.canvas.copy_from_bbox(self._subt_ax.bbox)
            self.subt_fig.canvas.restore_region(subt_background)
            self._subt_ax_data.set_data(self.graph_data['vmi_subt'])
            self._subt_ax.draw_artist(self._subt_ax_data)
            # self._subt_ax_data.autoscale()
            self.subt_fig.canvas.blit(self._subt_ax.bbox)
            
        else:
            # extent = (0, data_shape[0], 0, data_shape[1])
            data_shape = self.graph_data['vmi_fore'].shape
            extent = (0, data_shape[0], data_shape[1], 0)
            self._fore_ax_data.set_data(self.graph_data['vmi_fore'])
            self._fore_ax_data.autoscale()
            self._back_ax_data.set_data(self.graph_data['vmi_back'])
            self._back_ax_data.autoscale()
            self._subt_ax_data.set_data(self.graph_data['vmi_subt'])
            with IgnoreWarnings("makes transformation singular"):
                self._fore_ax_data.set_extent(extent)
                self._back_ax_data.set_extent(extent)
                self._subt_ax_data.set_extent(extent)
            self._subt_ax_data.autoscale()
            self._fore_ax_data.figure.canvas.draw()
            self._back_ax_data.figure.canvas.draw()
            self._subt_ax_data.figure.canvas.draw()

        self._vmi_shape = self.graph_data['vmi_fore'].shape

    def update_image_window(self):
        if do_blitting := ((self.graph_data['vmi_raw'].shape == self._image_vmi_shape)
                           and (self.graph_data['vmi_reduced'].shape==self._image_small_vmi_shape)
        ):
            vmi_raw_background = self.vmi_raw_fig.canvas.copy_from_bbox(self._vmi_raw_ax.bbox)
            self.vmi_raw_fig.canvas.restore_region(vmi_raw_background)
            self._vmi_raw_ax_data.set_data(self.graph_data['vmi_raw'])
            self._vmi_raw_guide_ax_data.set_data(self.graph_data['ring_guide'])
            self._vmi_raw_ax.draw_artist(self._vmi_raw_ax_data)
            self._vmi_raw_ax.draw_artist(self._vmi_raw_guide_ax_data)
            # self._vmi_raw_ax_data.autoscale()
            self.vmi_raw_fig.canvas.blit(self._vmi_raw_ax.bbox)
            
            vmi_corr_background = self.vmi_corr_fig.canvas.copy_from_bbox(self._vmi_corr_ax.bbox)
            self.vmi_corr_fig.canvas.restore_region(vmi_corr_background)
            self._vmi_corr_ax_data.set_data(self.graph_data['vmi_corr'])
            self._vmi_corr_ax.draw_artist(self._vmi_corr_ax_data)
            # self._vmi_corr_ax_data.autoscale()
            self.vmi_corr_fig.canvas.blit(self._vmi_corr_ax.bbox)
            
            vmi_reduced_background = self.vmi_reduced_fig.canvas.copy_from_bbox(self._vmi_reduced_ax.bbox)
            self.vmi_reduced_fig.canvas.restore_region(vmi_reduced_background)
            self._vmi_reduced_ax_data.set_data(self.graph_data['vmi_reduced'])
            self._vmi_reduced_ax.draw_artist(self._vmi_reduced_ax_data)
            # self._vmi_reduced_ax_data.autoscale()
            self.vmi_reduced_fig.canvas.blit(self._vmi_reduced_ax.bbox)
            
            vmi_fit_background = self.vmi_fit_fig.canvas.copy_from_bbox(self._vmi_fit_ax.bbox)
            self.vmi_fit_fig.canvas.restore_region(vmi_fit_background)
            self._vmi_fit_ax_data.set_data(self.graph_data['vmi_fit'])
            self._vmi_fit_ax.draw_artist(self._vmi_fit_ax_data)
            # self._vmi_fit_ax_data.autoscale()
            self.vmi_fit_fig.canvas.blit(self._vmi_fit_ax.bbox)
            
            vmi_inverse_background = self.vmi_inverse_fig.canvas.copy_from_bbox(self._vmi_inverse_ax.bbox)
            self.vmi_inverse_fig.canvas.restore_region(vmi_inverse_background)
            self._vmi_inverse_ax_data.set_data(self.graph_data['vmi_inverse'])
            self._vmi_inverse_ax.draw_artist(self._vmi_inverse_ax_data)
            # self._vmi_inverse_ax_data.autoscale()
            self.vmi_inverse_fig.canvas.blit(self._vmi_inverse_ax.bbox)
            
        else:
            data_shape = self.graph_data['vmi_raw'].shape
            extent = (0, data_shape[0], data_shape[1], 0)
            
            small_data_shape = self.graph_data['vmi_reduced'].shape
            small_extent = (0, small_data_shape[0], small_data_shape[1], 0)
            
            self._vmi_raw_ax_data.set_data(self.graph_data['vmi_raw'])
            self._vmi_raw_guide_ax_data.set_data(self.graph_data['ring_guide'])
            with IgnoreWarnings("makes transformation singular"):
                self._vmi_raw_ax_data.set_extent(extent)
            self._vmi_raw_ax_data.autoscale()
            self._vmi_raw_ax.figure.canvas.draw()
            
            self._vmi_corr_ax_data.set_data(self.graph_data['vmi_corr'])
            with IgnoreWarnings("makes transformation singular"):
                self._vmi_corr_ax_data.set_extent(extent)
            self._vmi_corr_ax_data.autoscale()
            self._vmi_corr_ax.figure.canvas.draw()
            
            self._vmi_reduced_ax_data.set_data(self.graph_data['vmi_reduced'])
            with IgnoreWarnings("makes transformation singular"):
                self._vmi_reduced_ax_data.set_extent(small_extent)
            self._vmi_reduced_ax_data.autoscale()
            self._vmi_reduced_ax.figure.canvas.draw()

            self._vmi_fit_ax_data.set_data(self.graph_data['vmi_fit'])
            with IgnoreWarnings("makes transformation singular"):
                self._vmi_fit_ax_data.set_extent(small_extent)
            self._vmi_fit_ax_data.autoscale()
            self._vmi_fit_ax.figure.canvas.draw()

            self._vmi_inverse_ax_data.set_data(self.graph_data['vmi_inverse'])
            with IgnoreWarnings("makes transformation singular"):
                self._vmi_inverse_ax_data.set_extent(small_extent)
            self._vmi_inverse_ax_data.autoscale()
            self._vmi_inverse_ax.figure.canvas.draw()

        self._image_vmi_shape = self.graph_data['vmi_raw'].shape
        self._image_small_vmi_shape = self.graph_data['vmi_reduced'].shape

        # PES in the image correction tab
        radial, rdf = self.graph_data['subt_rdf']
        self._vmi_rdf_ax_data.set_data(radial, rdf)
        self.set_new_xlim_ylim(radial, rdf, self._vmi_rdf_ax, 
            None, None)
        self._vmi_rdf_ax.figure.canvas.draw()
    
    def get_mq_lim_data(self, mq_coor):
        mq_start_string = self.text_edit_mq_start.toPlainText()
        mq_end_string = self.text_edit_mq_end.toPlainText()
        mq_bins_string = self.text_edit_mq_bins.toPlainText()
        # mq_coor, *_ = self.mq_data
        valid = np.isfinite(mq_coor)
        valid_mq = mq_coor[valid]
        if not valid.any():
            valid_mq = np.array([0,])
            
        default_mq_start = np.min(valid_mq)
        default_mq_end = np.max(valid_mq)
        default_mq_bins = len(valid_mq)
        if mq_start_string == '': 
            mq_start = default_mq_start
        else:
            mq_start = float(mq_start_string)
        if mq_end_string == '': 
            mq_end = default_mq_end
        else:
            mq_end = float(mq_end_string)
        if mq_bins_string == '': 
            mq_bins = default_mq_bins
        else:
            mq_bins = int(mq_bins_string)
        return mq_start, mq_end, mq_bins

    def get_tof_lim_data(self):
        tof_start_string = self.text_edit_tof_start.toPlainText()
        tof_end_string = self.text_edit_tof_end.toPlainText()
        tof_bins_string = self.text_edit_tof_bins.toPlainText()
        tof_coor, *_ = self.tof_data
        default_tof_start = np.min(tof_coor)
        default_tof_end = np.max(tof_coor)
        default_tof_bins = len(tof_coor)
        if tof_start_string == '': 
            tof_start = default_tof_start
        else:
            tof_start = float(tof_start_string)
        if tof_end_string == '': 
            tof_end = default_tof_end
        else:
            tof_end = float(tof_end_string)
        if tof_bins_string == '': 
            tof_bins = default_tof_bins
        else:
            tof_bins = int(tof_bins_string)
        return tof_start, tof_end, tof_bins
    

    @staticmethod
    def set_new_xlim_ylim(x, y, ax, start_str, end_str, kind='linear'):
        valid = np.isfinite(y) * np.isfinite(x)
        _x = x[valid]
        _y = y[valid]
        xlim = ax.get_xlim()
        new_xlim = list(xlim)
        non_empty_coor = len(_x) > 0
        if start_str is None and non_empty_coor:
            new_xlim[0] = np.min(_x)
        elif start_str is not None and non_empty_coor:
            new_xlim[0] = float(start_str)
        if end_str is None and non_empty_coor:
            new_xlim[1] = np.max(_x)
        elif end_str is not None and non_empty_coor:
            new_xlim[1] = float(end_str)
        if new_xlim[0] == new_xlim[1]:
            new_xlim = (None, None)
        new_xlim = ax.set_xlim(new_xlim)
        
        crit = (new_xlim[0] <= _x) * (_x <= new_xlim[1])
        y_crit = _y[crit]
        ylim = ax.get_ylim()
        if non_empty_coor and (len(y_crit)>0):
            new_ylim = (np.min(_y[crit]), np.max(_y[crit]))
        else:
            new_ylim = list(ylim)
        if new_ylim[0] == new_ylim[1]:
            new_ylim = (None, None)
        new_ylim = list(ax.set_ylim(new_ylim))
        if kind=='log':
            new_ylim[0] = new_ylim[1]*1e-5
        ax.set_ylim(new_ylim)


    def get_ke_lim_data(self, ke_coor):
        ke_start_string = self.text_edit_ke_start.toPlainText()
        ke_end_string = self.text_edit_ke_end.toPlainText()
        ke_bins_string = self.text_edit_ke_bins.toPlainText()
        # ke_coor, *_ = self.ke_data
        valid = np.isfinite(ke_coor)
        valid_ke = ke_coor[valid]
        if not valid.any():
            valid_ke = np.array([0,])
            
        default_ke_start = np.min(valid_ke)
        default_ke_end = np.max(valid_ke)
        default_ke_bins = len(valid_ke)
        if ke_start_string == '': 
            ke_start = default_ke_start
        else:
            ke_start = float(ke_start_string)
        if ke_end_string == '': 
            ke_end = default_ke_end
        else:
            ke_end = float(ke_end_string)
        if ke_bins_string == '': 
            ke_bins = default_ke_bins
        else:
            ke_bins = int(ke_bins_string)
        return ke_start, ke_end, ke_bins


    def update_pes_calibration_window(self):

        rsquare, subt_rsdf = self.graph_data['subt_rsdf']

        # perform calibration here!

        cal_points_string = self.test_edit_cal_points.toPlainText()
        rsquare_ke_peaks = self.string_to_pairs(cal_points_string, dtype=float)
        rsquare_points, ke_points = rsquare_ke_peaks.T


        from fermi_libraries.common_functions import weighted_linear_regression

        slope, *_ = weighted_linear_regression(rsquare_points, ke_points, zero_intercept=True)

        self.pes_calibration_constant = slope

        rsquare_ke_coor_func = lambda x: slope * x

        ke = rsquare_ke_coor_func(rsquare)
        pes = subt_rsdf / slope # jacobian correction

        self.graph_data['pes_subt'] = ke, pes


        ke_start, ke_end, ke_bins = self.get_ke_lim_data(ke)
        new_ke_coor = np.linspace(ke_start, ke_end, num=ke_bins)
        ke_coor, raw_pes = ke, pes
        with IgnoreWarnings("length one"):
            new_raw_pes = rebinning(new_ke_coor, ke_coor, raw_pes)
        self._line_ke_rsquare.set_data(new_ke_coor, new_raw_pes)


        model_rsquare = np.linspace(np.min(rsquare_points), np.max(rsquare_points), num=1000)

        self._line_cal_rsquare.set_data(model_rsquare, rsquare_ke_coor_func(model_rsquare))
        self._line_cal_rsquare_points.set_data(rsquare_points, ke_points)
        self.set_new_xlim_ylim(np.concatenate((model_rsquare, rsquare_points)), 
                               np.concatenate((rsquare_ke_coor_func(model_rsquare), ke_points)), 
                               self._cal_rsquare_ax, None, None)

        self.graph_data['ke_subt'] = ke, pes

        self._line_raw_rsquare.set_data(*self.graph_data['subt_rsdf'])
        self._line_raw_rsquare_points.set_data(rsquare_points, subt_rsdf[closest(rsquare_points, rsquare)])
        
        self.set_new_xlim_ylim(*self.graph_data['subt_rsdf'], self._raw_rsquare_ax, 
            None, None)
        test_data = self.get_ke_lim_data(ke)[:2]
        self.set_new_xlim_ylim(*self.graph_data['pes_subt'], self._ke_rsquare_ax, 
            *self.get_ke_lim_data(ke)[:2])
        # self._mq_tof_ax.ticklabel_format(axis='y', useOffset=False)  # setting the ylim resets the format! This is a quick fix

        self._line_cal_rsquare_points.figure.canvas.draw()
        self._line_raw_rsquare.figure.canvas.draw()
        # self._line_subt_ke.figure.canvas.draw()
        self._line_ke_rsquare.figure.canvas.draw()


    def change_pes_calibration_constants(self):
        self.text_edit_cal_constant.setText(str(round_to_n(self.pes_calibration_constant, 8)))

    def change_ion_tof_calibration_constants(self):
        self.text_edit_tof_constant_t0.setText(str(round_to_n(self.ion_tof_calibration_constants[0], 8)))
        self.text_edit_tof_constant_c.setText(str(round_to_n(self.ion_tof_calibration_constants[1], 8)))

    def click_fetch_new_files(self):
        self.status['fetch_new_files'] = True
        self.text_display_update_status.setText('Fetch')
        self.text_display_update_status_2.setText('Fetch')
        self.resume_timer()
    
    def click_auto_newest_folder(self):
        self.status['auto_newest_folder'] = True
        self.test_display_folder_status.setText('Search')
        self.test_display_folder_status_2.setText('Search')

    def click_stop_fetch(self):
        self.status['fetch_new_files'] = False
        self.text_display_update_status.setText('Stopped')
        self.text_display_update_status_2.setText('Stopped')
        self.stop_timer()

    def click_stay_folder(self):
        self.status['auto_newest_folder'] = False
        self.test_display_folder_status.setText('Stay')
        self.test_display_folder_status_2.setText('Stay')

import os, sys, traceback, re, pathlib
import numpy as np
import matplotlib.pyplot as plt
from time import strftime, localtime, time

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qtagg import \
    NavigationToolbar2QT as NavigationToolbar

from PySide6.QtCore import QObject, Signal, QThreadPool, Signal, Slot, QRunnable, QTimer
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication

from fermi_libraries.run_module import MultithreadRun
from fermi_libraries.run_module import Run
from fermi_libraries.common_functions import (
    set_recursion_limit, resolve_path, closest, set_default_labels, rebinning)
from fermi_libraries.dictionary_search import search_symbols
from fermi_libraries.calibration_tools import (
    tof_mq_calibration, tof_mq_coordinate_func, mq_tof_coordinate_func, 
    tof_to_mq_conversion, mq_to_tof_conversion)

from cpbasex.cpbasex import cpbasex_energy as cpbasex_energy_inversion
from cpbasex.gData import loadG
from cpbasex.image_mod import resize, resizeFoldedHalf, foldHalf
from cpbasex.image_mod import find_center, find_rotation, find_ellipticity
from cpbasex.image_mod import center_image, rotate, stretch

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        if 'progress_callback' in self.kwargs.keys():
            self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done

import warnings
import time

# the threadpool won't be closed until program exit, so we'll ignore this "pool not closed" warning
warnings.filterwarnings(action='ignore', category=ResourceWarning, module='.*pool')

class IgnoreWarnings(object):
    def __init__(self, message):
        self.message = message
    
    def __enter__(self):
        warnings.filterwarnings("ignore", message=f".*{self.message}.*")
    
    def __exit__(self, *_):
        warnings.filterwarnings("default", message=f".*{self.message}.*")

def round_to_n(x, n):
    if x == 0:
        return 0
    return round(x, -int(np.floor(np.sign(x) * np.log10(abs(x)))) + n)

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()
        
        self.layout = layout
        self.widget = widget
    
    def add_canvas(self, app):
        app.vmi_abel

        # main window PES canvas
        pes_fig = Figure(figsize=(5, 3))
        pes_canvas = FigureCanvas(pes_fig)
        app.vmi_abel.addWidget(pes_canvas)
        pes_toolbar = NavigationToolbar(pes_canvas, self)
        app.vmi_abel.addWidget(pes_toolbar)

        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        pes_toolbar.setSizePolicy(sizePolicy1)
        # pes_toolbar.setMinimumSize(QSize(200, 50))
        # pes_toolbar.setMaximumSize(QSize(200, 100))

        app._pes_ax = pes_canvas.figure.subplots()
        app._betas_ax = app._pes_ax.twinx()

        app._line_pes, = app._pes_ax.plot([], [])
        app._line_beta1, = app._betas_ax.plot([], [])
        app._line_beta2, = app._betas_ax.plot([], [])
        app._line_beta3, = app._betas_ax.plot([], [])
        app._line_beta4, = app._betas_ax.plot([], [])
        app._betas_ax.set_ylim(-2, 2)
        app._pes_ax.set_xlabel('PES signal')
        app._pes_ax.set_ylabel('eKE (eV)')
        app._betas_ax.set_ylabel(r'$\beta$-value')
        app._pes_ax.xaxis.labelpad = 0
        plt.tight_layout()
        pes_fig.subplots_adjust(bottom=0.26, left=0.15, right=0.90, top=0.95)
        
        x_lin, y_lin = np.linspace(-3,3,num=300), np.linspace(-3,3,num=300)
        x, y = np.meshgrid(x_lin, y_lin, indexing='ij')
        subt_placeholder = np.exp(-np.sqrt(x**2+y**2)/2) * 10
        back_placeholder = np.random.normal(size=np.shape(x))*1
        fore_placeholder = subt_placeholder + back_placeholder

        # fore, back, and subt plots
        app.fore_fig = Figure(figsize=(7, 7))
        fore_canvas = FigureCanvas(app.fore_fig)
        app.vmi_fore.addWidget(fore_canvas)
        app.vmi_fore.addWidget(NavigationToolbar(fore_canvas, self))
        app._fore_ax = fore_canvas.figure.subplots()
        with IgnoreWarnings("makes transformation singular"):
            app._fore_ax_data = app._fore_ax.imshow([[],])
        app.fore_fig.colorbar(app._fore_ax_data, ax=app._fore_ax)
        plt.tight_layout()
        
        app.back_fig = Figure(figsize=(7, 7))
        back_canvas = FigureCanvas(app.back_fig)
        app.vmi_back.addWidget(back_canvas)
        app.vmi_back.addWidget(NavigationToolbar(back_canvas, self))
        app._back_ax = back_canvas.figure.subplots()
        with IgnoreWarnings("makes transformation singular"):
            app._back_ax_data = app._back_ax.imshow([[],])
        app.back_fig.colorbar(app._back_ax_data, ax=app._back_ax)
        plt.tight_layout()
        
        app.subt_fig = Figure(figsize=(7, 7))
        subt_canvas = FigureCanvas(app.subt_fig)
        app.vmi_subt.addWidget(subt_canvas)
        app.vmi_subt.addWidget(NavigationToolbar(subt_canvas, self))
        app._subt_ax = subt_canvas.figure.subplots()
        with IgnoreWarnings("makes transformation singular"):
            app._subt_ax_data = app._subt_ax.imshow([[],])
        app.subt_fig.colorbar(app._subt_ax_data, ax=app._subt_ax)
        plt.tight_layout()

        # fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
        app.fore_fig.subplots_adjust(bottom=0.10, left=0.05, right=1.0, top=0.95)
        app.back_fig.subplots_adjust(bottom=0.10, left=0.05, right=1.0, top=0.95)
        app.subt_fig.subplots_adjust(bottom=0.10, left=0.05, right=1.0, top=0.95)

        # vmi calibration tab
        app.vmi_raw_fig = Figure(figsize=(7, 7))
        vmi_raw_canvas = FigureCanvas(app.vmi_raw_fig)
        app.vmi_show_raw.addWidget(vmi_raw_canvas)
        app.vmi_show_raw.addWidget(NavigationToolbar(vmi_raw_canvas, self))
        app._vmi_raw_ax = vmi_raw_canvas.figure.subplots()
        with IgnoreWarnings("makes transformation singular"):
            app._vmi_raw_guide_ax_data, *_ = app._vmi_raw_ax.plot([], [], color='red', linewidth=0.5)
            app._vmi_raw_ax_data = app._vmi_raw_ax.imshow([[],])
        plt.tight_layout()
        
        app.vmi_corr_fig = Figure(figsize=(7, 7))
        vmi_corr_canvas = FigureCanvas(app.vmi_corr_fig)
        app.vmi_show_corrected.addWidget(vmi_corr_canvas)
        app.vmi_show_corrected.addWidget(NavigationToolbar(vmi_corr_canvas, self))
        app._vmi_corr_ax = vmi_corr_canvas.figure.subplots()
        with IgnoreWarnings("makes transformation singular"):
            app._vmi_corr_ax_data = app._vmi_corr_ax.imshow([[],])
        plt.tight_layout()
        
        app.vmi_reduced_fig = Figure(figsize=(7, 7))
        vmi_reduced_canvas = FigureCanvas(app.vmi_reduced_fig)
        app.vmi_show_reduced.addWidget(vmi_reduced_canvas)
        app.vmi_show_reduced.addWidget(NavigationToolbar(vmi_reduced_canvas, self))
        app._vmi_reduced_ax = vmi_reduced_canvas.figure.subplots()
        with IgnoreWarnings("makes transformation singular"):
            app._vmi_reduced_ax_data = app._vmi_reduced_ax.imshow([[],])
        plt.tight_layout()

        app.vmi_fit_fig = Figure(figsize=(7, 7))
        vmi_fit_canvas = FigureCanvas(app.vmi_fit_fig)
        app.vmi_show_fit.addWidget(vmi_fit_canvas)
        app.vmi_show_fit.addWidget(NavigationToolbar(vmi_fit_canvas, self))
        app._vmi_fit_ax = vmi_fit_canvas.figure.subplots()
        with IgnoreWarnings("makes transformation singular"):
            app._vmi_fit_ax_data = app._vmi_fit_ax.imshow([[],])
        plt.tight_layout()
        
        app.vmi_inverse_fig = Figure(figsize=(7, 7))
        vmi_inverse_canvas = FigureCanvas(app.vmi_inverse_fig)
        app.vmi_show_inverse.addWidget(vmi_inverse_canvas)
        app.vmi_show_inverse.addWidget(NavigationToolbar(vmi_inverse_canvas, self))
        app._vmi_inverse_ax = vmi_inverse_canvas.figure.subplots()
        with IgnoreWarnings("makes transformation singular"):
            app._vmi_inverse_ax_data = app._vmi_inverse_ax.imshow([[],])
        plt.tight_layout()

        app.vmi_rdf_fig = Figure(figsize=(7, 7))
        vmi_rdf_canvas = FigureCanvas(app.vmi_rdf_fig)
        app.vmi_show_radialdist.addWidget(vmi_rdf_canvas)
        app.vmi_show_radialdist.addWidget(NavigationToolbar(vmi_rdf_canvas, self))
        app._vmi_rdf_ax = vmi_rdf_canvas.figure.subplots()
        app._vmi_rdf_ax_data, *_ = app._vmi_rdf_ax.plot([], [])
        app._vmi_rdf_ax.set_xlabel('radius')
        app._vmi_rdf_ax.set_ylabel('RDF')
        # self._vmi_rdf_ax.text(0, 200, 'Placeholder!', fontsize=20)
        plt.tight_layout()
        
        app.vmi_raw_fig.subplots_adjust(bottom=0.15, left=0.05, right=1.0, top=0.95)
        app.vmi_corr_fig.subplots_adjust(bottom=0.15, left=0.05, right=1.0, top=0.95)
        app.vmi_reduced_fig.subplots_adjust(bottom=0.15, left=0.05, right=1.0, top=0.95)
        app.vmi_fit_fig.subplots_adjust(bottom=0.15, left=0.05, right=1.0, top=0.95)
        app.vmi_inverse_fig.subplots_adjust(bottom=0.15, left=0.05, right=1.0, top=0.95)
        app.vmi_rdf_fig.subplots_adjust(bottom=0.15, left=0.05, right=0.95, top=0.95)
        

        # fore, back, and subt plots
        app.fore_tof_fig = Figure(figsize=(5, 3))
        fore_tof_canvas = FigureCanvas(app.fore_tof_fig)
        app.tof_fore.addWidget(fore_tof_canvas)
        app.tof_fore.addWidget(NavigationToolbar(fore_tof_canvas, self))
        app._fore_tof_ax = fore_tof_canvas.figure.subplots()
        app._line_fore_tof, = app._fore_tof_ax.plot([], [])
        app._fore_tof_ax.set_ylabel('TOF signal')
        app._fore_tof_ax.set_xlabel('TOF (ns)')
        app._fore_tof_ax.xaxis.labelpad = 0
        plt.tight_layout()
        app.fore_tof_fig.subplots_adjust(bottom=0.26, left=0.1, right=0.95, top=0.95)



        # back, back, and subt plots
        app.back_tof_fig = Figure(figsize=(5, 3))
        back_tof_canvas = FigureCanvas(app.back_tof_fig)
        app.tof_back.addWidget(back_tof_canvas)
        app.tof_back.addWidget(NavigationToolbar(back_tof_canvas, self))
        app._back_tof_ax = back_tof_canvas.figure.subplots()
        app._line_back_tof, = app._back_tof_ax.plot([], [])
        app._fore_tof_ax.set_ylabel('TOF signal')
        app._back_tof_ax.set_xlabel('TOF (ns)')
        app._back_tof_ax.xaxis.labelpad = 0
        plt.tight_layout()
        app.back_tof_fig.subplots_adjust(bottom=0.26, left=0.1, right=0.95, top=0.95)

        # subt, subt, and subt plots
        app.subt_tof_fig = Figure(figsize=(5, 3))
        subt_tof_canvas = FigureCanvas(app.subt_tof_fig)
        app.tof_subt.addWidget(subt_tof_canvas)
        app.tof_subt.addWidget(NavigationToolbar(subt_tof_canvas, self))
        app._subt_tof_ax = subt_tof_canvas.figure.subplots()
        app._line_subt_tof, = app._subt_tof_ax.plot([], [])
        app._fore_tof_ax.set_ylabel('TOF signal')
        app._subt_tof_ax.set_xlabel('TOF (ns)')
        app._subt_tof_ax.xaxis.labelpad = 0
        plt.tight_layout()
        app.subt_tof_fig.subplots_adjust(bottom=0.26, left=0.1, right=0.95, top=0.95)
        
        # TOF calibration tab
        raw_tof_fig = Figure(figsize=(5,3))
        raw_tof_canvas = FigureCanvas(raw_tof_fig)
        app.tof_show_raw.addWidget(raw_tof_canvas)
        app.tof_show_raw.addWidget(NavigationToolbar(raw_tof_canvas, self))
        app._raw_tof_ax = raw_tof_canvas.figure.subplots()
        app._raw_tof_ax.set_ylabel('TOF signal')
        app._raw_tof_ax.set_xlabel('TOF (ns)')
        app._line_raw_tof, = app._raw_tof_ax.plot([], [])
        app._line_raw_tof_points, = app._raw_tof_ax.plot([], [], marker='v', linestyle='')
        app._raw_tof_ax.xaxis.labelpad = 0
        raw_tof_fig.subplots_adjust(bottom=0.16, left=0.15, right=0.95, top=0.95)
        plt.tight_layout()
        
        mq_tof_fig = Figure(figsize=(5,3))
        mq_tof_canvas = FigureCanvas(mq_tof_fig)
        app.tof_show_mq.addWidget(mq_tof_canvas)
        app.tof_show_mq.addWidget(NavigationToolbar(mq_tof_canvas, self))
        app._mq_tof_ax = mq_tof_canvas.figure.subplots()
        app._mq_tof_ax.set_ylabel('m/q-signal')
        app._mq_tof_ax.set_xlabel('m/q')
        app._line_mq_tof, = app._mq_tof_ax.plot([], [])
        app._mq_tof_ax.xaxis.labelpad = 0
        app._mq_tof_ax.ticklabel_format(axis='y', useOffset=False, scilimits=(0,0))
        mq_tof_fig.subplots_adjust(bottom=0.16, left=0.15, right=0.95, top=0.92)
        plt.tight_layout()

        # TOF calibration plot
        cal_tof_fig = Figure(figsize=(5, 3))
        cal_tof_canvas = FigureCanvas(cal_tof_fig)
        app.tof_show_calibration.addWidget(cal_tof_canvas)
        app.tof_show_calibration.addWidget(NavigationToolbar(cal_tof_canvas, self))
        app._cal_tof_ax = cal_tof_canvas.figure.subplots()

        app._line_cal_tof, = app._cal_tof_ax.plot([], [], color='black')
        app._line_cal_tof_points, = app._cal_tof_ax.plot([], [], marker='o', linestyle='')
        app._cal_tof_ax.set_xlabel('TOF (ns)')
        app._cal_tof_ax.set_ylabel('m/q')
        app._cal_tof_ax.xaxis.labelpad = 0
        app._cal_tof_ax.yaxis.labelpad = 0
        plt.tight_layout()
        cal_tof_fig.subplots_adjust(bottom=0.26, left=0.15, right=0.95, top=0.95)


        
        # tof_raw_fig.subplots_adjust(bottom=0.15, left=0.05, right=1.0, top=0.95)
        # tof_corr_fig.subplots_adjust(bottom=0.15, left=0.05, right=1.0, top=0.95)
        
        app.fore_mq_fig = Figure(figsize=(7, 7))
        fore_mq_canvas = FigureCanvas(app.fore_mq_fig)
        app.mq_fore.addWidget(fore_mq_canvas)
        app.mq_fore.addWidget(NavigationToolbar(fore_mq_canvas, self))
        app._fore_mq_ax = fore_mq_canvas.figure.subplots()
        app._fore_mq_ax.set_xlabel('m/q')
        app._line_fore_mq, = app._fore_mq_ax.plot([], [])
        app._fore_mq_ax.xaxis.labelpad = 0
        plt.tight_layout()
        app.fore_mq_fig.subplots_adjust(bottom=0.26, left=0.1, right=0.95, top=0.95)

        app.back_mq_fig = Figure(figsize=(7, 7))
        back_mq_canvas = FigureCanvas(app.back_mq_fig)
        app.mq_back.addWidget(back_mq_canvas)
        app.mq_back.addWidget(NavigationToolbar(back_mq_canvas, self))
        app._back_mq_ax = back_mq_canvas.figure.subplots()
        app._back_mq_ax.set_xlabel('m/q')
        app._line_back_mq, = app._back_mq_ax.plot([], [])
        app._back_mq_ax.xaxis.labelpad = 0
        plt.tight_layout()
        app.back_mq_fig.subplots_adjust(bottom=0.26, left=0.1, right=0.95, top=0.95)

        app.subt_mq_fig = Figure(figsize=(7, 7))
        subt_mq_canvas = FigureCanvas(app.subt_mq_fig)
        app.mq_subt.addWidget(subt_mq_canvas)
        app.mq_subt.addWidget(NavigationToolbar(subt_mq_canvas, self))
        app._subt_mq_ax = subt_mq_canvas.figure.subplots()
        app._subt_mq_ax.set_xlabel('m/q')
        app._line_subt_mq, = app._subt_mq_ax.plot([], [])
        app._subt_mq_ax.xaxis.labelpad = 0
        plt.tight_layout()
        app.subt_mq_fig.subplots_adjust(bottom=0.26, left=0.1, right=0.95, top=0.95)

        # PES calibration tab
        raw_rsquare_fig = Figure(figsize=(5,3))
        raw_rsquare_canvas = FigureCanvas(raw_rsquare_fig)
        app.pes_show_rsquare.addWidget(raw_rsquare_canvas)
        app.pes_show_rsquare.addWidget(NavigationToolbar(raw_rsquare_canvas, self))
        app._raw_rsquare_ax = raw_rsquare_canvas.figure.subplots()
        app._raw_rsquare_ax.set_ylabel('radial-squared signal')
        app._raw_rsquare_ax.set_xlabel(r'r$^{2}$ (pixels$^{2}$)')
        app._line_raw_rsquare, = app._raw_rsquare_ax.plot([], [])
        app._line_raw_rsquare_points, = app._raw_rsquare_ax.plot([], [], marker='v', linestyle='')
        app._raw_rsquare_ax.xaxis.labelpad = 0
        raw_rsquare_fig.subplots_adjust(bottom=0.16, left=0.15, right=0.95, top=0.95)
        plt.tight_layout()
        
        ke_rsquare_fig = Figure(figsize=(5,3))
        ke_rsquare_canvas = FigureCanvas(ke_rsquare_fig)
        app.pes_show_ke.addWidget(ke_rsquare_canvas)
        app.pes_show_ke.addWidget(NavigationToolbar(ke_rsquare_canvas, self))
        app._ke_rsquare_ax = ke_rsquare_canvas.figure.subplots()
        app._ke_rsquare_ax.set_ylabel('KE-signal')
        app._ke_rsquare_ax.set_xlabel('eKE (eV)')
        app._line_ke_rsquare, = app._ke_rsquare_ax.plot([], [])
        app._ke_rsquare_ax.xaxis.labelpad = 0
        app._ke_rsquare_ax.ticklabel_format(axis='y', useOffset=False, scilimits=(0,0))
        ke_rsquare_fig.subplots_adjust(bottom=0.16, left=0.15, right=0.95, top=0.92)
        plt.tight_layout()

        # rsquare calibration plot
        cal_rsquare_fig = Figure(figsize=(5, 3))
        cal_rsquare_canvas = FigureCanvas(cal_rsquare_fig)
        app.rsquare_show_calibration.addWidget(cal_rsquare_canvas)
        app.rsquare_show_calibration.addWidget(NavigationToolbar(cal_rsquare_canvas, self))
        app._cal_rsquare_ax = cal_rsquare_canvas.figure.subplots()

        app._line_cal_rsquare, = app._cal_rsquare_ax.plot([], [], color='black')
        app._line_cal_rsquare_points, = app._cal_rsquare_ax.plot([], [], marker='o', linestyle='')
        app._cal_rsquare_ax.set_xlabel(r'r$^{2}$ (pixels$^{2}$)')
        app._cal_rsquare_ax.set_ylabel('KE (eV)')
        app._cal_rsquare_ax.xaxis.labelpad = 0
        app._cal_rsquare_ax.yaxis.labelpad = 0
        plt.tight_layout()
        cal_rsquare_fig.subplots_adjust(bottom=0.26, left=0.15, right=0.95, top=0.95)

        self.show()

def close_app_threadpool(w, app, tabwidget):
    value = app.exec()
    tabwidget.threadpool.waitForDone()
    return value

# import traceback
# print(traceback.format_exc())

DEBUG = False

def setup_window_app_tabwidget():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    tabWidgetApp = Ui_MainWindow()
    w = MainWindow()

    tabWidgetApp.setupUi(w)
    # w.setObjectName(u"FERMI LDM On-line analysis tool")
    w.setWindowTitle(QCoreApplication.translate("FERMI LDM On-line analysis tool", u"FERMI LDM On-line analysis tool", None))
    tabWidgetApp.setup_signals()
    w.add_canvas(tabWidgetApp)
    
    def wait_for_threads_and_close():  
        tabWidgetApp.threadpool.waitForDone()
        app.quit()
    
    tabWidgetApp.pushButton.clicked.connect(wait_for_threads_and_close)
    
    tabWidgetApp.apply_settings()
    
    return w, app, tabWidgetApp

if __name__ == '__main__':
    w, app, tabWidgetApp = setup_window_app_tabwidget()

    # sys.exit(app.exec())
    sys.exit(close_app_threadpool(w, app, tabWidgetApp))
    # app.exec()