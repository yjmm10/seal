# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'merge_image.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QDoubleSpinBox,
    QGraphicsView, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_Merge(object):
    def setupUi(self, Merge):
        if not Merge.objectName():
            Merge.setObjectName(u"Merge")
        Merge.resize(958, 667)
        self.groupBox = QGroupBox(Merge)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 50, 91, 51))
        self.gridLayoutWidget = QWidget(Merge)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(40, 110, 241, 186))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.back_pos_w = QLineEdit(self.gridLayoutWidget)
        self.back_pos_w.setObjectName(u"back_pos_w")

        self.horizontalLayout_2.addWidget(self.back_pos_w)

        self.back_pos_h = QLineEdit(self.gridLayoutWidget)
        self.back_pos_h.setObjectName(u"back_pos_h")

        self.horizontalLayout_2.addWidget(self.back_pos_h)


        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 1, 1, 1)

        self.back_path = QLineEdit(self.gridLayoutWidget)
        self.back_path.setObjectName(u"back_path")

        self.gridLayout.addWidget(self.back_path, 0, 1, 1, 1)

        self.back_padding = QCheckBox(self.gridLayoutWidget)
        self.back_padding.setObjectName(u"back_padding")

        self.gridLayout.addWidget(self.back_padding, 1, 1, 1, 1)

        self.fore_alpha = QDoubleSpinBox(self.gridLayoutWidget)
        self.fore_alpha.setObjectName(u"fore_alpha")
        self.fore_alpha.setMaximum(1.000000000000000)
        self.fore_alpha.setSingleStep(0.100000000000000)
        self.fore_alpha.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.fore_alpha, 4, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.fore_path = QLineEdit(self.gridLayoutWidget)
        self.fore_path.setObjectName(u"fore_path")

        self.gridLayout.addWidget(self.fore_path, 3, 1, 1, 1)

        self.fore_factor = QDoubleSpinBox(self.gridLayoutWidget)
        self.fore_factor.setObjectName(u"fore_factor")
        self.fore_factor.setMinimum(0.010000000000000)
        self.fore_factor.setMaximum(99.000000000000000)
        self.fore_factor.setSingleStep(0.100000000000000)
        self.fore_factor.setValue(1.000000000000000)

        self.gridLayout.addWidget(self.fore_factor, 6, 1, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 7, 0, 1, 1)

        self.single_save_image = QLineEdit(self.gridLayoutWidget)
        self.single_save_image.setObjectName(u"single_save_image")

        self.gridLayout.addWidget(self.single_save_image, 7, 1, 1, 1)

        self.back_view = QGraphicsView(Merge)
        self.back_view.setObjectName(u"back_view")
        self.back_view.setGeometry(QRect(330, 30, 281, 251))
        self.label_7 = QLabel(Merge)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(470, 290, 53, 16))
        self.label_8 = QLabel(Merge)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(660, 290, 53, 16))
        self.fore_view = QGraphicsView(Merge)
        self.fore_view.setObjectName(u"fore_view")
        self.fore_view.setGeometry(QRect(640, 30, 281, 251))
        self.merge_view = QGraphicsView(Merge)
        self.merge_view.setObjectName(u"merge_view")
        self.merge_view.setGeometry(QRect(330, 310, 301, 261))
        self.label_9 = QLabel(Merge)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(440, 590, 53, 16))
        self.show_images = QPushButton(Merge)
        self.show_images.setObjectName(u"show_images")
        self.show_images.setGeometry(QRect(40, 300, 75, 24))
        self.merge_images = QPushButton(Merge)
        self.merge_images.setObjectName(u"merge_images")
        self.merge_images.setGeometry(QRect(130, 300, 75, 24))
        self.gridLayoutWidget_2 = QWidget(Merge)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(40, 330, 241, 218))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fore_dir = QLineEdit(self.gridLayoutWidget_2)
        self.fore_dir.setObjectName(u"fore_dir")

        self.gridLayout_2.addWidget(self.fore_dir, 3, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.fore_factors_l = QLineEdit(self.gridLayoutWidget_2)
        self.fore_factors_l.setObjectName(u"fore_factors_l")

        self.horizontalLayout_4.addWidget(self.fore_factors_l)

        self.fore_factors_r = QLineEdit(self.gridLayoutWidget_2)
        self.fore_factors_r.setObjectName(u"fore_factors_r")

        self.horizontalLayout_4.addWidget(self.fore_factors_r)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 8, 1, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 4, 0, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 7, 0, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 5, 0, 1, 1)

        self.file_pre = QLineEdit(self.gridLayoutWidget_2)
        self.file_pre.setObjectName(u"file_pre")

        self.gridLayout_2.addWidget(self.file_pre, 6, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.fore_num_l = QSpinBox(self.gridLayoutWidget_2)
        self.fore_num_l.setObjectName(u"fore_num_l")
        self.fore_num_l.setValue(1)

        self.horizontalLayout_5.addWidget(self.fore_num_l)

        self.fore_num_r = QSpinBox(self.gridLayoutWidget_2)
        self.fore_num_r.setObjectName(u"fore_num_r")
        self.fore_num_r.setValue(2)

        self.horizontalLayout_5.addWidget(self.fore_num_r)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 4, 1, 1, 1)

        self.save_dir = QLineEdit(self.gridLayoutWidget_2)
        self.save_dir.setObjectName(u"save_dir")

        self.gridLayout_2.addWidget(self.save_dir, 5, 1, 1, 1)

        self.back_dir = QLineEdit(self.gridLayoutWidget_2)
        self.back_dir.setObjectName(u"back_dir")

        self.gridLayout_2.addWidget(self.back_dir, 0, 1, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 6, 0, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 8, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.fore_alphas_l = QLineEdit(self.gridLayoutWidget_2)
        self.fore_alphas_l.setObjectName(u"fore_alphas_l")

        self.horizontalLayout_3.addWidget(self.fore_alphas_l)

        self.fore_alphas_r = QLineEdit(self.gridLayoutWidget_2)
        self.fore_alphas_r.setObjectName(u"fore_alphas_r")

        self.horizontalLayout_3.addWidget(self.fore_alphas_r)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 7, 1, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget_2)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 2, 0, 1, 1)

        self.back_use_num = QSpinBox(self.gridLayoutWidget_2)
        self.back_use_num.setObjectName(u"back_use_num")
        self.back_use_num.setMaximum(9999)
        self.back_use_num.setValue(10)

        self.gridLayout_2.addWidget(self.back_use_num, 2, 1, 1, 1)

        self.batch_merge_images = QPushButton(Merge)
        self.batch_merge_images.setObjectName(u"batch_merge_images")
        self.batch_merge_images.setGeometry(QRect(210, 560, 75, 24))
        self.save_image = QPushButton(Merge)
        self.save_image.setObjectName(u"save_image")
        self.save_image.setGeometry(QRect(210, 300, 75, 24))
        self.label_on = QCheckBox(Merge)
        self.label_on.setObjectName(u"label_on")
        self.label_on.setGeometry(QRect(30, 560, 71, 20))
        self.label_on.setChecked(True)
        self.clear_dir = QPushButton(Merge)
        self.clear_dir.setObjectName(u"clear_dir")
        self.clear_dir.setGeometry(QRect(110, 560, 75, 24))

        self.retranslateUi(Merge)

        QMetaObject.connectSlotsByName(Merge)
    # setupUi

    def retranslateUi(self, Merge):
        Merge.setWindowTitle(QCoreApplication.translate("Merge", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Merge", u"\u56fe\u7247\u5408\u5e76", None))
        self.label.setText(QCoreApplication.translate("Merge", u"\u80cc\u666f\u56fe\u7247", None))
        self.label_2.setText(QCoreApplication.translate("Merge", u"\u524d\u666f\u56fe\u7247", None))
        self.label_4.setText(QCoreApplication.translate("Merge", u"\u4f4d\u7f6e", None))
        self.label_3.setText(QCoreApplication.translate("Merge", u"\u900f\u660e\u5ea6", None))
        self.back_pos_w.setText(QCoreApplication.translate("Merge", u"0", None))
        self.back_pos_h.setText(QCoreApplication.translate("Merge", u"0", None))
        self.back_path.setText(QCoreApplication.translate("Merge", u"back/bg01.png", None))
        self.back_padding.setText(QCoreApplication.translate("Merge", u"\u542f\u7528,\u6279\u91cf\u9ed8\u8ba4\u5173", None))
        self.label_5.setText(QCoreApplication.translate("Merge", u"\u7f29\u653e", None))
        self.label_6.setText(QCoreApplication.translate("Merge", u"\u80cc\u666f\u56fe\u6269\u5145", None))
        self.fore_path.setText(QCoreApplication.translate("Merge", u"fore/fore_1.png", None))
        self.label_15.setText(QCoreApplication.translate("Merge", u"\u4fdd\u5b58\u8def\u5f84", None))
        self.single_save_image.setText(QCoreApplication.translate("Merge", u"merge/single_image.png", None))
        self.label_7.setText(QCoreApplication.translate("Merge", u"\u80cc\u666f", None))
        self.label_8.setText(QCoreApplication.translate("Merge", u"\u524d\u666f", None))
        self.label_9.setText(QCoreApplication.translate("Merge", u"\u5408\u5e76", None))
        self.show_images.setText(QCoreApplication.translate("Merge", u"\u663e\u793a\u56fe\u7247", None))
        self.merge_images.setText(QCoreApplication.translate("Merge", u"\u5408\u5e76\u56fe\u7247", None))
        self.fore_dir.setText(QCoreApplication.translate("Merge", u"fore", None))
        self.fore_factors_l.setText(QCoreApplication.translate("Merge", u"0.5", None))
        self.fore_factors_r.setText(QCoreApplication.translate("Merge", u"2", None))
        self.label_17.setText(QCoreApplication.translate("Merge", u"\u524d\u666f\u4e2a\u6570", None))
        self.label_13.setText(QCoreApplication.translate("Merge", u"\u900f\u660e\u5ea6", None))
        self.label_10.setText(QCoreApplication.translate("Merge", u"\u80cc\u666f\u76ee\u5f55", None))
        self.label_12.setText(QCoreApplication.translate("Merge", u"\u5408\u5e76\u76ee\u5f55", None))
        self.file_pre.setText(QCoreApplication.translate("Merge", u"{time}_{num}_{size}", None))
        self.save_dir.setText(QCoreApplication.translate("Merge", u"merge", None))
        self.back_dir.setText(QCoreApplication.translate("Merge", u"back", None))
        self.label_16.setText(QCoreApplication.translate("Merge", u"\u6587\u4ef6\u524d\u7f00", None))
        self.label_14.setText(QCoreApplication.translate("Merge", u"\u7f29\u653e", None))
        self.fore_alphas_l.setText(QCoreApplication.translate("Merge", u"0.5", None))
        self.fore_alphas_r.setText(QCoreApplication.translate("Merge", u"1", None))
        self.label_11.setText(QCoreApplication.translate("Merge", u"\u524d\u666f\u76ee\u5f55", None))
        self.label_18.setText(QCoreApplication.translate("Merge", u"\u80cc\u666f\u6570\u91cf", None))
        self.batch_merge_images.setText(QCoreApplication.translate("Merge", u"\u6279\u91cf\u5408\u5e76", None))
        self.save_image.setText(QCoreApplication.translate("Merge", u"\u4fdd\u5b58\u56fe\u7247", None))
        self.label_on.setText(QCoreApplication.translate("Merge", u"\u6570\u636e\u6807\u6ce8", None))
        self.clear_dir.setText(QCoreApplication.translate("Merge", u"\u6e05\u7a7a\u6587\u4ef6\u5939", None))
    # retranslateUi

