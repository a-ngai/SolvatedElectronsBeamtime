# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
    QGridLayout, QGroupBox, QLabel, QMainWindow,
    QMenu, QMenuBar, QScrollArea, QSizePolicy,
    QStatusBar, QTabWidget, QTextBrowser, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(662, 669)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(20, 10, 621, 511))
        self.tabWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.tab_vmi_main = QWidget()
        self.tab_vmi_main.setObjectName(u"tab_vmi_main")
        self.scrollArea = QScrollArea(self.tab_vmi_main)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(210, 40, 61, 131))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 59, 129))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.button_fetch_new_files = QCommandLinkButton(self.tab_vmi_main)
        self.button_fetch_new_files.setObjectName(u"button_fetch_new_files")
        self.button_fetch_new_files.setGeometry(QRect(10, 210, 181, 31))
        self.tabWidget_2 = QTabWidget(self.tab_vmi_main)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(310, 10, 281, 291))
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
        self.scrollArea_2 = QScrollArea(self.tab_vmi_main)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(30, 320, 91, 154))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 89, 152))
        self.gridLayout_19 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.box_pes = QCheckBox(self.scrollAreaWidgetContents_2)
        self.box_pes.setObjectName(u"box_pes")

        self.gridLayout_19.addWidget(self.box_pes, 0, 0, 1, 1)

        self.box_beta1 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.box_beta1.setObjectName(u"box_beta1")

        self.gridLayout_19.addWidget(self.box_beta1, 1, 0, 1, 1)

        self.box_beta2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.box_beta2.setObjectName(u"box_beta2")

        self.gridLayout_19.addWidget(self.box_beta2, 2, 0, 1, 1)

        self.box_beta3 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.box_beta3.setObjectName(u"box_beta3")

        self.gridLayout_19.addWidget(self.box_beta3, 3, 0, 1, 1)

        self.box_beta4 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.box_beta4.setObjectName(u"box_beta4")

        self.gridLayout_19.addWidget(self.box_beta4, 4, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.label_files_used = QLabel(self.tab_vmi_main)
        self.label_files_used.setObjectName(u"label_files_used")
        self.label_files_used.setGeometry(QRect(210, 20, 61, 16))
        self.label_current_folder = QLabel(self.tab_vmi_main)
        self.label_current_folder.setObjectName(u"label_current_folder")
        self.label_current_folder.setGeometry(QRect(20, 10, 81, 16))
        self.text_edit_current_folder = QTextEdit(self.tab_vmi_main)
        self.text_edit_current_folder.setObjectName(u"text_edit_current_folder")
        self.text_edit_current_folder.setGeometry(QRect(20, 30, 151, 31))
        self.label_update_status = QLabel(self.tab_vmi_main)
        self.label_update_status.setObjectName(u"label_update_status")
        self.label_update_status.setGeometry(QRect(20, 180, 91, 16))
        self.text_display_update_status = QTextBrowser(self.tab_vmi_main)
        self.text_display_update_status.setObjectName(u"text_display_update_status")
        self.text_display_update_status.setGeometry(QRect(100, 180, 71, 31))
        self.button_stop_fetch = QCommandLinkButton(self.tab_vmi_main)
        self.button_stop_fetch.setObjectName(u"button_stop_fetch")
        self.button_stop_fetch.setGeometry(QRect(10, 240, 181, 31))
        self.label_abel_inversion = QLabel(self.tab_vmi_main)
        self.label_abel_inversion.setObjectName(u"label_abel_inversion")
        self.label_abel_inversion.setGeometry(QRect(20, 300, 91, 16))
        self.button_auto_newest_folder = QCommandLinkButton(self.tab_vmi_main)
        self.button_auto_newest_folder.setObjectName(u"button_auto_newest_folder")
        self.button_auto_newest_folder.setGeometry(QRect(10, 100, 181, 31))
        self.button_stay_current_folder = QCommandLinkButton(self.tab_vmi_main)
        self.button_stay_current_folder.setObjectName(u"button_stay_current_folder")
        self.button_stay_current_folder.setGeometry(QRect(10, 130, 181, 31))
        self.test_display_folder_status = QTextBrowser(self.tab_vmi_main)
        self.test_display_folder_status.setObjectName(u"test_display_folder_status")
        self.test_display_folder_status.setGeometry(QRect(100, 70, 71, 31))
        self.label_folder_status = QLabel(self.tab_vmi_main)
        self.label_folder_status.setObjectName(u"label_folder_status")
        self.label_folder_status.setGeometry(QRect(20, 70, 91, 16))
        self.verticalLayoutWidget = QWidget(self.tab_vmi_main)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(180, 300, 411, 181))
        self.vmi_abel = QVBoxLayout(self.verticalLayoutWidget)
        self.vmi_abel.setObjectName(u"vmi_abel")
        self.vmi_abel.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_vmi_main, "")
        self.tab_image_correction = QWidget()
        self.tab_image_correction.setObjectName(u"tab_image_correction")
        self.gridLayoutWidget_3 = QWidget(self.tab_image_correction)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 10, 371, 231))
        self.vmi_show_raw = QGridLayout(self.gridLayoutWidget_3)
        self.vmi_show_raw.setObjectName(u"vmi_show_raw")
        self.vmi_show_raw.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutWidget_4 = QWidget(self.tab_image_correction)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 250, 371, 231))
        self.vmi_show_corrected = QGridLayout(self.gridLayoutWidget_4)
        self.vmi_show_corrected.setObjectName(u"vmi_show_corrected")
        self.vmi_show_corrected.setContentsMargins(0, 0, 0, 0)
        self.label_raw_image = QLabel(self.tab_image_correction)
        self.label_raw_image.setObjectName(u"label_raw_image")
        self.label_raw_image.setGeometry(QRect(30, 10, 71, 16))
        self.label_corrected_image = QLabel(self.tab_image_correction)
        self.label_corrected_image.setObjectName(u"label_corrected_image")
        self.label_corrected_image.setGeometry(QRect(30, 250, 61, 16))
        self.button_apply_vmi_corrections = QCommandLinkButton(self.tab_image_correction)
        self.button_apply_vmi_corrections.setObjectName(u"button_apply_vmi_corrections")
        self.button_apply_vmi_corrections.setGeometry(QRect(390, 400, 161, 41))
        self.groupBox_4 = QGroupBox(self.tab_image_correction)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(390, 10, 221, 151))
        self.label_guess_ycenter = QLabel(self.groupBox_4)
        self.label_guess_ycenter.setObjectName(u"label_guess_ycenter")
        self.label_guess_ycenter.setGeometry(QRect(80, 20, 49, 16))
        self.label_guess_rotate = QLabel(self.groupBox_4)
        self.label_guess_rotate.setObjectName(u"label_guess_rotate")
        self.label_guess_rotate.setGeometry(QRect(160, 20, 49, 16))
        self.label_guess_xzoom = QLabel(self.groupBox_4)
        self.label_guess_xzoom.setObjectName(u"label_guess_xzoom")
        self.label_guess_xzoom.setGeometry(QRect(10, 90, 49, 16))
        self.label_guess_xcenter = QLabel(self.groupBox_4)
        self.label_guess_xcenter.setObjectName(u"label_guess_xcenter")
        self.label_guess_xcenter.setGeometry(QRect(10, 20, 49, 16))
        self.label_guess_yzoom = QLabel(self.groupBox_4)
        self.label_guess_yzoom.setObjectName(u"label_guess_yzoom")
        self.label_guess_yzoom.setGeometry(QRect(80, 90, 49, 16))
        self.text_display_guess_xcenter = QTextBrowser(self.groupBox_4)
        self.text_display_guess_xcenter.setObjectName(u"text_display_guess_xcenter")
        self.text_display_guess_xcenter.setGeometry(QRect(10, 40, 51, 31))
        self.text_dsplay_guess_ycenter = QTextBrowser(self.groupBox_4)
        self.text_dsplay_guess_ycenter.setObjectName(u"text_dsplay_guess_ycenter")
        self.text_dsplay_guess_ycenter.setGeometry(QRect(80, 40, 51, 31))
        self.text_display_guess_rotate = QTextBrowser(self.groupBox_4)
        self.text_display_guess_rotate.setObjectName(u"text_display_guess_rotate")
        self.text_display_guess_rotate.setGeometry(QRect(160, 40, 51, 31))
        self.text_display_guess_xzoom = QTextBrowser(self.groupBox_4)
        self.text_display_guess_xzoom.setObjectName(u"text_display_guess_xzoom")
        self.text_display_guess_xzoom.setGeometry(QRect(10, 110, 51, 31))
        self.text_diesplay_guess_yzoom = QTextBrowser(self.groupBox_4)
        self.text_diesplay_guess_yzoom.setObjectName(u"text_diesplay_guess_yzoom")
        self.text_diesplay_guess_yzoom.setGeometry(QRect(80, 110, 51, 31))
        self.button_get_guess_vmi_corrections = QCommandLinkButton(self.tab_image_correction)
        self.button_get_guess_vmi_corrections.setObjectName(u"button_get_guess_vmi_corrections")
        self.button_get_guess_vmi_corrections.setGeometry(QRect(390, 160, 131, 41))
        self.groupBox_5 = QGroupBox(self.tab_image_correction)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(390, 250, 221, 151))
        self.text_edit_correct_yzoom = QTextEdit(self.groupBox_5)
        self.text_edit_correct_yzoom.setObjectName(u"text_edit_correct_yzoom")
        self.text_edit_correct_yzoom.setGeometry(QRect(80, 100, 51, 31))
        self.label_correct_ycenter = QLabel(self.groupBox_5)
        self.label_correct_ycenter.setObjectName(u"label_correct_ycenter")
        self.label_correct_ycenter.setGeometry(QRect(80, 20, 49, 16))
        self.text_edit_correct_rotate = QTextEdit(self.groupBox_5)
        self.text_edit_correct_rotate.setObjectName(u"text_edit_correct_rotate")
        self.text_edit_correct_rotate.setGeometry(QRect(160, 40, 51, 31))
        self.text_edit_correct_xcenter = QTextEdit(self.groupBox_5)
        self.text_edit_correct_xcenter.setObjectName(u"text_edit_correct_xcenter")
        self.text_edit_correct_xcenter.setGeometry(QRect(10, 40, 51, 31))
        self.text_edit_correct_xzoom = QTextEdit(self.groupBox_5)
        self.text_edit_correct_xzoom.setObjectName(u"text_edit_correct_xzoom")
        self.text_edit_correct_xzoom.setGeometry(QRect(10, 100, 51, 31))
        self.text_edit_correct_ycenter = QTextEdit(self.groupBox_5)
        self.text_edit_correct_ycenter.setObjectName(u"text_edit_correct_ycenter")
        self.text_edit_correct_ycenter.setGeometry(QRect(80, 40, 51, 31))
        self.label_correct_rotate = QLabel(self.groupBox_5)
        self.label_correct_rotate.setObjectName(u"label_correct_rotate")
        self.label_correct_rotate.setGeometry(QRect(160, 20, 49, 16))
        self.label_correct_xzoom = QLabel(self.groupBox_5)
        self.label_correct_xzoom.setObjectName(u"label_correct_xzoom")
        self.label_correct_xzoom.setGeometry(QRect(10, 80, 49, 16))
        self.label_correct_xcenter = QLabel(self.groupBox_5)
        self.label_correct_xcenter.setObjectName(u"label_correct_xcenter")
        self.label_correct_xcenter.setGeometry(QRect(10, 20, 49, 16))
        self.label_correct_yzoom = QLabel(self.groupBox_5)
        self.label_correct_yzoom.setObjectName(u"label_correct_yzoom")
        self.label_correct_yzoom.setGeometry(QRect(80, 80, 49, 16))
        self.tabWidget.addTab(self.tab_image_correction, "")
        self.tab_calibration = QWidget()
        self.tab_calibration.setObjectName(u"tab_calibration")
        self.gridLayoutWidget_5 = QWidget(self.tab_calibration)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(30, 100, 351, 101))
        self.pes_show_pixels = QGridLayout(self.gridLayoutWidget_5)
        self.pes_show_pixels.setObjectName(u"pes_show_pixels")
        self.pes_show_pixels.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutWidget_6 = QWidget(self.tab_calibration)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(30, 300, 351, 91))
        self.pes_show_energy = QGridLayout(self.gridLayoutWidget_6)
        self.pes_show_energy.setObjectName(u"pes_show_energy")
        self.pes_show_energy.setContentsMargins(0, 0, 0, 0)
        self.label_pixel_axis = QLabel(self.tab_calibration)
        self.label_pixel_axis.setObjectName(u"label_pixel_axis")
        self.label_pixel_axis.setGeometry(QRect(40, 70, 49, 16))
        self.label_energy_axis = QLabel(self.tab_calibration)
        self.label_energy_axis.setObjectName(u"label_energy_axis")
        self.label_energy_axis.setGeometry(QRect(40, 270, 49, 16))
        self.test_edit_cal_points = QTextEdit(self.tab_calibration)
        self.test_edit_cal_points.setObjectName(u"test_edit_cal_points")
        self.test_edit_cal_points.setGeometry(QRect(490, 80, 91, 151))
        self.label_cal_points = QLabel(self.tab_calibration)
        self.label_cal_points.setObjectName(u"label_cal_points")
        self.label_cal_points.setGeometry(QRect(500, 50, 71, 21))
        self.button_apply_calibration = QCommandLinkButton(self.tab_calibration)
        self.button_apply_calibration.setObjectName(u"button_apply_calibration")
        self.button_apply_calibration.setGeometry(QRect(420, 250, 172, 41))
        self.label_pes_cal_constants = QLabel(self.tab_calibration)
        self.label_pes_cal_constants.setObjectName(u"label_pes_cal_constants")
        self.label_pes_cal_constants.setGeometry(QRect(440, 300, 91, 16))
        self.text_display_cal_constant = QTextBrowser(self.tab_calibration)
        self.text_display_cal_constant.setObjectName(u"text_display_cal_constant")
        self.text_display_cal_constant.setGeometry(QRect(520, 330, 71, 31))
        self.label_pes_constant_alpha = QLabel(self.tab_calibration)
        self.label_pes_constant_alpha.setObjectName(u"label_pes_constant_alpha")
        self.label_pes_constant_alpha.setGeometry(QRect(450, 340, 61, 16))
        self.tabWidget.addTab(self.tab_calibration, "")
        self.tab_tof_main = QWidget()
        self.tab_tof_main.setObjectName(u"tab_tof_main")
        self.tabWidget_3 = QTabWidget(self.tab_tof_main)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setGeometry(QRect(210, 20, 381, 221))
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.tab_9.setAutoFillBackground(False)
        self.gridLayout_20 = QGridLayout(self.tab_9)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.tof_fore_2 = QGridLayout()
        self.tof_fore_2.setObjectName(u"tof_fore_2")

        self.gridLayout_20.addLayout(self.tof_fore_2, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_9, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.gridLayout_21 = QGridLayout(self.tab_11)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.tof_back_2 = QGridLayout()
        self.tof_back_2.setObjectName(u"tof_back_2")

        self.gridLayout_21.addLayout(self.tof_back_2, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_11, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.gridLayout_22 = QGridLayout(self.tab_12)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.tof_subt_2 = QGridLayout()
        self.tof_subt_2.setObjectName(u"tof_subt_2")

        self.gridLayout_22.addLayout(self.tof_subt_2, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_12, "")
        self.combobox_tof_yscale = QComboBox(self.tab_tof_main)
        self.combobox_tof_yscale.addItem("")
        self.combobox_tof_yscale.addItem("")
        self.combobox_tof_yscale.setObjectName(u"combobox_tof_yscale")
        self.combobox_tof_yscale.setGeometry(QRect(440, 270, 131, 21))
        self.tabWidget.addTab(self.tab_tof_main, "")
        self.tab_tof_calibration = QWidget()
        self.tab_tof_calibration.setObjectName(u"tab_tof_calibration")
        self.gridLayoutWidget_7 = QWidget(self.tab_tof_calibration)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(30, 100, 351, 101))
        self.tof_show_tof = QGridLayout(self.gridLayoutWidget_7)
        self.tof_show_tof.setObjectName(u"tof_show_tof")
        self.tof_show_tof.setContentsMargins(0, 0, 0, 0)
        self.label_tof_axis = QLabel(self.tab_tof_calibration)
        self.label_tof_axis.setObjectName(u"label_tof_axis")
        self.label_tof_axis.setGeometry(QRect(40, 70, 111, 16))
        self.label_mq_axis = QLabel(self.tab_tof_calibration)
        self.label_mq_axis.setObjectName(u"label_mq_axis")
        self.label_mq_axis.setGeometry(QRect(40, 270, 101, 16))
        self.label_tof_cal_points = QLabel(self.tab_tof_calibration)
        self.label_tof_cal_points.setObjectName(u"label_tof_cal_points")
        self.label_tof_cal_points.setGeometry(QRect(500, 50, 71, 21))
        self.gridLayoutWidget_8 = QWidget(self.tab_tof_calibration)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(30, 300, 351, 91))
        self.tof_show_mq = QGridLayout(self.gridLayoutWidget_8)
        self.tof_show_mq.setObjectName(u"tof_show_mq")
        self.tof_show_mq.setContentsMargins(0, 0, 0, 0)
        self.test_edit_tof_cal_points = QTextEdit(self.tab_tof_calibration)
        self.test_edit_tof_cal_points.setObjectName(u"test_edit_tof_cal_points")
        self.test_edit_tof_cal_points.setGeometry(QRect(490, 80, 91, 151))
        self.text_display_tof_constant_t0 = QTextBrowser(self.tab_tof_calibration)
        self.text_display_tof_constant_t0.setObjectName(u"text_display_tof_constant_t0")
        self.text_display_tof_constant_t0.setGeometry(QRect(520, 370, 71, 31))
        self.label_tof_constants = QLabel(self.tab_tof_calibration)
        self.label_tof_constants.setObjectName(u"label_tof_constants")
        self.label_tof_constants.setGeometry(QRect(440, 300, 91, 16))
        self.button_apply_tof_calibration = QCommandLinkButton(self.tab_tof_calibration)
        self.button_apply_tof_calibration.setObjectName(u"button_apply_tof_calibration")
        self.button_apply_tof_calibration.setGeometry(QRect(420, 250, 172, 41))
        self.text_display_tof_constant_c = QTextBrowser(self.tab_tof_calibration)
        self.text_display_tof_constant_c.setObjectName(u"text_display_tof_constant_c")
        self.text_display_tof_constant_c.setGeometry(QRect(520, 330, 71, 31))
        self.label_tof_constant_c = QLabel(self.tab_tof_calibration)
        self.label_tof_constant_c.setObjectName(u"label_tof_constant_c")
        self.label_tof_constant_c.setGeometry(QRect(450, 340, 61, 16))
        self.label_tof_constant_t0 = QLabel(self.tab_tof_calibration)
        self.label_tof_constant_t0.setObjectName(u"label_tof_constant_t0")
        self.label_tof_constant_t0.setGeometry(QRect(450, 380, 61, 16))
        self.tabWidget.addTab(self.tab_tof_calibration, "")
        self.tab_settings = QWidget()
        self.tab_settings.setObjectName(u"tab_settings")
        self.label_search_dir_for_newest_folder = QLabel(self.tab_settings)
        self.label_search_dir_for_newest_folder.setObjectName(u"label_search_dir_for_newest_folder")
        self.label_search_dir_for_newest_folder.setGeometry(QRect(320, 10, 211, 16))
        self.text_edit_search_dir_for_newest_folder = QTextEdit(self.tab_settings)
        self.text_edit_search_dir_for_newest_folder.setObjectName(u"text_edit_search_dir_for_newest_folder")
        self.text_edit_search_dir_for_newest_folder.setGeometry(QRect(320, 30, 271, 31))
        self.label_tof_start = QLabel(self.tab_settings)
        self.label_tof_start.setObjectName(u"label_tof_start")
        self.label_tof_start.setGeometry(QRect(20, 180, 51, 16))
        self.text_edit_tof_start = QTextEdit(self.tab_settings)
        self.text_edit_tof_start.setObjectName(u"text_edit_tof_start")
        self.text_edit_tof_start.setGeometry(QRect(20, 200, 61, 31))
        self.label_tof_stop = QLabel(self.tab_settings)
        self.label_tof_stop.setObjectName(u"label_tof_stop")
        self.label_tof_stop.setGeometry(QRect(100, 180, 51, 16))
        self.text_edit_tof_stop = QTextEdit(self.tab_settings)
        self.text_edit_tof_stop.setObjectName(u"text_edit_tof_stop")
        self.text_edit_tof_stop.setGeometry(QRect(100, 200, 61, 31))
        self.box_slu_parity = QCheckBox(self.tab_settings)
        self.box_slu_parity.setObjectName(u"box_slu_parity")
        self.box_slu_parity.setGeometry(QRect(320, 330, 21, 22))
        self.label_slu_parity = QLabel(self.tab_settings)
        self.label_slu_parity.setObjectName(u"label_slu_parity")
        self.label_slu_parity.setGeometry(QRect(350, 330, 121, 16))
        self.groupBox = QGroupBox(self.tab_settings)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 20, 181, 151))
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
        self.groupBox_2.setGeometry(QRect(320, 160, 241, 147))
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
        self.applyChangesSettings.setGeometry(QRect(420, 400, 141, 31))
        self.text_edit_ke_start = QTextEdit(self.tab_settings)
        self.text_edit_ke_start.setObjectName(u"text_edit_ke_start")
        self.text_edit_ke_start.setGeometry(QRect(20, 280, 41, 31))
        self.label_ke_start = QLabel(self.tab_settings)
        self.label_ke_start.setObjectName(u"label_ke_start")
        self.label_ke_start.setGeometry(QRect(20, 260, 51, 16))
        self.text_edit_ke_end = QTextEdit(self.tab_settings)
        self.text_edit_ke_end.setObjectName(u"text_edit_ke_end")
        self.text_edit_ke_end.setGeometry(QRect(90, 280, 41, 31))
        self.label_ke_end = QLabel(self.tab_settings)
        self.label_ke_end.setObjectName(u"label_ke_end")
        self.label_ke_end.setGeometry(QRect(90, 260, 51, 16))
        self.text_edit_ke_bins = QTextEdit(self.tab_settings)
        self.text_edit_ke_bins.setObjectName(u"text_edit_ke_bins")
        self.text_edit_ke_bins.setGeometry(QRect(160, 280, 41, 31))
        self.label_ke_bins = QLabel(self.tab_settings)
        self.label_ke_bins.setObjectName(u"label_ke_bins")
        self.label_ke_bins.setGeometry(QRect(160, 260, 51, 16))
        self.label_abel_inversion_data_path = QLabel(self.tab_settings)
        self.label_abel_inversion_data_path.setObjectName(u"label_abel_inversion_data_path")
        self.label_abel_inversion_data_path.setGeometry(QRect(20, 340, 131, 16))
        self.text_edit_abel_inversion_data_path = QTextEdit(self.tab_settings)
        self.text_edit_abel_inversion_data_path.setObjectName(u"text_edit_abel_inversion_data_path")
        self.text_edit_abel_inversion_data_path.setGeometry(QRect(20, 360, 171, 31))
        self.label_subfolder_extension = QLabel(self.tab_settings)
        self.label_subfolder_extension.setObjectName(u"label_subfolder_extension")
        self.label_subfolder_extension.setGeometry(QRect(320, 70, 211, 16))
        self.text_edit_subfolder_extension = QTextEdit(self.tab_settings)
        self.text_edit_subfolder_extension.setObjectName(u"text_edit_subfolder_extension")
        self.text_edit_subfolder_extension.setGeometry(QRect(350, 90, 241, 31))
        self.label_subfolder_extension_2 = QLabel(self.tab_settings)
        self.label_subfolder_extension_2.setObjectName(u"label_subfolder_extension_2")
        self.label_subfolder_extension_2.setGeometry(QRect(320, 100, 31, 20))
        font = QFont()
        font.setPointSize(16)
        self.label_subfolder_extension_2.setFont(font)
        self.text_edit_num_cores = QTextEdit(self.tab_settings)
        self.text_edit_num_cores.setObjectName(u"text_edit_num_cores")
        self.text_edit_num_cores.setGeometry(QRect(20, 422, 41, 31))
        self.label_num_cores = QLabel(self.tab_settings)
        self.label_num_cores.setObjectName(u"label_num_cores")
        self.label_num_cores.setGeometry(QRect(20, 400, 171, 16))
        self.tabWidget.addTab(self.tab_settings, "")
        self.print_browser = QTextBrowser(self.centralwidget)
        self.print_browser.setObjectName(u"print_browser")
        self.print_browser.setGeometry(QRect(20, 530, 621, 91))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 662, 21))
        self.menuFERMI_On_line_analysis_tool = QMenu(self.menubar)
        self.menuFERMI_On_line_analysis_tool.setObjectName(u"menuFERMI_On_line_analysis_tool")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFERMI_On_line_analysis_tool.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(5)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_fetch_new_files.setText(QCoreApplication.translate("MainWindow", u"Fetch new files", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Fore", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Back", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"Subt", None))
        self.box_pes.setText(QCoreApplication.translate("MainWindow", u"PES", None))
        self.box_beta1.setText(QCoreApplication.translate("MainWindow", u"beta1", None))
        self.box_beta2.setText(QCoreApplication.translate("MainWindow", u"beta2", None))
        self.box_beta3.setText(QCoreApplication.translate("MainWindow", u"beta3", None))
        self.box_beta4.setText(QCoreApplication.translate("MainWindow", u"beta4", None))
        self.label_files_used.setText(QCoreApplication.translate("MainWindow", u"Files used", None))
        self.label_current_folder.setText(QCoreApplication.translate("MainWindow", u"Current folder", None))
        self.label_update_status.setText(QCoreApplication.translate("MainWindow", u"Update status:", None))
        self.text_display_update_status.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Stopped</p></body></html>", None))
        self.button_stop_fetch.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_abel_inversion.setText(QCoreApplication.translate("MainWindow", u"Abel inversion", None))
        self.button_auto_newest_folder.setText(QCoreApplication.translate("MainWindow", u"Auto newest folder", None))
        self.button_stay_current_folder.setText(QCoreApplication.translate("MainWindow", u"Stay current folder", None))
        self.test_display_folder_status.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Stay</p></body></html>", None))
        self.label_folder_status.setText(QCoreApplication.translate("MainWindow", u"Folder status:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_vmi_main), QCoreApplication.translate("MainWindow", u"VMI Main", None))
        self.label_raw_image.setText(QCoreApplication.translate("MainWindow", u"Raw", None))
        self.label_corrected_image.setText(QCoreApplication.translate("MainWindow", u"Corrected", None))
        self.button_apply_vmi_corrections.setText(QCoreApplication.translate("MainWindow", u"Apply correction", None))
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
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Correction parameters", None))
        self.text_edit_correct_yzoom.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.label_correct_ycenter.setText(QCoreApplication.translate("MainWindow", u"y-center", None))
        self.text_edit_correct_rotate.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None))
        self.text_edit_correct_xcenter.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None))
        self.text_edit_correct_xzoom.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.text_edit_correct_ycenter.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None))
        self.label_correct_rotate.setText(QCoreApplication.translate("MainWindow", u"rotate", None))
        self.label_correct_xzoom.setText(QCoreApplication.translate("MainWindow", u"x-zoom", None))
        self.label_correct_xcenter.setText(QCoreApplication.translate("MainWindow", u"x-center", None))
        self.label_correct_yzoom.setText(QCoreApplication.translate("MainWindow", u"y-zoom", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_image_correction), QCoreApplication.translate("MainWindow", u"Image", None))
        self.label_pixel_axis.setText(QCoreApplication.translate("MainWindow", u"Pixels", None))
        self.label_energy_axis.setText(QCoreApplication.translate("MainWindow", u"Energies", None))
        self.test_edit_cal_points.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0, 0</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_cal_points.setText(QCoreApplication.translate("MainWindow", u"Pixel, Energy", None))
        self.button_apply_calibration.setText(QCoreApplication.translate("MainWindow", u"Apply calibration", None))
        self.label_pes_cal_constants.setText(QCoreApplication.translate("MainWindow", u"Cal. constant", None))
        self.text_display_cal_constant.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_pes_constant_alpha.setText(QCoreApplication.translate("MainWindow", u"alpha", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_calibration), QCoreApplication.translate("MainWindow", u"Cal. (PES)", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Fore", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"Back", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"Subt", None))
        self.combobox_tof_yscale.setItemText(0, QCoreApplication.translate("MainWindow", u"Linear", None))
        self.combobox_tof_yscale.setItemText(1, QCoreApplication.translate("MainWindow", u"Log", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tof_main), QCoreApplication.translate("MainWindow", u"TOF main", None))
        self.label_tof_axis.setText(QCoreApplication.translate("MainWindow", u"TOF", None))
        self.label_mq_axis.setText(QCoreApplication.translate("MainWindow", u"mass/charge", None))
        self.label_tof_cal_points.setText(QCoreApplication.translate("MainWindow", u"TOF, m/q", None))
        self.test_edit_tof_cal_points.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0, 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1, 1</p></body></html>", None))
        self.text_display_tof_constant_t0.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_tof_constants.setText(QCoreApplication.translate("MainWindow", u"Cal. constant", None))
        self.button_apply_tof_calibration.setText(QCoreApplication.translate("MainWindow", u"Apply calibration", None))
        self.text_display_tof_constant_c.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_tof_constant_c.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.label_tof_constant_t0.setText(QCoreApplication.translate("MainWindow", u"t0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tof_calibration), QCoreApplication.translate("MainWindow", u"Cal. (TOF)", None))
        self.label_search_dir_for_newest_folder.setText(QCoreApplication.translate("MainWindow", u"Auto-search newest folder in directory", None))
        self.label_tof_start.setText(QCoreApplication.translate("MainWindow", u"TOF start", None))
        self.text_edit_tof_start.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">None</p></body></html>", None))
        self.label_tof_stop.setText(QCoreApplication.translate("MainWindow", u"TOF stop", None))
        self.text_edit_tof_stop.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">None</p></body></html>", None))
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
        self.text_edit_ke_start.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">None</p></body></html>", None))
        self.label_ke_start.setText(QCoreApplication.translate("MainWindow", u"KE start", None))
        self.text_edit_ke_end.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">None</p></body></html>", None))
        self.label_ke_end.setText(QCoreApplication.translate("MainWindow", u"KE end", None))
        self.text_edit_ke_bins.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">None</p></body></html>", None))
        self.label_ke_bins.setText(QCoreApplication.translate("MainWindow", u"KE bins", None))
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
        self.label_subfolder_extension_2.setText(QCoreApplication.translate("MainWindow", u"../", None))
        self.text_edit_num_cores.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.label_num_cores.setText(QCoreApplication.translate("MainWindow", u"Max # cores for multiprocess", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuFERMI_On_line_analysis_tool.setTitle(QCoreApplication.translate("MainWindow", u"FERMI LDM On-line analysis tool", None))
    # retranslateUi

