# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QAbstractSpinBox, QApplication, QCheckBox,
    QComboBox, QDialog, QFormLayout, QGraphicsView,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1131, 809)
        self.image_win = QGraphicsView(Dialog)
        self.image_win.setObjectName(u"image_win")
        self.image_win.setGeometry(QRect(580, 20, 401, 361))
        self.image_win.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.gridLayoutWidget_3 = QWidget(Dialog)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(40, 700, 252, 56))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.batch_save = QPushButton(self.gridLayoutWidget_3)
        self.batch_save.setObjectName(u"batch_save")

        self.gridLayout_5.addWidget(self.batch_save, 1, 1, 1, 1)

        self.label_nums = QSpinBox(self.gridLayoutWidget_3)
        self.label_nums.setObjectName(u"label_nums")
        self.label_nums.setMinimum(-99)
        self.label_nums.setStepType(QAbstractSpinBox.DefaultStepType)
        self.label_nums.setValue(28)

        self.gridLayout_5.addWidget(self.label_nums, 0, 1, 1, 1)

        self.line_label_on = QCheckBox(self.gridLayoutWidget_3)
        self.line_label_on.setObjectName(u"line_label_on")
        self.line_label_on.setChecked(True)

        self.gridLayout_5.addWidget(self.line_label_on, 1, 0, 1, 1)

        self.label_47 = QLabel(self.gridLayoutWidget_3)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_5.addWidget(self.label_47, 0, 0, 1, 1)

        self.clear_dir = QPushButton(self.gridLayoutWidget_3)
        self.clear_dir.setObjectName(u"clear_dir")

        self.gridLayout_5.addWidget(self.clear_dir, 0, 2, 1, 1)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 430, 251, 271))
        self.gridLayoutWidget_4 = QWidget(self.groupBox)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 20, 231, 236))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.bottom_random = QCheckBox(self.gridLayoutWidget_4)
        self.bottom_random.setObjectName(u"bottom_random")
        self.bottom_random.setChecked(True)

        self.gridLayout_4.addWidget(self.bottom_random, 5, 1, 1, 1)

        self.label_36 = QLabel(self.gridLayoutWidget_4)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_4.addWidget(self.label_36, 3, 0, 1, 1)

        self.label_43 = QLabel(self.gridLayoutWidget_4)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_4.addWidget(self.label_43, 1, 0, 1, 1)

        self.inter_filepath = QLineEdit(self.gridLayoutWidget_4)
        self.inter_filepath.setObjectName(u"inter_filepath")

        self.gridLayout_4.addWidget(self.inter_filepath, 8, 1, 1, 1)

        self.save_dir = QLineEdit(self.gridLayoutWidget_4)
        self.save_dir.setObjectName(u"save_dir")

        self.gridLayout_4.addWidget(self.save_dir, 1, 1, 1, 1)

        self.label_42 = QLabel(self.gridLayoutWidget_4)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_4.addWidget(self.label_42, 8, 0, 1, 1)

        self.label_38 = QLabel(self.gridLayoutWidget_4)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_4.addWidget(self.label_38, 5, 0, 1, 1)

        self.label_41 = QLabel(self.gridLayoutWidget_4)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_4.addWidget(self.label_41, 7, 0, 1, 1)

        self.bottom_filepath = QLineEdit(self.gridLayoutWidget_4)
        self.bottom_filepath.setObjectName(u"bottom_filepath")

        self.gridLayout_4.addWidget(self.bottom_filepath, 6, 1, 1, 1)

        self.label_37 = QLabel(self.gridLayoutWidget_4)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_4.addWidget(self.label_37, 0, 0, 1, 1)

        self.label_40 = QLabel(self.gridLayoutWidget_4)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_4.addWidget(self.label_40, 6, 0, 1, 1)

        self.label_39 = QLabel(self.gridLayoutWidget_4)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_4.addWidget(self.label_39, 4, 0, 1, 1)

        self.top_random = QCheckBox(self.gridLayoutWidget_4)
        self.top_random.setObjectName(u"top_random")
        self.top_random.setChecked(True)

        self.gridLayout_4.addWidget(self.top_random, 3, 1, 1, 1)

        self.inter_random = QCheckBox(self.gridLayoutWidget_4)
        self.inter_random.setObjectName(u"inter_random")
        self.inter_random.setChecked(True)

        self.gridLayout_4.addWidget(self.inter_random, 7, 1, 1, 1)

        self.batch_nums = QLineEdit(self.gridLayoutWidget_4)
        self.batch_nums.setObjectName(u"batch_nums")

        self.gridLayout_4.addWidget(self.batch_nums, 0, 1, 1, 1)

        self.label_44 = QLabel(self.gridLayoutWidget_4)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_4.addWidget(self.label_44, 2, 0, 1, 1)

        self.file_pre = QLineEdit(self.gridLayoutWidget_4)
        self.file_pre.setObjectName(u"file_pre")

        self.gridLayout_4.addWidget(self.file_pre, 2, 1, 1, 1)

        self.top_filepath = QLineEdit(self.gridLayoutWidget_4)
        self.top_filepath.setObjectName(u"top_filepath")

        self.gridLayout_4.addWidget(self.top_filepath, 4, 1, 1, 1)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(310, 10, 251, 651))
        self.gridLayoutWidget_2 = QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 20, 231, 625))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_text_content = QLineEdit(self.gridLayoutWidget_2)
        self.top_text_content.setObjectName(u"top_text_content")

        self.gridLayout_2.addWidget(self.top_text_content, 3, 1, 1, 1)

        self.label_23 = QLabel(self.gridLayoutWidget_2)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_2.addWidget(self.label_23, 16, 0, 1, 1)

        self.label_19 = QLabel(self.gridLayoutWidget_2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_2.addWidget(self.label_19, 2, 0, 1, 1)

        self.label_30 = QLabel(self.gridLayoutWidget_2)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_2.addWidget(self.label_30, 18, 0, 1, 1)

        self.label_27 = QLabel(self.gridLayoutWidget_2)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_2.addWidget(self.label_27, 17, 0, 1, 1)

        self.label_29 = QLabel(self.gridLayoutWidget_2)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_2.addWidget(self.label_29, 26, 0, 1, 1)

        self.top_text_on = QCheckBox(self.gridLayoutWidget_2)
        self.top_text_on.setObjectName(u"top_text_on")
        self.top_text_on.setChecked(True)

        self.gridLayout_2.addWidget(self.top_text_on, 0, 1, 1, 1)

        self.bottom_text_font = QLineEdit(self.gridLayoutWidget_2)
        self.bottom_text_font.setObjectName(u"bottom_text_font")

        self.gridLayout_2.addWidget(self.bottom_text_font, 16, 1, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 4, 0, 1, 1)

        self.bottom_text_on = QCheckBox(self.gridLayoutWidget_2)
        self.bottom_text_on.setObjectName(u"bottom_text_on")
        self.bottom_text_on.setChecked(True)

        self.gridLayout_2.addWidget(self.bottom_text_on, 7, 1, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget_2)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 3, 0, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget_2)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 1, 0, 1, 1)

        self.label_26 = QLabel(self.gridLayoutWidget_2)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_2.addWidget(self.label_26, 9, 0, 1, 1)

        self.top_text_shape = QComboBox(self.gridLayoutWidget_2)
        self.top_text_shape.addItem("")
        self.top_text_shape.addItem("")
        self.top_text_shape.addItem("")
        self.top_text_shape.setObjectName(u"top_text_shape")

        self.gridLayout_2.addWidget(self.top_text_shape, 1, 1, 1, 1)

        self.label_31 = QLabel(self.gridLayoutWidget_2)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_2.addWidget(self.label_31, 28, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.inter_shift_y = QSpinBox(self.gridLayoutWidget_2)
        self.inter_shift_y.setObjectName(u"inter_shift_y")
        self.inter_shift_y.setMinimum(-99)
        self.inter_shift_y.setStepType(QAbstractSpinBox.DefaultStepType)
        self.inter_shift_y.setValue(6)

        self.horizontalLayout_13.addWidget(self.inter_shift_y)


        self.gridLayout_2.addLayout(self.horizontalLayout_13, 27, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.top_text_font_w = QLineEdit(self.gridLayoutWidget_2)
        self.top_text_font_w.setObjectName(u"top_text_font_w")

        self.horizontalLayout_5.addWidget(self.top_text_font_w)

        self.top_text_font_h = QLineEdit(self.gridLayoutWidget_2)
        self.top_text_font_h.setObjectName(u"top_text_font_h")

        self.horizontalLayout_5.addWidget(self.top_text_font_h)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 4, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.bottom_text_font_w = QLineEdit(self.gridLayoutWidget_2)
        self.bottom_text_font_w.setObjectName(u"bottom_text_font_w")

        self.horizontalLayout_8.addWidget(self.bottom_text_font_w)

        self.bottom_text_font_h = QLineEdit(self.gridLayoutWidget_2)
        self.bottom_text_font_h.setObjectName(u"bottom_text_font_h")

        self.horizontalLayout_8.addWidget(self.bottom_text_font_h)


        self.gridLayout_2.addLayout(self.horizontalLayout_8, 12, 1, 1, 1)

        self.top_text_space = QSpinBox(self.gridLayoutWidget_2)
        self.top_text_space.setObjectName(u"top_text_space")
        self.top_text_space.setMinimum(0)
        self.top_text_space.setValue(0)

        self.gridLayout_2.addWidget(self.top_text_space, 5, 1, 1, 1)

        self.bottom_text_content = QLineEdit(self.gridLayoutWidget_2)
        self.bottom_text_content.setObjectName(u"bottom_text_content")

        self.gridLayout_2.addWidget(self.bottom_text_content, 10, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.bottom_text_size_w = QLineEdit(self.gridLayoutWidget_2)
        self.bottom_text_size_w.setObjectName(u"bottom_text_size_w")

        self.horizontalLayout_7.addWidget(self.bottom_text_size_w)

        self.bottom_text_size_h = QLineEdit(self.gridLayoutWidget_2)
        self.bottom_text_size_h.setObjectName(u"bottom_text_size_h")

        self.horizontalLayout_7.addWidget(self.bottom_text_size_h)


        self.gridLayout_2.addLayout(self.horizontalLayout_7, 9, 1, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.inter_text_font_w = QLineEdit(self.gridLayoutWidget_2)
        self.inter_text_font_w.setObjectName(u"inter_text_font_w")

        self.horizontalLayout_10.addWidget(self.inter_text_font_w)

        self.inter_text_font_h = QLineEdit(self.gridLayoutWidget_2)
        self.inter_text_font_h.setObjectName(u"inter_text_font_h")

        self.horizontalLayout_10.addWidget(self.inter_text_font_h)


        self.gridLayout_2.addLayout(self.horizontalLayout_10, 26, 1, 1, 1)

        self.label_34 = QLabel(self.gridLayoutWidget_2)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_2.addWidget(self.label_34, 20, 0, 1, 1)

        self.label_21 = QLabel(self.gridLayoutWidget_2)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_2.addWidget(self.label_21, 12, 0, 1, 1)

        self.inter_text_space = QSpinBox(self.gridLayoutWidget_2)
        self.inter_text_space.setObjectName(u"inter_text_space")
        self.inter_text_space.setMinimum(0)
        self.inter_text_space.setValue(0)

        self.gridLayout_2.addWidget(self.inter_text_space, 20, 1, 1, 1)

        self.inter_text_on = QCheckBox(self.gridLayoutWidget_2)
        self.inter_text_on.setObjectName(u"inter_text_on")
        self.inter_text_on.setChecked(True)

        self.gridLayout_2.addWidget(self.inter_text_on, 17, 1, 1, 1)

        self.label_22 = QLabel(self.gridLayoutWidget_2)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_2.addWidget(self.label_22, 7, 0, 1, 1)

        self.label_46 = QLabel(self.gridLayoutWidget_2)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_2.addWidget(self.label_46, 27, 0, 1, 1)

        self.label_33 = QLabel(self.gridLayoutWidget_2)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_2.addWidget(self.label_33, 5, 0, 1, 1)

        self.label_32 = QLabel(self.gridLayoutWidget_2)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_2.addWidget(self.label_32, 19, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.inter_text_size_w = QLineEdit(self.gridLayoutWidget_2)
        self.inter_text_size_w.setObjectName(u"inter_text_size_w")

        self.horizontalLayout_9.addWidget(self.inter_text_size_w)

        self.inter_text_size_h = QLineEdit(self.gridLayoutWidget_2)
        self.inter_text_size_h.setObjectName(u"inter_text_size_h")

        self.horizontalLayout_9.addWidget(self.inter_text_size_h)


        self.gridLayout_2.addLayout(self.horizontalLayout_9, 19, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.top_text_size_w = QLineEdit(self.gridLayoutWidget_2)
        self.top_text_size_w.setObjectName(u"top_text_size_w")

        self.horizontalLayout_6.addWidget(self.top_text_size_w)

        self.top_text_size_h = QLineEdit(self.gridLayoutWidget_2)
        self.top_text_size_h.setObjectName(u"top_text_size_h")

        self.horizontalLayout_6.addWidget(self.top_text_size_h)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 2, 1, 1, 1)

        self.label_35 = QLabel(self.gridLayoutWidget_2)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_2.addWidget(self.label_35, 13, 0, 1, 1)

        self.bottom_text_shape = QComboBox(self.gridLayoutWidget_2)
        self.bottom_text_shape.addItem("")
        self.bottom_text_shape.addItem("")
        self.bottom_text_shape.addItem("")
        self.bottom_text_shape.setObjectName(u"bottom_text_shape")

        self.gridLayout_2.addWidget(self.bottom_text_shape, 8, 1, 1, 1)

        self.label_25 = QLabel(self.gridLayoutWidget_2)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_2.addWidget(self.label_25, 10, 0, 1, 1)

        self.inter_text_content = QLineEdit(self.gridLayoutWidget_2)
        self.inter_text_content.setObjectName(u"inter_text_content")

        self.gridLayout_2.addWidget(self.inter_text_content, 23, 1, 1, 1)

        self.inter_text_font = QLineEdit(self.gridLayoutWidget_2)
        self.inter_text_font.setObjectName(u"inter_text_font")

        self.gridLayout_2.addWidget(self.inter_text_font, 28, 1, 1, 1)

        self.label_24 = QLabel(self.gridLayoutWidget_2)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_2.addWidget(self.label_24, 8, 0, 1, 1)

        self.label_28 = QLabel(self.gridLayoutWidget_2)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_2.addWidget(self.label_28, 23, 0, 1, 1)

        self.bottom_text_space = QSpinBox(self.gridLayoutWidget_2)
        self.bottom_text_space.setObjectName(u"bottom_text_space")
        self.bottom_text_space.setMinimum(0)
        self.bottom_text_space.setValue(0)

        self.gridLayout_2.addWidget(self.bottom_text_space, 13, 1, 1, 1)

        self.top_text_font = QLineEdit(self.gridLayoutWidget_2)
        self.top_text_font.setObjectName(u"top_text_font")

        self.gridLayout_2.addWidget(self.top_text_font, 6, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 6, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.inter_text_shape = QComboBox(self.gridLayoutWidget_2)
        self.inter_text_shape.addItem("")
        self.inter_text_shape.addItem("")
        self.inter_text_shape.addItem("")
        self.inter_text_shape.setObjectName(u"inter_text_shape")

        self.gridLayout_2.addWidget(self.inter_text_shape, 18, 1, 1, 1)

        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(30, 10, 251, 421))
        self.widget = QWidget(self.groupBox_3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 230, 435))
        self.formLayout_2 = QFormLayout(self.widget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.image_w = QLineEdit(self.widget)
        self.image_w.setObjectName(u"image_w")

        self.horizontalLayout.addWidget(self.image_w)

        self.image_h = QLineEdit(self.widget)
        self.image_h.setObjectName(u"image_h")

        self.horizontalLayout.addWidget(self.image_h)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.img_g = QLineEdit(self.widget)
        self.img_g.setObjectName(u"img_g")

        self.gridLayout_3.addWidget(self.img_g, 0, 1, 1, 1)

        self.img_r = QLineEdit(self.widget)
        self.img_r.setObjectName(u"img_r")

        self.gridLayout_3.addWidget(self.img_r, 0, 0, 1, 1)

        self.img_b = QLineEdit(self.widget)
        self.img_b.setObjectName(u"img_b")

        self.gridLayout_3.addWidget(self.img_b, 0, 2, 1, 1)


        self.formLayout_2.setLayout(1, QFormLayout.FieldRole, self.gridLayout_3)

        self.resize_factor = QSpinBox(self.widget)
        self.resize_factor.setObjectName(u"resize_factor")
        self.resize_factor.setMinimum(0)
        self.resize_factor.setValue(2)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.resize_factor)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_9)

        self.out_on = QCheckBox(self.widget)
        self.out_on.setObjectName(u"out_on")
        self.out_on.setChecked(True)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.out_on)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.out_shape = QComboBox(self.widget)
        self.out_shape.addItem("")
        self.out_shape.addItem("")
        self.out_shape.addItem("")
        self.out_shape.setObjectName(u"out_shape")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.out_shape)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_8)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.out_size_w = QLineEdit(self.widget)
        self.out_size_w.setObjectName(u"out_size_w")

        self.horizontalLayout_2.addWidget(self.out_size_w)

        self.out_size_h = QLineEdit(self.widget)
        self.out_size_h.setObjectName(u"out_size_h")

        self.horizontalLayout_2.addWidget(self.out_size_h)


        self.formLayout_2.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.out_width = QSpinBox(self.widget)
        self.out_width.setObjectName(u"out_width")
        self.out_width.setMinimum(0)
        self.out_width.setValue(7)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.out_width)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_6)

        self.border_on = QCheckBox(self.widget)
        self.border_on.setObjectName(u"border_on")
        self.border_on.setChecked(True)

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.border_on)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_10)

        self.border_shape = QComboBox(self.widget)
        self.border_shape.addItem("")
        self.border_shape.addItem("")
        self.border_shape.addItem("")
        self.border_shape.setObjectName(u"border_shape")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.border_shape)

        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.label_14)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.border_size_w = QLineEdit(self.widget)
        self.border_size_w.setObjectName(u"border_size_w")

        self.horizontalLayout_3.addWidget(self.border_size_w)

        self.border_size_h = QLineEdit(self.widget)
        self.border_size_h.setObjectName(u"border_size_h")

        self.horizontalLayout_3.addWidget(self.border_size_h)


        self.formLayout_2.setLayout(9, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.label_15)

        self.border_width = QSpinBox(self.widget)
        self.border_width.setObjectName(u"border_width")
        self.border_width.setMinimum(0)
        self.border_width.setValue(1)

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.border_width)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(11, QFormLayout.LabelRole, self.label_11)

        self.in_on = QCheckBox(self.widget)
        self.in_on.setObjectName(u"in_on")
        self.in_on.setChecked(False)

        self.formLayout_2.setWidget(11, QFormLayout.FieldRole, self.in_on)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(12, QFormLayout.LabelRole, self.label_12)

        self.in_shape = QComboBox(self.widget)
        self.in_shape.addItem("")
        self.in_shape.addItem("")
        self.in_shape.addItem("")
        self.in_shape.setObjectName(u"in_shape")

        self.formLayout_2.setWidget(12, QFormLayout.FieldRole, self.in_shape)

        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_2.setWidget(13, QFormLayout.LabelRole, self.label_16)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.in_size_w = QLineEdit(self.widget)
        self.in_size_w.setObjectName(u"in_size_w")

        self.horizontalLayout_4.addWidget(self.in_size_w)

        self.in_size_h = QLineEdit(self.widget)
        self.in_size_h.setObjectName(u"in_size_h")

        self.horizontalLayout_4.addWidget(self.in_size_h)


        self.formLayout_2.setLayout(13, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_2.setWidget(14, QFormLayout.LabelRole, self.label_17)

        self.in_width = QSpinBox(self.widget)
        self.in_width.setObjectName(u"in_width")
        self.in_width.setMinimum(0)
        self.in_width.setValue(1)

        self.formLayout_2.setWidget(14, QFormLayout.FieldRole, self.in_width)

        self.label_45 = QLabel(self.widget)
        self.label_45.setObjectName(u"label_45")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_45)

        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(320, 670, 231, 51))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.update_config = QPushButton(self.gridLayoutWidget)
        self.update_config.setObjectName(u"update_config")

        self.gridLayout.addWidget(self.update_config, 0, 0, 1, 1)

        self.image_draw = QPushButton(self.gridLayoutWidget)
        self.image_draw.setObjectName(u"image_draw")

        self.gridLayout.addWidget(self.image_draw, 0, 1, 1, 1)

        self.save_path = QLineEdit(self.gridLayoutWidget)
        self.save_path.setObjectName(u"save_path")

        self.gridLayout.addWidget(self.save_path, 1, 0, 1, 1)

        self.single_save = QPushButton(self.gridLayoutWidget)
        self.single_save.setObjectName(u"single_save")

        self.gridLayout.addWidget(self.single_save, 1, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.batch_save.setText(QCoreApplication.translate("Dialog", u"\u6279\u91cf\u4fdd\u5b58", None))
        self.line_label_on.setText(QCoreApplication.translate("Dialog", u"\u6587\u672c\u884c\u6807\u6ce8", None))
        self.label_47.setText(QCoreApplication.translate("Dialog", u"\u6807\u6ce8\u6570\u91cf", None))
        self.clear_dir.setText(QCoreApplication.translate("Dialog", u"\u6e05\u7a7a\u6587\u4ef6\u5939", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u6279\u91cf\u914d\u7f6e\u53c2\u6570", None))
        self.bottom_random.setText(QCoreApplication.translate("Dialog", u"\u968f\u673a", None))
        self.label_36.setText(QCoreApplication.translate("Dialog", u"\u4e0a\u65b9\u6587\u5b57", None))
        self.label_43.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58\u6587\u4ef6\u5939", None))
        self.inter_filepath.setText(QCoreApplication.translate("Dialog", u"content/inter.txt", None))
        self.save_dir.setText(QCoreApplication.translate("Dialog", u"out", None))
        self.label_42.setText(QCoreApplication.translate("Dialog", u"\u6587\u4ef6\u8def\u5f84(\u968f\u673a\u65e0\u6548)", None))
        self.label_38.setText(QCoreApplication.translate("Dialog", u"\u4e0b\u65b9\u6587\u5b57", None))
        self.label_41.setText(QCoreApplication.translate("Dialog", u"\u5185\u90e8\u6587\u5b57", None))
        self.bottom_filepath.setText(QCoreApplication.translate("Dialog", u"content/bottom.txt", None))
        self.label_37.setText(QCoreApplication.translate("Dialog", u"\u6570\u91cf", None))
        self.label_40.setText(QCoreApplication.translate("Dialog", u"\u6587\u4ef6\u8def\u5f84(\u968f\u673a\u65e0\u6548)", None))
        self.label_39.setText(QCoreApplication.translate("Dialog", u"\u6587\u4ef6\u8def\u5f84(\u968f\u673a\u65e0\u6548)", None))
        self.top_random.setText(QCoreApplication.translate("Dialog", u"\u968f\u673a", None))
        self.inter_random.setText(QCoreApplication.translate("Dialog", u"\u968f\u673a", None))
        self.batch_nums.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.label_44.setText(QCoreApplication.translate("Dialog", u"\u6587\u4ef6\u5939\u524d\u7f00", None))
        self.file_pre.setText(QCoreApplication.translate("Dialog", u"{shape}_{num}_{time}", None))
        self.top_filepath.setText(QCoreApplication.translate("Dialog", u"content/top.txt", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"\u6587\u5b57\u4fe1\u606f\u914d\u7f6e", None))
        self.top_text_content.setText(QCoreApplication.translate("Dialog", u"\u798f\u5efa\u67d0\u67d0\u67d0\u6709\u9650\u516c\u53f8", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"\u5b57\u4f53", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"\u6587\u672c\u884c\u5bbd\u5ea6", None))
        self.label_30.setText(QCoreApplication.translate("Dialog", u"\u5f62\u72b6", None))
        self.label_27.setText(QCoreApplication.translate("Dialog", u"\u4e2d\u95f4\u6587\u5b57", None))
        self.label_29.setText(QCoreApplication.translate("Dialog", u"\u6587\u5b57\u5bbd\u9ad8", None))
        self.top_text_on.setText(QCoreApplication.translate("Dialog", u"\u542f\u7528", None))
        self.bottom_text_font.setText(QCoreApplication.translate("Dialog", u"./fonts/\u5b8b\u4f53.TTF", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u6587\u5b57\u5bbd\u9ad8", None))
        self.bottom_text_on.setText(QCoreApplication.translate("Dialog", u"\u542f\u7528", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"\u5185\u5bb9", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"\u5f62\u72b6", None))
        self.label_26.setText(QCoreApplication.translate("Dialog", u"\u6587\u672c\u884c\u5bbd\u5ea6", None))
        self.top_text_shape.setItemText(0, QCoreApplication.translate("Dialog", u"circle", None))
        self.top_text_shape.setItemText(1, QCoreApplication.translate("Dialog", u"rectangle", None))
        self.top_text_shape.setItemText(2, QCoreApplication.translate("Dialog", u"oval", None))

        self.label_31.setText(QCoreApplication.translate("Dialog", u"\u5b57\u4f53", None))
        self.top_text_font_w.setText(QCoreApplication.translate("Dialog", u"21", None))
        self.top_text_font_h.setText(QCoreApplication.translate("Dialog", u"24", None))
        self.bottom_text_font_w.setText(QCoreApplication.translate("Dialog", u"10", None))
        self.bottom_text_font_h.setText(QCoreApplication.translate("Dialog", u"15", None))
        self.bottom_text_content.setText(QCoreApplication.translate("Dialog", u"123456789012X", None))
        self.bottom_text_size_w.setText(QCoreApplication.translate("Dialog", u"123", None))
        self.bottom_text_size_h.setText(QCoreApplication.translate("Dialog", u"73", None))
        self.inter_text_font_w.setText(QCoreApplication.translate("Dialog", u"27", None))
        self.inter_text_font_h.setText(QCoreApplication.translate("Dialog", u"31", None))
        self.label_34.setText(QCoreApplication.translate("Dialog", u"\u5b57\u95f4\u8ddd", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"\u6587\u5b57\u5bbd\u9ad8", None))
        self.inter_text_on.setText(QCoreApplication.translate("Dialog", u"\u542f\u7528", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"\u4e0b\u65b9\u6587\u5b57", None))
        self.label_46.setText(QCoreApplication.translate("Dialog", u"\u6587\u5b57\u504f\u79fb", None))
        self.label_33.setText(QCoreApplication.translate("Dialog", u"\u5b57\u95f4\u8ddd", None))
        self.label_32.setText(QCoreApplication.translate("Dialog", u"\u6587\u672c\u884c\u5bbd\u5ea6", None))
        self.inter_text_size_w.setText(QCoreApplication.translate("Dialog", u"125", None))
        self.inter_text_size_h.setText(QCoreApplication.translate("Dialog", u"75", None))
        self.top_text_size_w.setText(QCoreApplication.translate("Dialog", u"123", None))
        self.top_text_size_h.setText(QCoreApplication.translate("Dialog", u"74", None))
        self.label_35.setText(QCoreApplication.translate("Dialog", u"\u5b57\u95f4\u8ddd", None))
        self.bottom_text_shape.setItemText(0, QCoreApplication.translate("Dialog", u"circle", None))
        self.bottom_text_shape.setItemText(1, QCoreApplication.translate("Dialog", u"rectangle", None))
        self.bottom_text_shape.setItemText(2, QCoreApplication.translate("Dialog", u"oval", None))

        self.label_25.setText(QCoreApplication.translate("Dialog", u"\u5185\u5bb9", None))
        self.inter_text_content.setText(QCoreApplication.translate("Dialog", u"\u8d22\u52a1\u4e13\u7528\u7ae0", None))
        self.inter_text_font.setText(QCoreApplication.translate("Dialog", u"./fonts/\u5b8b\u4f53.TTF", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"\u5f62\u72b6", None))
        self.label_28.setText(QCoreApplication.translate("Dialog", u"\u5185\u5bb9", None))
        self.top_text_font.setText(QCoreApplication.translate("Dialog", u"./fonts/\u5b8b\u4f53.TTF", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u5b57\u4f53", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u4e0a\u65b9\u6587\u5b57", None))
        self.inter_text_shape.setItemText(0, QCoreApplication.translate("Dialog", u"rectangle", None))
        self.inter_text_shape.setItemText(1, QCoreApplication.translate("Dialog", u"circle", None))
        self.inter_text_shape.setItemText(2, QCoreApplication.translate("Dialog", u"oval", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"\u56fe\u7247\u4fe1\u606f\u914d\u7f6e", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u56fe\u50cf\u5927\u5c0fwh", None))
        self.image_w.setText(QCoreApplication.translate("Dialog", u"310", None))
        self.image_h.setText(QCoreApplication.translate("Dialog", u"310", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u989c\u8272RGB", None))
        self.img_g.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.img_r.setText(QCoreApplication.translate("Dialog", u"255", None))
        self.img_b.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u5916\u8f6e\u5ed3\u914d\u7f6e", None))
        self.out_on.setText(QCoreApplication.translate("Dialog", u"\u542f\u7528", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u5f62\u72b6", None))
        self.out_shape.setItemText(0, QCoreApplication.translate("Dialog", u"circle", None))
        self.out_shape.setItemText(1, QCoreApplication.translate("Dialog", u"rectangle", None))
        self.out_shape.setItemText(2, QCoreApplication.translate("Dialog", u"oval", None))

        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u5927\u5c0f", None))
        self.out_size_w.setText(QCoreApplication.translate("Dialog", u"150", None))
        self.out_size_h.setText(QCoreApplication.translate("Dialog", u"100", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u7ebf\u7c97", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u8fb9\u754c\u7ebf\u914d\u7f6e", None))
        self.border_on.setText(QCoreApplication.translate("Dialog", u"\u542f\u7528", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u5f62\u72b6", None))
        self.border_shape.setItemText(0, QCoreApplication.translate("Dialog", u"circle", None))
        self.border_shape.setItemText(1, QCoreApplication.translate("Dialog", u"rectangle", None))
        self.border_shape.setItemText(2, QCoreApplication.translate("Dialog", u"oval", None))

        self.label_14.setText(QCoreApplication.translate("Dialog", u"\u5927\u5c0f", None))
        self.border_size_w.setText(QCoreApplication.translate("Dialog", u"140", None))
        self.border_size_h.setText(QCoreApplication.translate("Dialog", u"90", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"\u7ebf\u7c97", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u5185\u90e8\u7ebf\u914d\u7f6e", None))
        self.in_on.setText(QCoreApplication.translate("Dialog", u"\u542f\u7528", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u5f62\u72b6", None))
        self.in_shape.setItemText(0, QCoreApplication.translate("Dialog", u"circle", None))
        self.in_shape.setItemText(1, QCoreApplication.translate("Dialog", u"rectangle", None))
        self.in_shape.setItemText(2, QCoreApplication.translate("Dialog", u"oval", None))

        self.label_16.setText(QCoreApplication.translate("Dialog", u"\u5927\u5c0f", None))
        self.in_size_w.setText(QCoreApplication.translate("Dialog", u"100", None))
        self.in_size_h.setText(QCoreApplication.translate("Dialog", u"75", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"\u7ebf\u7c97", None))
        self.label_45.setText(QCoreApplication.translate("Dialog", u"\u6e05\u6670\u5ea6", None))
        self.update_config.setText(QCoreApplication.translate("Dialog", u"\u914d\u7f6e\u66f4\u65b0", None))
        self.image_draw.setText(QCoreApplication.translate("Dialog", u"\u751f\u6210", None))
        self.save_path.setText(QCoreApplication.translate("Dialog", u"seal.png", None))
        self.single_save.setText(QCoreApplication.translate("Dialog", u"\u5355\u5f20\u4fdd\u5b58", None))
    # retranslateUi

