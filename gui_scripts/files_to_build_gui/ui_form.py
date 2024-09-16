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
        MainWindow.resize(776, 728)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(10, 10, 761, 571))
        self.tabWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.tabWidget.setStyleSheet(u"")
        self.tab_vmi_main = QWidget()
        self.tab_vmi_main.setObjectName(u"tab_vmi_main")
        self.scrollArea = QScrollArea(self.tab_vmi_main)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(210, 120, 161, 161))
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
        self.button_fetch_new_files = QCommandLinkButton(self.tab_vmi_main)
        self.button_fetch_new_files.setObjectName(u"button_fetch_new_files")
        self.button_fetch_new_files.setGeometry(QRect(10, 240, 181, 31))
        self.tabWidget_2 = QTabWidget(self.tab_vmi_main)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(440, 10, 311, 321))
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
        self.scrollArea_2.setGeometry(QRect(30, 350, 91, 154))
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
        self.label_files_used.setGeometry(QRect(210, 100, 61, 16))
        self.label_current_folder = QLabel(self.tab_vmi_main)
        self.label_current_folder.setObjectName(u"label_current_folder")
        self.label_current_folder.setGeometry(QRect(20, 10, 81, 16))
        self.text_edit_current_folder = QTextEdit(self.tab_vmi_main)
        self.text_edit_current_folder.setObjectName(u"text_edit_current_folder")
        self.text_edit_current_folder.setGeometry(QRect(20, 30, 351, 41))
        self.label_update_status = QLabel(self.tab_vmi_main)
        self.label_update_status.setObjectName(u"label_update_status")
        self.label_update_status.setGeometry(QRect(20, 210, 91, 16))
        self.text_display_update_status = QTextBrowser(self.tab_vmi_main)
        self.text_display_update_status.setObjectName(u"text_display_update_status")
        self.text_display_update_status.setGeometry(QRect(100, 210, 71, 31))
        self.button_stop_fetch = QCommandLinkButton(self.tab_vmi_main)
        self.button_stop_fetch.setObjectName(u"button_stop_fetch")
        self.button_stop_fetch.setGeometry(QRect(10, 270, 181, 31))
        self.label_abel_inversion = QLabel(self.tab_vmi_main)
        self.label_abel_inversion.setObjectName(u"label_abel_inversion")
        self.label_abel_inversion.setGeometry(QRect(20, 330, 91, 16))
        self.button_auto_newest_folder = QCommandLinkButton(self.tab_vmi_main)
        self.button_auto_newest_folder.setObjectName(u"button_auto_newest_folder")
        self.button_auto_newest_folder.setGeometry(QRect(10, 130, 181, 31))
        self.button_stay_current_folder = QCommandLinkButton(self.tab_vmi_main)
        self.button_stay_current_folder.setObjectName(u"button_stay_current_folder")
        self.button_stay_current_folder.setGeometry(QRect(10, 160, 181, 31))
        self.test_display_folder_status = QTextBrowser(self.tab_vmi_main)
        self.test_display_folder_status.setObjectName(u"test_display_folder_status")
        self.test_display_folder_status.setGeometry(QRect(100, 100, 71, 31))
        self.label_folder_status = QLabel(self.tab_vmi_main)
        self.label_folder_status.setObjectName(u"label_folder_status")
        self.label_folder_status.setGeometry(QRect(20, 100, 91, 16))
        self.verticalLayoutWidget = QWidget(self.tab_vmi_main)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(150, 330, 601, 211))
        self.vmi_abel = QVBoxLayout(self.verticalLayoutWidget)
        self.vmi_abel.setObjectName(u"vmi_abel")
        self.vmi_abel.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_vmi_main, "")
        self.tab_image_correction = QWidget()
        self.tab_image_correction.setObjectName(u"tab_image_correction")
        self.groupBox_5 = QGroupBox(self.tab_image_correction)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(420, 390, 331, 141))
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
        self.button_apply_vmi_corrections = QCommandLinkButton(self.groupBox_5)
        self.button_apply_vmi_corrections.setObjectName(u"button_apply_vmi_corrections")
        self.button_apply_vmi_corrections.setGeometry(QRect(140, 100, 181, 41))
        self.tabWidget_4 = QTabWidget(self.tab_image_correction)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.tabWidget_4.setGeometry(QRect(10, 10, 361, 381))
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_6 = QGridLayout(self.tab_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.vmi_show_raw = QGridLayout()
        self.vmi_show_raw.setObjectName(u"vmi_show_raw")

        self.gridLayout_6.addLayout(self.vmi_show_raw, 0, 0, 1, 1)

        self.tabWidget_4.addTab(self.tab_4, "")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.gridLayout_11 = QGridLayout(self.tab_15)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.vmi_show_fit = QGridLayout()
        self.vmi_show_fit.setObjectName(u"vmi_show_fit")

        self.gridLayout_11.addLayout(self.vmi_show_fit, 0, 0, 1, 1)

        self.tabWidget_4.addTab(self.tab_15, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_7 = QGridLayout(self.tab_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.vmi_show_inverse = QGridLayout()
        self.vmi_show_inverse.setObjectName(u"vmi_show_inverse")

        self.gridLayout_7.addLayout(self.vmi_show_inverse, 0, 0, 1, 1)

        self.tabWidget_4.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_8 = QGridLayout(self.tab_6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.vmi_show_rdf = QGridLayout()
        self.vmi_show_rdf.setObjectName(u"vmi_show_rdf")

        self.gridLayout_8.addLayout(self.vmi_show_rdf, 0, 0, 1, 1)

        self.tabWidget_4.addTab(self.tab_6, "")
        self.tabWidget_5 = QTabWidget(self.tab_image_correction)
        self.tabWidget_5.setObjectName(u"tabWidget_5")
        self.tabWidget_5.setGeometry(QRect(380, 10, 371, 381))
        self.tabWidget_5.setStyleSheet(u"")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.gridLayout_9 = QGridLayout(self.tab_13)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.vmi_show_corr = QGridLayout()
        self.vmi_show_corr.setObjectName(u"vmi_show_corr")

        self.gridLayout_9.addLayout(self.vmi_show_corr, 0, 0, 1, 1)

        self.tabWidget_5.addTab(self.tab_13, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.gridLayout_10 = QGridLayout(self.tab_14)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.vmi_show_reduced = QGridLayout()
        self.vmi_show_reduced.setObjectName(u"vmi_show_reduced")

        self.gridLayout_10.addLayout(self.vmi_show_reduced, 0, 0, 1, 1)

        self.tabWidget_5.addTab(self.tab_14, "")
        self.text_edit_reduce_image_size = QTextEdit(self.tab_image_correction)
        self.text_edit_reduce_image_size.setObjectName(u"text_edit_reduce_image_size")
        self.text_edit_reduce_image_size.setGeometry(QRect(320, 430, 51, 31))
        self.label_reduce_image_size = QLabel(self.tab_image_correction)
        self.label_reduce_image_size.setObjectName(u"label_reduce_image_size")
        self.label_reduce_image_size.setGeometry(QRect(300, 410, 101, 16))
        self.text_browser_gdata_image_size = QTextBrowser(self.tab_image_correction)
        self.text_browser_gdata_image_size.setObjectName(u"text_browser_gdata_image_size")
        self.text_browser_gdata_image_size.setGeometry(QRect(320, 490, 51, 31))
        self.text_browser_gdata_image_size.setStyleSheet(u"background-color: rgb(144, 144, 144);")
        self.label_gdata_image_size = QLabel(self.tab_image_correction)
        self.label_gdata_image_size.setObjectName(u"label_gdata_image_size")
        self.label_gdata_image_size.setGeometry(QRect(300, 470, 101, 16))
        self.groupBox_4 = QGroupBox(self.tab_image_correction)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 390, 281, 141))
        self.label_guess_ycenter = QLabel(self.groupBox_4)
        self.label_guess_ycenter.setObjectName(u"label_guess_ycenter")
        self.label_guess_ycenter.setGeometry(QRect(80, 20, 49, 16))
        self.label_guess_rotate = QLabel(self.groupBox_4)
        self.label_guess_rotate.setObjectName(u"label_guess_rotate")
        self.label_guess_rotate.setGeometry(QRect(160, 20, 49, 16))
        self.label_guess_xzoom = QLabel(self.groupBox_4)
        self.label_guess_xzoom.setObjectName(u"label_guess_xzoom")
        self.label_guess_xzoom.setGeometry(QRect(10, 80, 49, 16))
        self.label_guess_xcenter = QLabel(self.groupBox_4)
        self.label_guess_xcenter.setObjectName(u"label_guess_xcenter")
        self.label_guess_xcenter.setGeometry(QRect(10, 20, 49, 16))
        self.label_guess_yzoom = QLabel(self.groupBox_4)
        self.label_guess_yzoom.setObjectName(u"label_guess_yzoom")
        self.label_guess_yzoom.setGeometry(QRect(80, 80, 49, 16))
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
        self.text_display_guess_xzoom.setGeometry(QRect(10, 100, 51, 31))
        self.text_diesplay_guess_yzoom = QTextBrowser(self.groupBox_4)
        self.text_diesplay_guess_yzoom.setObjectName(u"text_diesplay_guess_yzoom")
        self.text_diesplay_guess_yzoom.setGeometry(QRect(80, 100, 51, 31))
        self.button_get_guess_vmi_corrections = QCommandLinkButton(self.tab_image_correction)
        self.button_get_guess_vmi_corrections.setObjectName(u"button_get_guess_vmi_corrections")
        self.button_get_guess_vmi_corrections.setGeometry(QRect(160, 490, 131, 41))
        self.tabWidget.addTab(self.tab_image_correction, "")
        self.groupBox_5.raise_()
        self.tabWidget_4.raise_()
        self.text_edit_reduce_image_size.raise_()
        self.label_reduce_image_size.raise_()
        self.text_browser_gdata_image_size.raise_()
        self.label_gdata_image_size.raise_()
        self.groupBox_4.raise_()
        self.button_get_guess_vmi_corrections.raise_()
        self.tabWidget_5.raise_()
        self.tab_calibration = QWidget()
        self.tab_calibration.setObjectName(u"tab_calibration")
        self.gridLayoutWidget_5 = QWidget(self.tab_calibration)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(0, 0, 451, 261))
        self.pes_show_pixels = QGridLayout(self.gridLayoutWidget_5)
        self.pes_show_pixels.setObjectName(u"pes_show_pixels")
        self.pes_show_pixels.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutWidget_6 = QWidget(self.tab_calibration)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(0, 270, 451, 261))
        self.pes_show_energy = QGridLayout(self.gridLayoutWidget_6)
        self.pes_show_energy.setObjectName(u"pes_show_energy")
        self.pes_show_energy.setContentsMargins(0, 0, 0, 0)
        self.label_pixel_axis = QLabel(self.tab_calibration)
        self.label_pixel_axis.setObjectName(u"label_pixel_axis")
        self.label_pixel_axis.setGeometry(QRect(40, 20, 49, 16))
        self.label_energy_axis = QLabel(self.tab_calibration)
        self.label_energy_axis.setObjectName(u"label_energy_axis")
        self.label_energy_axis.setGeometry(QRect(40, 290, 49, 16))
        self.test_edit_cal_points = QTextEdit(self.tab_calibration)
        self.test_edit_cal_points.setObjectName(u"test_edit_cal_points")
        self.test_edit_cal_points.setGeometry(QRect(470, 240, 91, 131))
        self.label_cal_points = QLabel(self.tab_calibration)
        self.label_cal_points.setObjectName(u"label_cal_points")
        self.label_cal_points.setGeometry(QRect(480, 210, 71, 21))
        self.button_apply_pes_calibration = QCommandLinkButton(self.tab_calibration)
        self.button_apply_pes_calibration.setObjectName(u"button_apply_pes_calibration")
        self.button_apply_pes_calibration.setGeometry(QRect(460, 370, 172, 41))
        self.label_pes_cal_constants = QLabel(self.tab_calibration)
        self.label_pes_cal_constants.setObjectName(u"label_pes_cal_constants")
        self.label_pes_cal_constants.setGeometry(QRect(640, 210, 91, 21))
        self.text_display_cal_constant = QTextBrowser(self.tab_calibration)
        self.text_display_cal_constant.setObjectName(u"text_display_cal_constant")
        self.text_display_cal_constant.setGeometry(QRect(620, 240, 121, 31))
        self.label_pes_constant_alpha = QLabel(self.tab_calibration)
        self.label_pes_constant_alpha.setObjectName(u"label_pes_constant_alpha")
        self.label_pes_constant_alpha.setGeometry(QRect(580, 240, 61, 16))
        self.text_edit_ke_start = QTextEdit(self.tab_calibration)
        self.text_edit_ke_start.setObjectName(u"text_edit_ke_start")
        self.text_edit_ke_start.setGeometry(QRect(550, 500, 41, 31))
        self.text_edit_ke_end = QTextEdit(self.tab_calibration)
        self.text_edit_ke_end.setObjectName(u"text_edit_ke_end")
        self.text_edit_ke_end.setGeometry(QRect(620, 500, 41, 31))
        self.label_ke_start = QLabel(self.tab_calibration)
        self.label_ke_start.setObjectName(u"label_ke_start")
        self.label_ke_start.setGeometry(QRect(550, 480, 51, 16))
        self.label_ke_bins = QLabel(self.tab_calibration)
        self.label_ke_bins.setObjectName(u"label_ke_bins")
        self.label_ke_bins.setGeometry(QRect(690, 480, 51, 16))
        self.text_edit_ke_bins = QTextEdit(self.tab_calibration)
        self.text_edit_ke_bins.setObjectName(u"text_edit_ke_bins")
        self.text_edit_ke_bins.setGeometry(QRect(690, 500, 41, 31))
        self.label_ke_end = QLabel(self.tab_calibration)
        self.label_ke_end.setObjectName(u"label_ke_end")
        self.label_ke_end.setGeometry(QRect(620, 480, 51, 16))
        self.gridLayoutWidget_10 = QWidget(self.tab_calibration)
        self.gridLayoutWidget_10.setObjectName(u"gridLayoutWidget_10")
        self.gridLayoutWidget_10.setGeometry(QRect(450, 0, 301, 211))
        self.eke_show_calibration = QGridLayout(self.gridLayoutWidget_10)
        self.eke_show_calibration.setObjectName(u"eke_show_calibration")
        self.eke_show_calibration.setContentsMargins(0, 0, 0, 0)
        self.label_eke_calibration = QLabel(self.tab_calibration)
        self.label_eke_calibration.setObjectName(u"label_eke_calibration")
        self.label_eke_calibration.setGeometry(QRect(490, 20, 161, 16))
        self.button_apply_pes_use_constants = QCommandLinkButton(self.tab_calibration)
        self.button_apply_pes_use_constants.setObjectName(u"button_apply_pes_use_constants")
        self.button_apply_pes_use_constants.setGeometry(QRect(610, 310, 131, 41))
        self.tabWidget.addTab(self.tab_calibration, "")
        self.tab_tof_main = QWidget()
        self.tab_tof_main.setObjectName(u"tab_tof_main")
        self.tabWidget_3 = QTabWidget(self.tab_tof_main)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setGeometry(QRect(10, 10, 741, 361))
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.tab_9.setAutoFillBackground(False)
        self.gridLayout_20 = QGridLayout(self.tab_9)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.tof_fore = QGridLayout()
        self.tof_fore.setObjectName(u"tof_fore")

        self.gridLayout_20.addLayout(self.tof_fore, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_9, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.gridLayout_21 = QGridLayout(self.tab_11)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.tof_back = QGridLayout()
        self.tof_back.setObjectName(u"tof_back")

        self.gridLayout_21.addLayout(self.tof_back, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_11, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.gridLayout_22 = QGridLayout(self.tab_12)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.tof_subt = QGridLayout()
        self.tof_subt.setObjectName(u"tof_subt")

        self.gridLayout_22.addLayout(self.tof_subt, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_12, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mq_fore = QGridLayout()
        self.mq_fore.setObjectName(u"mq_fore")

        self.gridLayout.addLayout(self.mq_fore, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_2 = QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.mq_back = QGridLayout()
        self.mq_back.setObjectName(u"mq_back")

        self.gridLayout_2.addLayout(self.mq_back, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.mq_subt = QGridLayout()
        self.mq_subt.setObjectName(u"mq_subt")

        self.gridLayout_3.addLayout(self.mq_subt, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab, "")
        self.combobox_tof_yscale = QComboBox(self.tab_tof_main)
        self.combobox_tof_yscale.addItem("")
        self.combobox_tof_yscale.addItem("")
        self.combobox_tof_yscale.setObjectName(u"combobox_tof_yscale")
        self.combobox_tof_yscale.setGeometry(QRect(580, 390, 131, 21))
        self.text_edit_current_folder_2 = QTextEdit(self.tab_tof_main)
        self.text_edit_current_folder_2.setObjectName(u"text_edit_current_folder_2")
        self.text_edit_current_folder_2.setGeometry(QRect(20, 400, 341, 31))
        self.button_fetch_new_files_2 = QCommandLinkButton(self.tab_tof_main)
        self.button_fetch_new_files_2.setObjectName(u"button_fetch_new_files_2")
        self.button_fetch_new_files_2.setGeometry(QRect(200, 470, 181, 31))
        self.label_update_status_2 = QLabel(self.tab_tof_main)
        self.label_update_status_2.setObjectName(u"label_update_status_2")
        self.label_update_status_2.setGeometry(QRect(210, 440, 91, 16))
        self.label_current_folder_2 = QLabel(self.tab_tof_main)
        self.label_current_folder_2.setObjectName(u"label_current_folder_2")
        self.label_current_folder_2.setGeometry(QRect(20, 380, 81, 16))
        self.label_folder_status_2 = QLabel(self.tab_tof_main)
        self.label_folder_status_2.setObjectName(u"label_folder_status_2")
        self.label_folder_status_2.setGeometry(QRect(20, 440, 91, 16))
        self.button_stay_current_folder_2 = QCommandLinkButton(self.tab_tof_main)
        self.button_stay_current_folder_2.setObjectName(u"button_stay_current_folder_2")
        self.button_stay_current_folder_2.setGeometry(QRect(10, 500, 181, 31))
        self.text_display_update_status_2 = QTextBrowser(self.tab_tof_main)
        self.text_display_update_status_2.setObjectName(u"text_display_update_status_2")
        self.text_display_update_status_2.setGeometry(QRect(290, 440, 71, 31))
        self.test_display_folder_status_2 = QTextBrowser(self.tab_tof_main)
        self.test_display_folder_status_2.setObjectName(u"test_display_folder_status_2")
        self.test_display_folder_status_2.setGeometry(QRect(100, 440, 71, 31))
        self.button_stop_fetch_2 = QCommandLinkButton(self.tab_tof_main)
        self.button_stop_fetch_2.setObjectName(u"button_stop_fetch_2")
        self.button_stop_fetch_2.setGeometry(QRect(200, 500, 181, 31))
        self.button_auto_newest_folder_2 = QCommandLinkButton(self.tab_tof_main)
        self.button_auto_newest_folder_2.setObjectName(u"button_auto_newest_folder_2")
        self.button_auto_newest_folder_2.setGeometry(QRect(10, 470, 181, 31))
        self.tabWidget.addTab(self.tab_tof_main, "")
        self.tab_tof_calibration = QWidget()
        self.tab_tof_calibration.setObjectName(u"tab_tof_calibration")
        self.gridLayoutWidget_7 = QWidget(self.tab_tof_calibration)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(0, 0, 451, 261))
        self.tof_show_raw = QGridLayout(self.gridLayoutWidget_7)
        self.tof_show_raw.setObjectName(u"tof_show_raw")
        self.tof_show_raw.setContentsMargins(0, 0, 0, 0)
        self.label_tof_axis = QLabel(self.tab_tof_calibration)
        self.label_tof_axis.setObjectName(u"label_tof_axis")
        self.label_tof_axis.setGeometry(QRect(140, 20, 111, 16))
        self.label_mq_axis = QLabel(self.tab_tof_calibration)
        self.label_mq_axis.setObjectName(u"label_mq_axis")
        self.label_mq_axis.setGeometry(QRect(140, 290, 101, 16))
        self.label_tof_cal_points = QLabel(self.tab_tof_calibration)
        self.label_tof_cal_points.setObjectName(u"label_tof_cal_points")
        self.label_tof_cal_points.setGeometry(QRect(480, 210, 71, 21))
        self.gridLayoutWidget_8 = QWidget(self.tab_tof_calibration)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(0, 270, 451, 261))
        self.tof_show_mq = QGridLayout(self.gridLayoutWidget_8)
        self.tof_show_mq.setObjectName(u"tof_show_mq")
        self.tof_show_mq.setContentsMargins(0, 0, 0, 0)
        self.text_edit_tof_cal_points = QTextEdit(self.tab_tof_calibration)
        self.text_edit_tof_cal_points.setObjectName(u"text_edit_tof_cal_points")
        self.text_edit_tof_cal_points.setGeometry(QRect(470, 240, 91, 131))
        self.text_edit_tof_constant_t0 = QTextEdit(self.tab_tof_calibration)
        self.text_edit_tof_constant_t0.setObjectName(u"text_edit_tof_constant_t0")
        self.text_edit_tof_constant_t0.setGeometry(QRect(610, 270, 131, 31))
        self.label_tof_constants = QLabel(self.tab_tof_calibration)
        self.label_tof_constants.setObjectName(u"label_tof_constants")
        self.label_tof_constants.setGeometry(QRect(640, 210, 91, 21))
        self.button_apply_tof_calibration = QCommandLinkButton(self.tab_tof_calibration)
        self.button_apply_tof_calibration.setObjectName(u"button_apply_tof_calibration")
        self.button_apply_tof_calibration.setGeometry(QRect(460, 370, 161, 41))
        self.text_edit_tof_constant_c = QTextEdit(self.tab_tof_calibration)
        self.text_edit_tof_constant_c.setObjectName(u"text_edit_tof_constant_c")
        self.text_edit_tof_constant_c.setGeometry(QRect(610, 240, 131, 31))
        self.label_tof_constant_c = QLabel(self.tab_tof_calibration)
        self.label_tof_constant_c.setObjectName(u"label_tof_constant_c")
        self.label_tof_constant_c.setGeometry(QRect(590, 240, 31, 16))
        self.label_tof_constant_t0 = QLabel(self.tab_tof_calibration)
        self.label_tof_constant_t0.setObjectName(u"label_tof_constant_t0")
        self.label_tof_constant_t0.setGeometry(QRect(590, 270, 31, 16))
        self.label_mq_end = QLabel(self.tab_tof_calibration)
        self.label_mq_end.setObjectName(u"label_mq_end")
        self.label_mq_end.setGeometry(QRect(620, 480, 51, 16))
        self.label_mq_start = QLabel(self.tab_tof_calibration)
        self.label_mq_start.setObjectName(u"label_mq_start")
        self.label_mq_start.setGeometry(QRect(550, 480, 51, 16))
        self.text_edit_tof_end = QTextEdit(self.tab_tof_calibration)
        self.text_edit_tof_end.setObjectName(u"text_edit_tof_end")
        self.text_edit_tof_end.setGeometry(QRect(620, 440, 41, 31))
        self.text_edit_mq_end = QTextEdit(self.tab_tof_calibration)
        self.text_edit_mq_end.setObjectName(u"text_edit_mq_end")
        self.text_edit_mq_end.setGeometry(QRect(620, 500, 41, 31))
        self.text_edit_mq_bins = QTextEdit(self.tab_tof_calibration)
        self.text_edit_mq_bins.setObjectName(u"text_edit_mq_bins")
        self.text_edit_mq_bins.setGeometry(QRect(690, 500, 41, 31))
        self.label_mq_bins = QLabel(self.tab_tof_calibration)
        self.label_mq_bins.setObjectName(u"label_mq_bins")
        self.label_mq_bins.setGeometry(QRect(690, 480, 51, 16))
        self.label_tof_end = QLabel(self.tab_tof_calibration)
        self.label_tof_end.setObjectName(u"label_tof_end")
        self.label_tof_end.setGeometry(QRect(620, 420, 51, 16))
        self.text_edit_mq_start = QTextEdit(self.tab_tof_calibration)
        self.text_edit_mq_start.setObjectName(u"text_edit_mq_start")
        self.text_edit_mq_start.setGeometry(QRect(550, 500, 41, 31))
        self.text_edit_tof_start = QTextEdit(self.tab_tof_calibration)
        self.text_edit_tof_start.setObjectName(u"text_edit_tof_start")
        self.text_edit_tof_start.setGeometry(QRect(550, 440, 41, 31))
        self.label_tof_start = QLabel(self.tab_tof_calibration)
        self.label_tof_start.setObjectName(u"label_tof_start")
        self.label_tof_start.setGeometry(QRect(550, 420, 51, 16))
        self.label_tof_bins = QLabel(self.tab_tof_calibration)
        self.label_tof_bins.setObjectName(u"label_tof_bins")
        self.label_tof_bins.setGeometry(QRect(690, 420, 51, 16))
        self.text_edit_tof_bins = QTextEdit(self.tab_tof_calibration)
        self.text_edit_tof_bins.setObjectName(u"text_edit_tof_bins")
        self.text_edit_tof_bins.setGeometry(QRect(690, 440, 41, 31))
        self.gridLayoutWidget_9 = QWidget(self.tab_tof_calibration)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(450, 0, 301, 211))
        self.tof_show_calibration = QGridLayout(self.gridLayoutWidget_9)
        self.tof_show_calibration.setObjectName(u"tof_show_calibration")
        self.tof_show_calibration.setContentsMargins(0, 0, 0, 0)
        self.label_tof_calibration = QLabel(self.tab_tof_calibration)
        self.label_tof_calibration.setObjectName(u"label_tof_calibration")
        self.label_tof_calibration.setGeometry(QRect(490, 20, 161, 16))
        self.button_apply_tof_use_constants = QCommandLinkButton(self.tab_tof_calibration)
        self.button_apply_tof_use_constants.setObjectName(u"button_apply_tof_use_constants")
        self.button_apply_tof_use_constants.setGeometry(QRect(610, 310, 131, 41))
        self.tabWidget.addTab(self.tab_tof_calibration, "")
        self.gridLayoutWidget_7.raise_()
        self.label_tof_cal_points.raise_()
        self.gridLayoutWidget_8.raise_()
        self.text_edit_tof_cal_points.raise_()
        self.text_edit_tof_constant_t0.raise_()
        self.label_tof_constants.raise_()
        self.button_apply_tof_calibration.raise_()
        self.text_edit_tof_constant_c.raise_()
        self.label_tof_constant_c.raise_()
        self.label_tof_constant_t0.raise_()
        self.label_mq_end.raise_()
        self.label_mq_start.raise_()
        self.text_edit_tof_end.raise_()
        self.text_edit_mq_end.raise_()
        self.text_edit_mq_bins.raise_()
        self.label_mq_bins.raise_()
        self.label_tof_end.raise_()
        self.text_edit_mq_start.raise_()
        self.text_edit_tof_start.raise_()
        self.label_tof_start.raise_()
        self.label_tof_bins.raise_()
        self.text_edit_tof_bins.raise_()
        self.gridLayoutWidget_9.raise_()
        self.label_tof_axis.raise_()
        self.label_mq_axis.raise_()
        self.label_tof_calibration.raise_()
        self.button_apply_tof_use_constants.raise_()
        self.tab_settings = QWidget()
        self.tab_settings.setObjectName(u"tab_settings")
        self.label_search_dir_for_newest_folder = QLabel(self.tab_settings)
        self.label_search_dir_for_newest_folder.setObjectName(u"label_search_dir_for_newest_folder")
        self.label_search_dir_for_newest_folder.setGeometry(QRect(320, 10, 211, 16))
        self.text_edit_search_dir_for_newest_folder = QTextEdit(self.tab_settings)
        self.text_edit_search_dir_for_newest_folder.setObjectName(u"text_edit_search_dir_for_newest_folder")
        self.text_edit_search_dir_for_newest_folder.setGeometry(QRect(320, 30, 271, 31))
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
        self.box_slu_parity.setGeometry(QRect(320, 330, 21, 22))
        self.label_slu_parity = QLabel(self.tab_settings)
        self.label_slu_parity.setObjectName(u"label_slu_parity")
        self.label_slu_parity.setGeometry(QRect(350, 330, 121, 16))
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
        self.label_abel_inversion_data_path = QLabel(self.tab_settings)
        self.label_abel_inversion_data_path.setObjectName(u"label_abel_inversion_data_path")
        self.label_abel_inversion_data_path.setGeometry(QRect(20, 330, 131, 16))
        self.text_edit_abel_inversion_data_path = QTextEdit(self.tab_settings)
        self.text_edit_abel_inversion_data_path.setObjectName(u"text_edit_abel_inversion_data_path")
        self.text_edit_abel_inversion_data_path.setGeometry(QRect(20, 350, 171, 31))
        self.label_subfolder_extension = QLabel(self.tab_settings)
        self.label_subfolder_extension.setObjectName(u"label_subfolder_extension")
        self.label_subfolder_extension.setGeometry(QRect(320, 70, 211, 16))
        self.text_edit_subfolder_extension = QTextEdit(self.tab_settings)
        self.text_edit_subfolder_extension.setObjectName(u"text_edit_subfolder_extension")
        self.text_edit_subfolder_extension.setGeometry(QRect(350, 90, 241, 31))
        self.label_subfolder_extension_2 = QLabel(self.tab_settings)
        self.label_subfolder_extension_2.setObjectName(u"label_subfolder_extension_2")
        self.label_subfolder_extension_2.setGeometry(QRect(330, 89, 21, 31))
        font = QFont()
        font.setPointSize(16)
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
        self.text_edit_search_dir_for_newest_folder_2 = QTextEdit(self.tab_settings)
        self.text_edit_search_dir_for_newest_folder_2.setObjectName(u"text_edit_search_dir_for_newest_folder_2")
        self.text_edit_search_dir_for_newest_folder_2.setGeometry(QRect(600, 30, 141, 31))
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
        self.tabWidget.addTab(self.tab_settings, "")
        self.print_browser = QTextBrowser(self.centralwidget)
        self.print_browser.setObjectName(u"print_browser")
        self.print_browser.setGeometry(QRect(10, 580, 761, 91))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 776, 21))
        self.menuFERMI_On_line_analysis_tool = QMenu(self.menubar)
        self.menuFERMI_On_line_analysis_tool.setObjectName(u"menuFERMI_On_line_analysis_tool")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFERMI_On_line_analysis_tool.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(5)
        self.tabWidget_2.setCurrentIndex(2)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
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
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Raw", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_15), QCoreApplication.translate("MainWindow", u"Fit", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Inverse", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Radial dist.", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"Corrected", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"Reduced", None))
        self.text_edit_reduce_image_size.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_reduce_image_size.setText(QCoreApplication.translate("MainWindow", u"Reduce image size", None))
        self.label_gdata_image_size.setText(QCoreApplication.translate("MainWindow", u"gdata image size", None))
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
        self.button_apply_pes_calibration.setText(QCoreApplication.translate("MainWindow", u"Apply calibration", None))
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
        self.text_edit_ke_start.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_edit_ke_end.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_ke_start.setText(QCoreApplication.translate("MainWindow", u"KE start", None))
        self.label_ke_bins.setText(QCoreApplication.translate("MainWindow", u"KE bins", None))
        self.text_edit_ke_bins.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_ke_end.setText(QCoreApplication.translate("MainWindow", u"KE end", None))
        self.label_eke_calibration.setText(QCoreApplication.translate("MainWindow", u"Calibration fit", None))
        self.button_apply_pes_use_constants.setText(QCoreApplication.translate("MainWindow", u"Use constants", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_calibration), QCoreApplication.translate("MainWindow", u"Cal. (PES)", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Fore", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"Back", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"Subt", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Fore (m/q)", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Back (m/q)", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Subt (m/q)", None))
        self.combobox_tof_yscale.setItemText(0, QCoreApplication.translate("MainWindow", u"Linear", None))
        self.combobox_tof_yscale.setItemText(1, QCoreApplication.translate("MainWindow", u"Log", None))

        self.button_fetch_new_files_2.setText(QCoreApplication.translate("MainWindow", u"Fetch new files", None))
        self.label_update_status_2.setText(QCoreApplication.translate("MainWindow", u"Update status:", None))
        self.label_current_folder_2.setText(QCoreApplication.translate("MainWindow", u"Current folder", None))
        self.label_folder_status_2.setText(QCoreApplication.translate("MainWindow", u"Folder status:", None))
        self.button_stay_current_folder_2.setText(QCoreApplication.translate("MainWindow", u"Stay current folder", None))
        self.text_display_update_status_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Stopped</p></body></html>", None))
        self.test_display_folder_status_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Stay</p></body></html>", None))
        self.button_stop_fetch_2.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.button_auto_newest_folder_2.setText(QCoreApplication.translate("MainWindow", u"Auto newest folder", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tof_main), QCoreApplication.translate("MainWindow", u"TOF main", None))
        self.label_tof_axis.setText(QCoreApplication.translate("MainWindow", u"TOF", None))
        self.label_mq_axis.setText(QCoreApplication.translate("MainWindow", u"Mass/Charge", None))
        self.label_tof_cal_points.setText(QCoreApplication.translate("MainWindow", u"TOF, m/q", None))
        self.text_edit_tof_cal_points.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0, 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1, 1</p></body></html>", None))
        self.text_edit_tof_constant_t0.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_tof_constants.setText(QCoreApplication.translate("MainWindow", u"Cal. constants", None))
        self.button_apply_tof_calibration.setText(QCoreApplication.translate("MainWindow", u"Apply calibration", None))
        self.text_edit_tof_constant_c.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_tof_constant_c.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.label_tof_constant_t0.setText(QCoreApplication.translate("MainWindow", u"t0", None))
        self.label_mq_end.setText(QCoreApplication.translate("MainWindow", u"m/q end", None))
        self.label_mq_start.setText(QCoreApplication.translate("MainWindow", u"m/q start", None))
        self.text_edit_tof_end.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_edit_mq_end.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_edit_mq_bins.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_mq_bins.setText(QCoreApplication.translate("MainWindow", u"m/q bins", None))
        self.label_tof_end.setText(QCoreApplication.translate("MainWindow", u"TOF end", None))
        self.text_edit_mq_start.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_edit_tof_start.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_tof_start.setText(QCoreApplication.translate("MainWindow", u"TOF start", None))
        self.label_tof_bins.setText(QCoreApplication.translate("MainWindow", u"TOF bins", None))
        self.text_edit_tof_bins.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_tof_calibration.setText(QCoreApplication.translate("MainWindow", u"Calibration fit", None))
        self.button_apply_tof_use_constants.setText(QCoreApplication.translate("MainWindow", u"Use constants", None))
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
        self.label_num_cores.setText(QCoreApplication.translate("MainWindow", u"Max # cores for multiprocess", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuFERMI_On_line_analysis_tool.setTitle(QCoreApplication.translate("MainWindow", u"FERMI LDM On-line analysis tool", None))
    # retranslateUi

