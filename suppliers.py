from form import suppliers_form

from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore

from models import *

import peewee

class Addedit_suppliers(QMainWindow, suppliers_form.Ui_AddEditForm):
    def __init__(self, parent=None, suppliers=None):
        super(Addedit_suppliers, self).__init__(parent)
        self.setupUi(self)
        self.suppliers = suppliers
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.lineEdit_ContactInfosuppliers.setInputMask('+7 (999) 999-9999')

        self.OkBtn.setDefault(True)
        self.CancelBtn.setDefault(True)

        self.OkBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.CancelBtn.setFocusPolicy(QtCore.Qt.StrongFocus)

        if self.suppliers:
            pass
        else:
            self.OkBtn.clicked.connect(self.create_suppliers)

        self.CancelBtn.clicked.connect(self.close)

    def closeEvent(self, event):
        if self.parent() is not None:
            self.parent().loaddata_suppliers()
            self.parent().loaddata_Product()
            self.parent().loaddata_delivery()
        super(Addedit_suppliers, self).closeEvent(event) 

    def validator(self):
        text_line = self.lineEdit_Namesuppliers.text()
        if self.lineEdit_Namesuppliers.text() == "" or len(text_line) <= 2:
            QMessageBox.critical(self, 'Ошибка', 'Вы не заполнили поле "Название" или введенное вами слово меньше 3 букв!')
            return False
        if self.lineEdit_ContactInfosuppliers.text() == "" or len(self.lineEdit_ContactInfosuppliers.text()) < 17:
            QMessageBox.critical(self, 'Ошибка', 'Вы не заполнили поле "Номер телефона"!')
            return False
        else:
            return True

    def create_suppliers(self):
        if self.validator():
            name = self.lineEdit_Namesuppliers.text()
            contactInfo = self.lineEdit_ContactInfosuppliers.text()
        
            try:
                Suppliers(
                    name=name,
                    сontactInfo=contactInfo,
                ).save()
                self.close() 
            except peewee.IntegrityError:
                QMessageBox.critical(self, 'Ошибка', 'Поставщик с таким именем или номером телефона уже существует!')

    def edit_suppliers(self, suppliers):
        self.lineEdit_Namesuppliers.setText(suppliers.name)
        self.lineEdit_ContactInfosuppliers.setText(suppliers.сontactInfo)

        self.OkBtn.clicked.connect(lambda: self.update_suppliers(suppliers))

    def update_suppliers(self, suppliers):
        if self.validator():
            update = Suppliers.get(Suppliers.id == suppliers.id)
            update.name = self.lineEdit_Namesuppliers.text()
            update.сontactInfo = self.lineEdit_ContactInfosuppliers.text()
            try:
                update.save()
                self.close()
            except peewee.IntegrityError:
                QMessageBox.critical(self, 'Ошибка', 'Поставщик с таким именем или номером телефона уже существует!')

    def delete_suppliers(self, suppliers):
        msg = QMessageBox()
        msg.setWindowTitle("Подтверждение удаления")
        msg.setText(f"Вы уверены, что хотите удалить '{suppliers.name}'?")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Задаем русские названия кнопкам
        msg.button(QMessageBox.Yes).setText('Да')
        msg.button(QMessageBox.No).setText('Нет')

        confirm = msg.exec_()
        if confirm == QMessageBox.Yes:
            try:
                suppliers.delete_instance()
            except peewee.IntegrityError:
                QMessageBox.critical(self, 'Ошибка', f'На запись "{suppliers.name}" есть ссылка в другой таблице')
            if self.parent() is not None:
                self.parent().loaddata_suppliers()  # Обновляем данные в таблице
