from form import clients_form

from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore

from models import Clients

import re
import peewee


class Addedit_clients(QMainWindow, clients_form.Ui_AddEditForm):
    def __init__(self, parent=None, clients=None):
        super(Addedit_clients, self).__init__(parent)
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.clients = clients
        
        self.lineEdit_contact.setInputMask('+7 (999) 999-9999')

        self.OkBtn.setDefault(True)
        self.CancelBtn.setDefault(True)
        self.OkBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.CancelBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        if self.clients:
            pass
        else:
            self.OkBtn.clicked.connect(self.create_Staff)

        self.CancelBtn.clicked.connect(self.close)
        
    def closeEvent(self, event):
        if self.parent() is not None:
            self.parent().loaddata_clients()
            self.parent().loaddata_order()
        super(Addedit_clients, self).closeEvent(event) 

    def validator(self):
        if (self.lineEdit_firstName.text() == "" or len(self.lineEdit_firstName.text()) <= 2):
            QMessageBox.critical(self, 'Ошибка', 'Вы не заполнили поле "Имя" или введенное вами слово меньше 3 букв!')
            return False
        elif (self.lineEdit_lastName.text() == "" or len(self.lineEdit_lastName.text()) <= 2):
            QMessageBox.critical(self, 'Ошибка', 'Вы не заполнили поле "Фамилия" или введенное вами слово меньше 3 букв!')
            return False
        elif (self.lineEdit_middleName.text() == "" or len(self.lineEdit_middleName.text()) <= 2):
            QMessageBox.critical(self, 'Ошибка', 'Вы не заполнили поле "Отчество" или введенное вами слово меньше 3 букв!')
            return False
        elif self.lineEdit_contact.text() == "" or len(self.lineEdit_contact.text()) < 17:
            QMessageBox.critical(self, 'Ошибка', 'Вы не заполнили поле "Номер телефона"!')
            return False
        elif self.lineEdit_Address.text() == "":
            QMessageBox.critical(self, 'Ошибка', 'Вы не заполнили поле "Адрес"')
            return False
        elif self.lineEdit_City.text() == "":
            QMessageBox.critical(self, 'Ошибка', 'Вы не заполнили поле "Город" или введенное вами слово меньше 3 букв!')
            return False
        else:
            return True

    def create_Staff(self):
        if self.validator():
            firstName = self.lineEdit_firstName.text()
            lastName = self.lineEdit_lastName.text()
            middleName = self.lineEdit_middleName.text()
            contact = self.lineEdit_contact.text()
            Address = self.lineEdit_Address.text()
            City = self.lineEdit_City.text()

            try:
                Clients(
                    firstName=firstName,
                    lastName=lastName,
                    middleName=middleName,
                    contact=contact,
                    Address=Address,
                    City=City,
                ).save()
                self.close()
            except peewee.IntegrityError:
                QMessageBox.critical(self, 'Ошибка', 'Клиент с таким номером телефона уже существует!')

    def edit_clients(self, clients):
        self.lineEdit_firstName.setText(clients.firstName)
        self.lineEdit_lastName.setText(clients.lastName)
        self.lineEdit_middleName.setText(clients.middleName)
        self.lineEdit_contact.setText(clients.contact)
        self.lineEdit_Address.setText(clients.Address)
        self.lineEdit_City.setText(clients.City)

        self.OkBtn.clicked.connect(lambda: self.update_Staff(clients))

    def update_Staff(self, clients):
        if self.validator():
            update = Clients.get(Clients.id == clients.id)
            update.firstName = self.lineEdit_firstName.text()
            update.lastName = self.lineEdit_lastName.text()
            update.middleName = self.lineEdit_middleName.text()
            update.contact = self.lineEdit_contact.text()
            update.Address = self.lineEdit_Address.text()
            update.City = self.lineEdit_City.text()

            try:
                update.save()
                self.close()
            except peewee.IntegrityError:
                QMessageBox.critical(self, 'Ошибка', 'Клиент с таким номером телефона уже существует!')

    def delete_clients(self, clients):
        msg = QMessageBox()
        msg.setWindowTitle("Подтверждение удаления")
        msg.setText(f"Вы уверены, что хотите удалить '{clients.lastName} {clients.firstName} {clients.middleName}'?")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Задаем русские названия кнопкам
        msg.button(QMessageBox.Yes).setText('Да')
        msg.button(QMessageBox.No).setText('Нет')

        confirm = msg.exec_()
        if confirm == QMessageBox.Yes:
            try:
                clients.delete_instance()
            except peewee.IntegrityError:
                QMessageBox.critical(self, 'Ошибка', f'На запись "{clients.lastName} {clients.firstName} {clients.middleName}" есть ссылка в другой таблице')
            if self.parent() is not None:
                self.parent().loaddata_clients()  # Обновляем данные в таблице