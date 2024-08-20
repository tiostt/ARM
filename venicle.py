from form import venicle_form

from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore

from models import Venicle, Staff

import re
import peewee

class Addedit_venicle(QMainWindow, venicle_form.Ui_AddEditForm):
    def __init__(self, parent=None, venicle=None):
        super(Addedit_venicle, self).__init__(parent)
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.venicle = venicle
        self.pattern_capacity = re.compile(r'^(\d+|\d+\.\d+)$')
        
        selected_date = self.get_selected_date()
        self.lineEdit_date_venicle.setText(selected_date.strftime("%d.%m.%Y"))
        self.calendarWidget_venicle.clicked.connect(self.get_selected_date)
        self.lineEdit_date_venicle.setReadOnly(True)

        self.lineEdit_registrationNumber_venicle.setInputMask("A-999-AA-999")

        self.loaddata_combobox()

        self.OkBtn.setDefault(True)
        self.CancelBtn.setDefault(True)

        self.OkBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.CancelBtn.setFocusPolicy(QtCore.Qt.StrongFocus)

        if self.venicle:
            pass
        else:
            self.OkBtn.clicked.connect(self.create_venicle)

        self.CancelBtn.clicked.connect(self.close)
        
    def closeEvent(self, event):
        if self.parent() is not None:
            self.parent().loaddata_venicle()
            self.parent().loaddata_delivery()
            self.parent().loaddata_order()
        super(Addedit_venicle, self).closeEvent(event) 

    def get_selected_date(self):# -> Any | None:
        selected_date = self.calendarWidget_venicle.selectedDate()
        if self.lineEdit_date_venicle.text() == "":
            return selected_date.toPyDate()
        else:
            selected_date = selected_date.toPyDate()
            self.lineEdit_date_venicle.setText(selected_date.strftime("%d.%m.%Y"))

    def validate_registration_number(self, text):
        # Регулярное выражение для проверки формата регистрационного номера с дефисами
        pattern = r'^[А-Яа-я]-\d{3}-[А-Яа-я]{2}-\d{3}$'  # Обновлено для соответствия маске с дефисами
        if not re.match(pattern, text):
            QMessageBox.critical(self, 'Ошибка', 'Вы не заполнили поле "Регистрационный номер" или ввели не кириллицу!')
            return False
        return True

    def validator(self):
        if self.comboBox_venicle.currentText() == "":
            QMessageBox.critical(self, 'Ошибка', 'Вы не выбрали поле "Сотрудник" или сама таблица пуста')
            return False
        elif self.lineEdit_mode_venicle.text() == "" or len(self.lineEdit_mode_venicle.text()) <= 2:
            QMessageBox.critical(self, 'Ошибка', 'Вы не заполнили поле "Модель машины" или введенное вами слово меньше 3 букв!')
            return False
        elif not self.validate_registration_number(self.lineEdit_registrationNumber_venicle.text()):
            return False
        elif not self.pattern_capacity.search(self.lineEdit_capacity_venicle.text()) or float(self.lineEdit_capacity_venicle.text()) == 0:
            QMessageBox.critical(self, 'Ошибка', 'Вы не корректно заполнили поле "Грузоподъемность"!')
            return False
        else:
            return True

    def loaddata_combobox(self):
        self.comboBox_venicle.clear()
        data = [x for x in Staff.select()]
        
        for i in data:
            staff_name = f"{i.lastName} {i.firstName} {i.middleName}"
            self.comboBox_venicle.addItem(staff_name, i.id)

    def create_venicle(self):
        if self.validator():
            staff_id = self.comboBox_venicle.currentData()
            model = self.lineEdit_mode_venicle.text()
            registrationNumber = self.lineEdit_registrationNumber_venicle.text()
            capacity = self.lineEdit_capacity_venicle.text()
            maintenanceDate = self.lineEdit_date_venicle.text()

            try:
                Venicle(
                    staff=staff_id,
                    model=model,
                    registrationNumber=registrationNumber,
                    capacity=capacity,
                    maintenanceDate=maintenanceDate,
                ).save()
                self.close()
            except peewee.IntegrityError:
                QMessageBox.critical(self, 'Ошибка', 'Транспортное средство с таким регистрационным номером уже существует!')

    def edit_venicle(self, venicle):

        self.loaddata_combobox()
        index = self.comboBox_venicle.findData(venicle.staff.id)
        self.comboBox_venicle.setCurrentIndex(index)

        self.lineEdit_mode_venicle.setText(venicle.model)
        self.lineEdit_registrationNumber_venicle.setText(venicle.registrationNumber)
        self.lineEdit_capacity_venicle.setText(str(venicle.capacity ))
        self.lineEdit_date_venicle.setText(str(venicle.maintenanceDate.strftime('%d.%m.%Y')))
        self.calendarWidget_venicle.setSelectedDate(venicle.maintenanceDate)

        self.OkBtn.clicked.connect(lambda: self.update_venicle(venicle))

    def update_venicle(self, venicle):
        if self.validator():
            update = Venicle.get(Venicle.id == venicle.id)
            update.staff = self.comboBox_venicle.currentData()
            update.model = self.lineEdit_mode_venicle.text()
            update.registrationNumber  = self.lineEdit_registrationNumber_venicle.text()
            update.capacity = self.lineEdit_capacity_venicle.text()
            update.maintenanceDate = self.lineEdit_date_venicle.text()

            try:
                update.save()
            except peewee.IntegrityError:
                QMessageBox.critical(self, 'Ошибка', 'Транспортное средство с таким регистрационным номером уже существует!')
            self.close()

    def delete_venicle(self, venicle):
        msg = QMessageBox()
        msg.setWindowTitle("Подтверждение удаления")
        msg.setText(f"Вы уверены, что хотите удалить транспортное средство с номером '{venicle.registrationNumber}'?")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Задаем русские названия кнопкам
        msg.button(QMessageBox.Yes).setText('Да')
        msg.button(QMessageBox.No).setText('Нет')

        confirm = msg.exec_()
        if confirm == QMessageBox.Yes:
            try:
                venicle.delete_instance()
            except peewee.IntegrityError:
                QMessageBox.critical(self, 'Ошибка', f'На запись "{venicle.model}" есть ссылка в другой таблице')
            if self.parent() is not None:
                self.parent().loaddata_venicle()  # Обновляем данные в таблице