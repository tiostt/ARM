# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Product.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddEditForm(object):
    def setupUi(self, AddEditForm):
        AddEditForm.setObjectName("AddEditForm")
        AddEditForm.resize(500, 560)
        AddEditForm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(AddEditForm)
        self.centralwidget.setObjectName("centralwidget")
        self.labelProduct1 = QtWidgets.QLabel(self.centralwidget)
        self.labelProduct1.setGeometry(QtCore.QRect(50, 20, 381, 31))
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
        self.labelProduct2.setGeometry(QtCore.QRect(50, 120, 381, 16))
        self.labelProduct2.setStyleSheet('font: 75 12pt "MS Shell Dlg 2";')
        self.labelProduct2.setObjectName("labelProduct2")
        self.labelProduct3 = QtWidgets.QLabel(self.centralwidget)
        self.labelProduct3.setGeometry(QtCore.QRect(50, 220, 401, 31))
        self.labelProduct3.setStyleSheet('font: 75 12pt "MS Shell Dlg 2";')
        self.labelProduct3.setObjectName("labelProduct3")
        self.lineEdit_NameProduct = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_NameProduct.setGeometry(QtCore.QRect(40, 60, 421, 41))
        self.lineEdit_NameProduct.setStyleSheet(
            "QLineEdit {\n"
            "    border: 3 solid rgb(0, 0, 0);\n"
            "    border-radius: 10;\n"
            "    padding: 5;\n"
            "    \n"
            '    font: 75 10pt "MS Shell Dlg 2";\n'
            "}"
        )
        self.lineEdit_NameProduct.setText("")
        self.lineEdit_NameProduct.setObjectName("lineEdit_NameProduct")
        self.lineEdit_quantityProduct = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_quantityProduct.setGeometry(QtCore.QRect(40, 160, 421, 41))
        self.lineEdit_quantityProduct.setStyleSheet(
            "QLineEdit {\n"
            "    border: 3 solid rgb(0, 0, 0);\n"
            "    border-radius: 10;\n"
            "    padding: 5;\n"
            "    \n"
            '    font: 75 10pt "MS Shell Dlg 2";\n'
            "}"
        )
        self.lineEdit_quantityProduct.setObjectName("lineEdit_quantityProduct")
        self.comboBox_supplier = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_supplier.setGeometry(QtCore.QRect(40, 260, 421, 41))
        self.comboBox_supplier.setStyleSheet(
            "QComboBox{    \n"
            "    border: 3 solid rgb(0, 0, 0);\n"
            "    border-radius: 10;\n"
            "    padding: 5;\n"
            '    font: 75 10pt "MS Shell Dlg 2";\n'
            "}\n"
            "QComboBox::drop-down {\n"
            "    background-color: rgb(255, 255, 255);\n"
            "    border-radius: 8;\n"
            "    width: 30;\n"
            "}\n"
            "QComboBox::down-arrow {\n"
            "    width: 0px;\n"
            "    height: 0px;\n"
            "    border-left: 5px solid transparent;\n"
            "    border-right: 5px solid transparent;\n"
            "    border-top: 5px solid black; /* Цвет стрелки */\n"
            "}\n"
            "QComboBox QAbstractItemView {\n"
            "    margin-top: 2;\n"
            "    color: rgb(255, 255, 255);\n"
            "    background-color: #373e4e;\n"
            "    padding: 10;\n"
            "    selection-background-color: rgb(39, 44, 54);\n"
            "}"
        )
        self.comboBox_supplier.setObjectName("comboBox_supplier")
        self.lineEdit_price = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_price.setGeometry(QtCore.QRect(40, 360, 421, 41))
        self.lineEdit_price.setStyleSheet(
            "QLineEdit {\n"
            "    border: 3 solid rgb(0, 0, 0);\n"
            "    border-radius: 10;\n"
            "    padding: 5;\n"
            "    \n"
            '    font: 75 10pt "MS Shell Dlg 2";\n'
            "}"
        )
        self.lineEdit_price.setObjectName("lineEdit_price")
        self.OkBtn = QtWidgets.QPushButton(self.centralwidget)
        self.OkBtn.setGeometry(QtCore.QRect(50, 450, 130, 70))
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
        self.OkBtn.setObjectName("OkBtn")
        self.CancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.CancelBtn.setGeometry(QtCore.QRect(320, 450, 130, 70))
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
        self.labelProduct3_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelProduct3_2.setGeometry(QtCore.QRect(50, 320, 401, 31))
        self.labelProduct3_2.setStyleSheet('font: 75 12pt "MS Shell Dlg 2";')
        self.labelProduct3_2.setObjectName("labelProduct3_2")
        
        AddEditForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddEditForm)
        QtCore.QMetaObject.connectSlotsByName(AddEditForm)

    def retranslateUi(self, AddEditForm):
        _translate = QtCore.QCoreApplication.translate
        AddEditForm.setWindowTitle(_translate("AddEditForm", "Добавить товар"))
        self.labelProduct1.setText(_translate("AddEditForm", "Наименование товара"))
        self.labelProduct2.setText(_translate("AddEditForm", "количество в тоннах"))
        self.labelProduct3.setText(_translate("AddEditForm", "Поставщик"))
        self.OkBtn.setText(_translate("AddEditForm", "OK"))
        self.CancelBtn.setText(_translate("AddEditForm", "Отмена"))
        self.labelProduct3_2.setText(_translate("AddEditForm", "Цена за тонну"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AddEditForm = QtWidgets.QMainWindow()
    ui = Ui_AddEditForm()
    ui.setupUi(AddEditForm)
    AddEditForm.show()
    sys.exit(app.exec_())
