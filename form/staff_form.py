# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'staff.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddEditForm(object):
    def setupUi(self, AddEditForm):
        AddEditForm.setObjectName("AddEditForm")
        AddEditForm.setFixedSize(965, 599)
        AddEditForm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(AddEditForm)
        self.centralwidget.setObjectName("centralwidget")
        self.labelProduct1 = QtWidgets.QLabel(self.centralwidget)
        self.labelProduct1.setGeometry(QtCore.QRect(50, 120, 381, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.labelProduct1.sizePolicy().hasHeightForWidth()
        )
        self.labelProduct1.setSizePolicy(sizePolicy)
        self.labelProduct1.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.labelProduct1.setStyleSheet('font: 75 12pt "MS Shell Dlg 2";')
        self.labelProduct1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelProduct1.setTextFormat(QtCore.Qt.AutoText)
        self.labelProduct1.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.labelProduct1.setWordWrap(False)
        self.labelProduct1.setObjectName("labelProduct1")
        self.labelProduct2 = QtWidgets.QLabel(self.centralwidget)
        self.labelProduct2.setGeometry(QtCore.QRect(50, 215, 381, 31))
        self.labelProduct2.setStyleSheet('font: 75 12pt "MS Shell Dlg 2";')
        self.labelProduct2.setObjectName("labelProduct2")
        self.labelProduct3 = QtWidgets.QLabel(self.centralwidget)
        self.labelProduct3.setGeometry(QtCore.QRect(520, 20, 401, 31))
        self.labelProduct3.setStyleSheet('font: 75 12pt "MS Shell Dlg 2";')
        self.labelProduct3.setObjectName("labelProduct3")
        self.lineEdit_Namestaff = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Namestaff.setGeometry(QtCore.QRect(40, 60, 421, 41))
        self.lineEdit_Namestaff.setStyleSheet(
            "QLineEdit {\n"
            "    border: 3 solid rgb(0, 0, 0);\n"
            "    border-radius: 10;\n"
            "    padding: 5;\n"
            "    \n"
            '    font: 75 10pt "MS Shell Dlg 2";\n'
            "}"
        )
        self.lineEdit_Namestaff.setText("")
        self.lineEdit_Namestaff.setObjectName("lineEdit_Namestaff")
        self.lineEdit_ContactInfoStaff = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ContactInfoStaff.setGeometry(QtCore.QRect(40, 160, 421, 41))
        self.lineEdit_ContactInfoStaff.setStyleSheet(
            "QLineEdit {\n"
            "    border: 3 solid rgb(0, 0, 0);\n"
            "    border-radius: 10;\n"
            "    padding: 5;\n"
            "    \n"
            '    font: 75 10pt "MS Shell Dlg 2";\n'
            "}"
        )
        self.lineEdit_ContactInfoStaff.setText("")
        self.lineEdit_ContactInfoStaff.setObjectName("lineEdit_ContactInfoStaff")
        self.lineEdit_priceStaff = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_priceStaff.setGeometry(QtCore.QRect(40, 260, 421, 41))
        self.lineEdit_priceStaff.setStyleSheet(
            "QLineEdit {\n"
            "    border: 3 solid rgb(0, 0, 0);\n"
            "    border-radius: 10;\n"
            "    padding: 5;\n"
            "    \n"
            '    font: 75 10pt "MS Shell Dlg 2";\n'
            "}"
        )
        self.lineEdit_priceStaff.setObjectName("lineEdit_priceStaff")
        self.lineEdit_ContactInfo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ContactInfo.setGeometry(QtCore.QRect(40, 360, 421, 41))
        self.lineEdit_ContactInfo.setStyleSheet(
            "QLineEdit {\n"
            "    border: 3 solid rgb(0, 0, 0);\n"
            "    border-radius: 10;\n"
            "    padding: 5;\n"
            "    \n"
            '    font: 75 10pt "MS Shell Dlg 2";\n'
            "}"
        )
        self.lineEdit_ContactInfo.setObjectName("lineEdit_ContactInfo")
        self.lineEdit_priceStaff_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_priceStaff_2.setGeometry(QtCore.QRect(510, 65, 421, 41))
        self.lineEdit_priceStaff_2.setStyleSheet(
            "QLineEdit {\n"
            "    border: 3 solid rgb(0, 0, 0);\n"
            "    border-radius: 10;\n"
            "    padding: 5;\n"
            "    \n"
            '    font: 75 10pt "MS Shell Dlg 2";\n'
            "}"
        )
        self.lineEdit_priceStaff_2.setObjectName("lineEdit_priceStaff_2")
        self.lineEdit_expiration_dateStaff = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_expiration_dateStaff.setGeometry(QtCore.QRect(510, 165, 421, 41))
        self.lineEdit_expiration_dateStaff.setStyleSheet(
            "QLineEdit {\n"
            "    border: 3 solid rgb(0, 0, 0);\n"
            "    border-radius: 10;\n"
            "    padding: 5;\n"
            "    \n"
            '    font: 75 10pt "MS Shell Dlg 2";\n'
            "}"
        )
        self.lineEdit_expiration_dateStaff.setText("")
        self.lineEdit_expiration_dateStaff.setObjectName(
            "lineEdit_expiration_dateStaff"
        )
        self.labelProduct3_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelProduct3_2.setGeometry(QtCore.QRect(520, 120, 401, 31))
        self.labelProduct3_2.setStyleSheet('font: 75 12pt "MS Shell Dlg 2";')
        self.labelProduct3_2.setObjectName("labelProduct3_2")
        self.calendarWidget_Staff = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget_Staff.setGeometry(QtCore.QRect(520, 220, 401, 241))
        self.calendarWidget_Staff.setStyleSheet(
            "background-color: rgb(67, 202, 202);\n"
            'font: 75 9pt "MS Shell Dlg 2";\n'
            "border-radius: 10;\n"
            "color: rgb(0, 0, 0);"
        )
        self.calendarWidget_Staff.setObjectName("calendarWidget_Staff")
        self.OkBtn = QtWidgets.QPushButton(self.centralwidget)
        self.OkBtn.setGeometry(QtCore.QRect(50, 500, 130, 70))
        self.OkBtn.setStyleSheet(
            "QPushButton {\n"
            "     border-radius: 10px;\n"
            "     background-color: #0E0188;\n"
            "    color: rgb(255, 255, 255);\n"
            '    font: 75 14pt "MS Shell Dlg 2";\n'
            "}\n"
            "QPushButton:hover {\n"
            "    background-color: #070049;\n"
            "}\n"
            ""
        )
        self.OkBtn.setCheckable(False)
        self.OkBtn.setChecked(False)
        self.OkBtn.setObjectName("OkBtn")
        self.CancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.CancelBtn.setGeometry(QtCore.QRect(770, 500, 130, 70))
        self.CancelBtn.setStyleSheet(
            " QPushButton {\n"
            "     border-radius: 10px;\n"
            "     background-color: #0E0188;\n"
            "    color: rgb(255, 255, 255);\n"
            '    font: 75 14pt "MS Shell Dlg 2";\n'
            "}\n"
            "QPushButton:hover {\n"
            "    background-color: #070049;\n"
            "}\n"
            ""
        )
        self.CancelBtn.setObjectName("CancelBtn")
        
        self.labelProduct2_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelProduct2_2.setGeometry(QtCore.QRect(50, 315, 381, 31))
        self.labelProduct2_2.setStyleSheet('font: 75 12pt "MS Shell Dlg 2";')
        self.labelProduct2_2.setObjectName("labelProduct2_2")
        self.labelProduct1_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelProduct1_2.setGeometry(QtCore.QRect(50, 20, 381, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.labelProduct1_2.sizePolicy().hasHeightForWidth()
        )
        self.labelProduct1_2.setSizePolicy(sizePolicy)
        self.labelProduct1_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.labelProduct1_2.setStyleSheet('font: 75 12pt "MS Shell Dlg 2";')
        self.labelProduct1_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelProduct1_2.setTextFormat(QtCore.Qt.AutoText)
        self.labelProduct1_2.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.labelProduct1_2.setWordWrap(False)
        self.labelProduct1_2.setObjectName("labelProduct1_2")
        AddEditForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddEditForm)
        QtCore.QMetaObject.connectSlotsByName(AddEditForm)

    def retranslateUi(self, AddEditForm):
        _translate = QtCore.QCoreApplication.translate
        AddEditForm.setWindowTitle(_translate("AddEditForm", "Добавить сотрудника"))
        self.labelProduct1.setText(_translate("AddEditForm", "Фамилия"))
        self.labelProduct2.setText(_translate("AddEditForm", "Отчество"))
        self.labelProduct3.setText(_translate("AddEditForm", "Должность"))
        self.OkBtn.setText(_translate("AddEditForm", "OK"))
        self.CancelBtn.setText(_translate("AddEditForm", "Отмена"))
        self.labelProduct2_2.setText(_translate("AddEditForm", "Номер телефона"))
        self.labelProduct1_2.setText(_translate("AddEditForm", "Имя"))
        self.labelProduct3_2.setText(_translate("AddEditForm", "Дата найма"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AddEditForm = QtWidgets.QMainWindow()
    ui = Ui_AddEditForm()
    ui.setupUi(AddEditForm)
    AddEditForm.show()
    sys.exit(app.exec_())
