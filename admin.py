# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\FAS.ui'
#
# Created: Tue May 07 22:10:45 2019
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_admin(object):
    def setupUi(self, admin):
        admin.setObjectName(_fromUtf8("admin"))
        admin.resize(1141, 836)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/holder/img/logo.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        admin.setWindowIcon(icon)
        admin.setStyleSheet(_fromUtf8(""))
        self.gridLayout = QtGui.QGridLayout(admin)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(admin)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setMargin(3)
        self.label.setIndent(-1)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.label_9 = QtGui.QLabel(admin)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_6.addWidget(self.label_9)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.label_10 = QtGui.QLabel(admin)
        self.label_10.setMargin(0)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_7.addWidget(self.label_10)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.tab_4 = QtGui.QTabWidget(admin)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tab_4.setFont(font)
        self.tab_4.setStyleSheet(_fromUtf8(""))
        self.tab_4.setDocumentMode(False)
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.add_class_tab = QtGui.QWidget()
        self.add_class_tab.setObjectName(_fromUtf8("add_class_tab"))
        self.gridLayout_5 = QtGui.QGridLayout(self.add_class_tab)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.groupBox_2 = QtGui.QGroupBox(self.add_class_tab)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.add_class_list = QtGui.QListWidget(self.groupBox_2)
        self.add_class_list.setObjectName(_fromUtf8("add_class_list"))
        self.verticalLayout.addWidget(self.add_class_list)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_5.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox_5 = QtGui.QGroupBox(self.add_class_tab)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_25 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_25.setObjectName(_fromUtf8("verticalLayout_25"))
        self.formLayout_13 = QtGui.QFormLayout()
        self.formLayout_13.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_13.setObjectName(_fromUtf8("formLayout_13"))
        self.label_7 = QtGui.QLabel(self.groupBox_5)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_13.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.add_class_id = QtGui.QLineEdit(self.groupBox_5)
        self.add_class_id.setObjectName(_fromUtf8("add_class_id"))
        self.formLayout_13.setWidget(0, QtGui.QFormLayout.FieldRole, self.add_class_id)
        self.label_24 = QtGui.QLabel(self.groupBox_5)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.formLayout_13.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_24)
        self.add_class_code = QtGui.QLineEdit(self.groupBox_5)
        self.add_class_code.setObjectName(_fromUtf8("add_class_code"))
        self.formLayout_13.setWidget(1, QtGui.QFormLayout.FieldRole, self.add_class_code)
        self.label_25 = QtGui.QLabel(self.groupBox_5)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.formLayout_13.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_25)
        self.add_class_teacher = QtGui.QLineEdit(self.groupBox_5)
        self.add_class_teacher.setObjectName(_fromUtf8("add_class_teacher"))
        self.formLayout_13.setWidget(3, QtGui.QFormLayout.FieldRole, self.add_class_teacher)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem6)
        self.add_class_btn = QtGui.QPushButton(self.groupBox_5)
        self.add_class_btn.setObjectName(_fromUtf8("add_class_btn"))
        self.horizontalLayout_15.addWidget(self.add_class_btn)
        self.formLayout_13.setLayout(4, QtGui.QFormLayout.FieldRole, self.horizontalLayout_15)
        self.verticalLayout_25.addLayout(self.formLayout_13)
        self.gridLayout_5.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.tab_4.addTab(self.add_class_tab, _fromUtf8(""))
        self.register_tab = QtGui.QWidget()
        self.register_tab.setObjectName(_fromUtf8("register_tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.register_tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.register_tab)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_4.addWidget(self.label_6, 0, 1, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem7, 6, 2, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.register_student_pic = QtGui.QLabel(self.groupBox)
        self.register_student_pic.setText(_fromUtf8(""))
        self.register_student_pic.setPixmap(QtGui.QPixmap(_fromUtf8(":/holder/img/holder_1.PNG")))
        self.register_student_pic.setObjectName(_fromUtf8("register_student_pic"))
        self.verticalLayout_3.addWidget(self.register_student_pic)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem8)
        self.reg_std_upload_btn = QtGui.QPushButton(self.groupBox)
        self.reg_std_upload_btn.setObjectName(_fromUtf8("reg_std_upload_btn"))
        self.verticalLayout_3.addWidget(self.reg_std_upload_btn)
        self.reg_std_add_finger_btn = QtGui.QPushButton(self.groupBox)
        self.reg_std_add_finger_btn.setObjectName(_fromUtf8("reg_std_add_finger_btn"))
        self.verticalLayout_3.addWidget(self.reg_std_add_finger_btn)
        self.reg_std_btn = QtGui.QPushButton(self.groupBox)
        self.reg_std_btn.setObjectName(_fromUtf8("reg_std_btn"))
        self.verticalLayout_3.addWidget(self.reg_std_btn)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 2, 2, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem9, 6, 3, 1, 1)
        self.std_reg_text = QtGui.QTextEdit(self.groupBox)
        self.std_reg_text.setObjectName(_fromUtf8("std_reg_text"))
        self.gridLayout_4.addWidget(self.std_reg_text, 2, 1, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem10, 0, 2, 1, 1)
        self.formLayout_6 = QtGui.QFormLayout()
        self.formLayout_6.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.reg_std_id = QtGui.QLineEdit(self.groupBox)
        self.reg_std_id.setObjectName(_fromUtf8("reg_std_id"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.FieldRole, self.reg_std_id)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_6.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.reg_std_name = QtGui.QLineEdit(self.groupBox)
        self.reg_std_name.setObjectName(_fromUtf8("reg_std_name"))
        self.formLayout_6.setWidget(2, QtGui.QFormLayout.FieldRole, self.reg_std_name)
        self.label_14 = QtGui.QLabel(self.groupBox)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout_6.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_14)
        self.reg_std_dob = QtGui.QDateEdit(self.groupBox)
        self.reg_std_dob.setObjectName(_fromUtf8("reg_std_dob"))
        self.formLayout_6.setWidget(3, QtGui.QFormLayout.FieldRole, self.reg_std_dob)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_6.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_4)
        self.reg_std_guardian = QtGui.QLineEdit(self.groupBox)
        self.reg_std_guardian.setObjectName(_fromUtf8("reg_std_guardian"))
        self.formLayout_6.setWidget(4, QtGui.QFormLayout.FieldRole, self.reg_std_guardian)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_6.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_5)
        self.reg_std_address = QtGui.QTextEdit(self.groupBox)
        self.reg_std_address.setObjectName(_fromUtf8("reg_std_address"))
        self.formLayout_6.setWidget(5, QtGui.QFormLayout.FieldRole, self.reg_std_address)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_6.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_11)
        self.reg_std_class_list = QtGui.QListWidget(self.groupBox)
        self.reg_std_class_list.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.reg_std_class_list.setObjectName(_fromUtf8("reg_std_class_list"))
        self.formLayout_6.setWidget(6, QtGui.QFormLayout.FieldRole, self.reg_std_class_list)
        self.gridLayout_4.addLayout(self.formLayout_6, 2, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tab_4.addTab(self.register_tab, _fromUtf8(""))
        self.records_tab = QtGui.QWidget()
        self.records_tab.setObjectName(_fromUtf8("records_tab"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.records_tab)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.verticalLayout_24 = QtGui.QVBoxLayout()
        self.verticalLayout_24.setObjectName(_fromUtf8("verticalLayout_24"))
        self.groupBox_4 = QtGui.QGroupBox(self.records_tab)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.formLayout_12 = QtGui.QFormLayout(self.groupBox_4)
        self.formLayout_12.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_12.setObjectName(_fromUtf8("formLayout_12"))
        self.label_18 = QtGui.QLabel(self.groupBox_4)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.formLayout_12.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_18)
        self.res_class = QtGui.QComboBox(self.groupBox_4)
        self.res_class.setObjectName(_fromUtf8("res_class"))
        self.formLayout_12.setWidget(0, QtGui.QFormLayout.FieldRole, self.res_class)
        self.label_12 = QtGui.QLabel(self.groupBox_4)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_12.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_12)
        self.res_std_id = QtGui.QComboBox(self.groupBox_4)
        self.res_std_id.setObjectName(_fromUtf8("res_std_id"))
        self.formLayout_12.setWidget(1, QtGui.QFormLayout.FieldRole, self.res_std_id)
        self.label_19 = QtGui.QLabel(self.groupBox_4)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.formLayout_12.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_19)
        self.res_date_from = QtGui.QDateEdit(self.groupBox_4)
        self.res_date_from.setObjectName(_fromUtf8("res_date_from"))
        self.formLayout_12.setWidget(3, QtGui.QFormLayout.FieldRole, self.res_date_from)
        self.label_20 = QtGui.QLabel(self.groupBox_4)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.formLayout_12.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_20)
        self.res_date_to = QtGui.QDateEdit(self.groupBox_4)
        self.res_date_to.setObjectName(_fromUtf8("res_date_to"))
        self.formLayout_12.setWidget(4, QtGui.QFormLayout.FieldRole, self.res_date_to)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.export_button = QtGui.QPushButton(self.groupBox_4)
        self.export_button.setObjectName(_fromUtf8("export_button"))
        self.horizontalLayout_4.addWidget(self.export_button)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.res_reset_btn = QtGui.QPushButton(self.groupBox_4)
        self.res_reset_btn.setObjectName(_fromUtf8("res_reset_btn"))
        self.horizontalLayout_4.addWidget(self.res_reset_btn)
        self.res_display_btn = QtGui.QPushButton(self.groupBox_4)
        self.res_display_btn.setObjectName(_fromUtf8("res_display_btn"))
        self.horizontalLayout_4.addWidget(self.res_display_btn)
        self.formLayout_12.setLayout(5, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.verticalLayout_24.addWidget(self.groupBox_4)
        self.frame_2 = QtGui.QFrame(self.records_tab)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_24.addWidget(self.frame_2)
        self.horizontalLayout_11.addLayout(self.verticalLayout_24)
        self.groupBox_3 = QtGui.QGroupBox(self.records_tab)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.verticalLayout_23 = QtGui.QVBoxLayout()
        self.verticalLayout_23.setObjectName(_fromUtf8("verticalLayout_23"))
        self.res_table_view = QtGui.QTableWidget(self.groupBox_3)
        self.res_table_view.setObjectName(_fromUtf8("res_table_view"))
        self.res_table_view.setColumnCount(0)
        self.res_table_view.setRowCount(0)
        self.res_table_view.horizontalHeader().setDefaultSectionSize(120)
        self.verticalLayout_23.addWidget(self.res_table_view)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_13 = QtGui.QLabel(self.groupBox_3)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_10.addWidget(self.label_13)
        self.result_count = QtGui.QLabel(self.groupBox_3)
        self.result_count.setObjectName(_fromUtf8("result_count"))
        self.horizontalLayout_10.addWidget(self.result_count)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem12)
        self.verticalLayout_23.addLayout(self.horizontalLayout_10)
        self.gridLayout_6.addLayout(self.verticalLayout_23, 0, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.horizontalLayout_11.addWidget(self.groupBox_3)
        self.tab_4.addTab(self.records_tab, _fromUtf8(""))
        self.verticalLayout_5.addWidget(self.tab_4)
        spacerItem13 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem13)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.retranslateUi(admin)
        self.tab_4.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(admin)

    def retranslateUi(self, admin):
        admin.setWindowTitle(_translate("admin", "Fingerprint Attendance (Admin)", None))
        self.label.setText(_translate("admin", "Fingerprint Based Attendance System", None))
        self.label_9.setText(_translate("admin", "By", None))
        self.label_10.setText(_translate("admin", "Saqib Shabir", None))
        self.groupBox_2.setTitle(_translate("admin", "Classes", None))
        self.groupBox_5.setTitle(_translate("admin", "GroupBox", None))
        self.label_7.setText(_translate("admin", "Class ID", None))
        self.label_24.setText(_translate("admin", "Class Code", None))
        self.label_25.setText(_translate("admin", "Teacher Name", None))
        self.add_class_btn.setText(_translate("admin", "Add Class", None))
        self.tab_4.setTabText(self.tab_4.indexOf(self.add_class_tab), _translate("admin", "Add Class", None))
        self.groupBox.setTitle(_translate("admin", "Student Details", None))
        self.label_6.setText(_translate("admin", "Status ", None))
        self.reg_std_upload_btn.setText(_translate("admin", "Upload Image", None))
        self.reg_std_add_finger_btn.setText(_translate("admin", "Add Fingerprint", None))
        self.reg_std_btn.setText(_translate("admin", "Register", None))
        self.label_2.setText(_translate("admin", " Student ID", None))
        self.label_3.setText(_translate("admin", " Name", None))
        self.label_14.setText(_translate("admin", " DOB", None))
        self.label_4.setText(_translate("admin", " Guardian ", None))
        self.label_5.setText(_translate("admin", " Address", None))
        self.label_11.setText(_translate("admin", " Classes", None))
        self.tab_4.setTabText(self.tab_4.indexOf(self.register_tab), _translate("admin", "Register", None))
        self.groupBox_4.setTitle(_translate("admin", "GroupBox", None))
        self.label_18.setText(_translate("admin", "Class", None))
        self.label_12.setText(_translate("admin", "Student ID", None))
        self.label_19.setText(_translate("admin", "From", None))
        self.label_20.setText(_translate("admin", "To", None))
        self.export_button.setText(_translate("admin", "Export Report", None))
        self.res_reset_btn.setText(_translate("admin", "Reset", None))
        self.res_display_btn.setText(_translate("admin", "Display", None))
        self.groupBox_3.setTitle(_translate("admin", "Attendance Results", None))
        self.label_13.setText(_translate("admin", "Total Attendence :", None))
        self.result_count.setText(_translate("admin", "0", None))
        self.tab_4.setTabText(self.tab_4.indexOf(self.records_tab), _translate("admin", "Display Record", None))

import resource_rc
