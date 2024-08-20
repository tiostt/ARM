from form import product_form

from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore

from models import Products, Suppliers

import re
import peewee

class Addedit_Product(QMainWindow, product_form.Ui_AddEditForm):
    def __init__(self, parent=None, product=None):
        super(Addedit_Product, self).__init__(parent)
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.product = product
        self.pattern_quantity = re.compile(r'^(\d+|\d+\.\d+)$')

        self.OkBtn.setDefault(True)
        self.CancelBtn.setDefault(True)

        self.OkBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.CancelBtn.setFocusPolicy(QtCore.Qt.StrongFocus)

        self.CancelBtn.clicked.connect(self.close)

        self.loaddata_combobox()
        
    def closeEvent(self, event):
        if self.parent() is not None:
            self.parent().loaddata_Product()
            self.parent().loaddata_order()
        super(Addedit_Product, self).closeEvent(event) 

    def loaddata_combobox(self):
        self.comboBox_supplier.clear()
        data_supplier = [x for x in Suppliers.select()]
        
        for supplier in data_supplier:
            self.comboBox_supplier.addItem(supplier.name, supplier.id)
            
    def validator(self):
        text_line = self.lineEdit_NameProduct.text()
        if self.lineEdit_NameProduct.text() == "" or len(text_line) <= 2:
            QMessageBox.critical(self, 'Ошибка', 'Вы не заполнили поле "Название" или введенное вами слово меньше 3 букв!')
            return False
        elif self.comboBox_supplier.currentText() == "":
            QMessageBox.critical(self, 'Ошибка', 'Вы не заполнили поле "Поставщик" или сама таблица пуста')
            return False
        elif not self.pattern_quantity.search(self.lineEdit_quantityProduct.text()) or float(self.lineEdit_quantityProduct.text()) == 0:
            QMessageBox.critical(self, 'Ошибка', 'Вы не корректно заполнили поле "Колличество"!')
            return False
        elif not self.pattern_quantity.search(self.lineEdit_price.text()) or float(self.lineEdit_price.text()) == 0:
            QMessageBox.critical(self, 'Ошибка', 'Вы не корректно заполнили поле "Цена"!')
            return False
        else:
            return True

    
    def edit_product(self, product):
        index = self.comboBox_supplier.findData(product.suppliers.id)
        self.comboBox_supplier.setCurrentIndex(index)
        
        self.lineEdit_NameProduct.setText(product.name)
        self.lineEdit_quantityProduct.setText(str(product.quantity))
        self.lineEdit_price.setText(str(product.price ))

        self.OkBtn.clicked.connect(lambda: self.update_product(product))

    def update_product(self, product):
        if self.validator():
            update = Products.get(Products.id == product.id)
            update.name = self.lineEdit_NameProduct.text()
            update.quantity = self.lineEdit_quantityProduct.text()
            update.suppliers  = self.comboBox_supplier.currentData()
            update.price = self.lineEdit_price.text()
            try:
                update.save()
                self.close()
            except peewee.DataError:
                QMessageBox.critical(self, 'Ошибка', 'Цена не может превышать 100 тысяч рублей')
            except peewee.IntegrityError:
                QMessageBox.critical(self, 'Ошибка', 'Товар с таким именем уже существует!')

    def delete_product(self, product):
        msg = QMessageBox()
        msg.setWindowTitle("Подтверждение удаления")
        msg.setText(f"Вы уверены, что хотите удалить '{product.name}|{product.suppliers.name}'?")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Задаем русские названия кнопкам
        msg.button(QMessageBox.Yes).setText('Да')
        msg.button(QMessageBox.No).setText('Нет')

        confirm = msg.exec_()
        if confirm == QMessageBox.Yes:
            try:
                product.delete_instance()
            except peewee.IntegrityError:
                QMessageBox.critical(self, 'Ошибка', f'На запись "{product.name}|{product.suppliers.name}" есть ссылка в другой таблице')
            if self.parent() is not None:
                self.parent().loaddata_Product()  # Обновляем данные в таблице