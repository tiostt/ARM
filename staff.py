from form import staff_form

from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore

from models import Staff

import re
import peewee


class Addedit_Staff(QMainWindow, staff_form.Ui_AddEditForm):
    def __init__(self, parent=None, staff=None):
        super(Addedit_Staff, self).__init__(parent)
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.staff = staff
        
        selected_date = self.get_selected_date()
        self.lineEdit_expiration_dateStaff.setText(selected_date.strftime("%d.%m.%Y"))
        self.calendarWidget_Staff.clicked.connect(self.get_selected_date)
        self.lineEdit_expiration_dateStaff.setReadOnly(True)

        self.lineEdit_ContactInfo.setInputMask('+7 (999) 999-9999')

        self.OkBtn.setDefault(True)
        self.CancelBtn.setDefault(True)

        self.OkBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.CancelBtn.setFocusPolicy(QtCore.Qt.StrongFocus)

        if self.staff:
            pass
        else:
            self.OkBtn.clicked.connect(self.create_Staff)

        self.CancelBtn.clicked.connect(self.close)
        
    def closeEvent(self, event):
        if self.parent() is not None:
            self.parent().loaddata_staff()
            self.parent().loaddata_venicle()
        super(Addedit_Staff, self).closeEvent(event) 

    def get_selected_date(self):
        selected_date = self.calendarWidget_Staff.selectedDate()
        if self.lineEdit_expiration_dateStaff.text() == "":
            return selected_date.toPyDate()
        else:
            selected_date = selected_date.toPyDate()
            self.lineEdit_expiration_dateStaff.setText(selected_date.strftime("%d.%m.%Y"))

    def validator(self):
        if (self.lineEdit_Namestaff.text() == "" or len(self.lineEdit_Namestaff.text()) <= 2):
            QMessageBox.critical(self, 'Ошибка', 'Вы не заполнили поле "Имя" или введенное вами слово меньше 3 букв!')
            return False
        elif (self.lineEdit_ContactInfoStaff.text() == "" or len(self.lineEdit_ContactInfoStaff.text()) <= 2):
            QMessageBox.critical(self, 'Ошибка', 'Вы не заполнили поле "Фамилия" или введенное вами слово меньше 3 букв!')
            return False
        elif (self.lineEdit_ContactInfo.text() == "" or len(self.lineEdit_ContactInfo.text()) < 17):
            QMessageBox.critical(self, 'Ошибка', 'Вы не заполнили поле "Номер телефона"!')
            return False
        elif (self.lineEdit_priceStaff.text() == "" or len(self.lineEdit_priceStaff.text()) <= 2):
            QMessageBox.critical(self, 'Ошибка', 'Вы не заполнили поле "Отчество" или введенное вами слово меньше 3 букв!')
            return False
        elif (self.lineEdit_priceStaff_2.text() == "" or len(self.lineEdit_priceStaff_2.text()) <= 2):
            QMessageBox.critical(self, 'Ошибка', 'Вы не заполнили поле "Должность" или введенное вами слово меньше 3 букв!')
            return False
        else:
            return True


    def create_Staff(self):
        if self.validator():
            firstName = self.lineEdit_Namestaff.text()
            lastName = self.lineEdit_ContactInfoStaff.text()
            middleName = self.lineEdit_priceStaff.text()
            сontactInfo = self.lineEdit_ContactInfo.text()
            position = self.lineEdit_priceStaff_2.text()
            hireDate = self.lineEdit_expiration_dateStaff.text()

            try:
                Staff(
                    firstName=firstName,
                    lastName=lastName,
                    middleName=middleName,
                    сontactInfo = сontactInfo,
                    position=position,
                    hireDate=hireDate,
                ).save()
                self.close()
            except peewee.IntegrityError:
                QMessageBox.critical(self, 'Ошибка', 'Сотрудник с таким номером телефона уже существует!')

    def edit_Staff(self, staff):
        self.lineEdit_Namestaff.setText(staff.firstName)
        self.lineEdit_ContactInfoStaff.setText(staff.lastName)
        self.lineEdit_priceStaff.setText(staff.middleName)
        self.lineEdit_ContactInfo.setText(staff.сontactInfo)
        self.lineEdit_priceStaff_2.setText(staff.position)
        self.lineEdit_expiration_dateStaff.setText(str(staff.hireDate.strftime('%d.%m.%Y')))
        self.calendarWidget_Staff.setSelectedDate(staff.hireDate)

        self.OkBtn.clicked.connect(lambda: self.update_Staff(staff))

    def update_Staff(self, staff):
        if self.validator():
            update = Staff.get(Staff.id == staff.id)
            update.firstName = self.lineEdit_Namestaff.text()
            update.lastName = self.lineEdit_ContactInfoStaff.text()
            update.middleName = self.lineEdit_priceStaff.text()
            update.сontactInfo = self.lineEdit_ContactInfo.text()
            update.position = self.lineEdit_priceStaff_2.text()
            update.hireDate = self.lineEdit_expiration_dateStaff.text()
            
            try:
                update.save()
                self.close()
            except peewee.IntegrityError:
                QMessageBox.critical(self, 'Ошибка', 'Сотрудник с таким номером телефона уже существует!')

    def delete_Staff(self, staff):
        msg = QMessageBox()
        msg.setWindowTitle("Подтверждение удаления")
        msg.setText(f"Вы уверены, что хотите удалить '{staff.lastName} {staff.firstName} {staff.middleName}'?")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Задаем русские названия кнопкам
        msg.button(QMessageBox.Yes).setText('Да')
        msg.button(QMessageBox.No).setText('Нет')

        confirm = msg.exec_()
        if confirm == QMessageBox.Yes:
            try:
                staff.delete_instance()
            except peewee.IntegrityError:
                QMessageBox.critical(self, 'Ошибка', f'На запись "{staff.lastName} {staff.firstName} {staff.middleName}" есть ссылка в другой таблице')
            if self.parent() is not None:
                self.parent().loaddata_staff()  # Обновляем данные в таблице