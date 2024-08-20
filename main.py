from form import main_form
from product import Addedit_Product
from suppliers import Addedit_suppliers
from staff import Addedit_Staff
from venicle import Addedit_venicle
from delivery import Addedit_delivery
from clients import Addedit_clients
from orders import Addedit_orders

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QAbstractItemView
from PyQt5.QtGui import QIcon

from models import *

from peewee import fn
import peewee
import sys


class Application(QMainWindow, main_form.Ui_MainWindow):
    def __init__(self):
        super(Application, self).__init__()
        self.setupUi(self)
        self.sort_order = True

        # Товары
        self.btn_edit_product.setDefault(True)
        self.btn_delete_product.setDefault(True)
        
        self.btn_edit_product.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_delete_product.setFocusPolicy(QtCore.Qt.StrongFocus)

        self.btn_edit_product.clicked.connect(self.open_edit_Product)
        self.btn_delete_product.clicked.connect(self.open_delete_Product)

        self.tableWidget_Product.setColumnCount(4)
        self.tableWidget_Product.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_Product.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_Product.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_Product.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_Product.setHorizontalHeaderLabels(("Название", "Количество т.", "Поставщик", "Цена за 1 тонну"))
        self.tableWidget_Product.horizontalHeader().sectionClicked.connect(self.on_header_clicked_product)
        self.tableWidget_Product.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.loaded_products = None
        self.search_btn_product.clicked.connect(lambda: self.loaddata_Product(search_string=self.lineEdit_search_product.text()))
        self.loaddata_Product()
        self.tableWidget_Product.doubleClicked.connect(self.open_edit_Product)
        self.lineEdit_search_product.setPlaceholderText("Поиск...")
        
        # Поставщики
        self.btn_add_suppliers.setDefault(True)
        self.btn_edit_suppliers.setDefault(True)
        self.btn_delete_suppliers.setDefault(True)

        self.btn_add_suppliers.clicked.connect(self.open_Add_suppliers)
        self.btn_edit_suppliers.clicked.connect(self.open_edit_suppliers)
        self.btn_delete_suppliers.clicked.connect(self.open_delete_suppliers)

        self.btn_add_suppliers.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_edit_suppliers.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_delete_suppliers.setFocusPolicy(QtCore.Qt.StrongFocus)

        self.tableWidget_suppliers.setColumnCount(2)
        self.tableWidget_suppliers.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_suppliers.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_suppliers.setHorizontalHeaderLabels(("Поставщик", "Контактный телефон"))
        self.tableWidget_suppliers.horizontalHeader().sectionClicked.connect(self.on_header_clicked_supliers)
        self.tableWidget_suppliers.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.loaded_suppliers = None
        self.search_btn_suppliers.clicked.connect(lambda: self.loaddata_suppliers(search_string=self.lineEdit_search_suppliers.text()))
        self.loaddata_suppliers()
        self.tableWidget_suppliers.doubleClicked.connect(self.open_edit_suppliers)
        self.lineEdit_search_suppliers.setPlaceholderText("Поиск...")

        # Сотрудники
        self.btn_add_staff.setDefault(True)
        self.btn_edit_staff.setDefault(True)
        self.btn_delete_staff.setDefault(True)

        self.btn_add_staff.clicked.connect(self.open_Add_staff)
        self.btn_edit_staff.clicked.connect(self.open_edit_staff)
        self.btn_delete_staff.clicked.connect(self.open_delete_staff)

        self.btn_add_staff.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_edit_staff.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_delete_staff.setFocusPolicy(QtCore.Qt.StrongFocus)

        self.tableWidget_staff.setColumnCount(6)
        self.tableWidget_staff.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_staff.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_staff.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_staff.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_staff.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_staff.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_staff.setHorizontalHeaderLabels(("Имя", "Фамилия", "Отчество", "Номер телефона", "Должность", "Дата найма"))
        self.tableWidget_staff.horizontalHeader().sectionClicked.connect(self.on_header_clicked_staff)
        self.tableWidget_staff.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.loaded_staff = None
        self.search_btn_staff.clicked.connect(lambda: self.loaddata_staff(search_string=self.lineEdit_search_staff.text()))
        self.loaddata_staff()
        self.tableWidget_staff.doubleClicked.connect(self.open_edit_staff)
        self.lineEdit_search_staff.setPlaceholderText("Поиск...")

        # Транспортные средства
        self.btn_add_venicle.setDefault(True)
        self.btn_edit_venicle.setDefault(True)
        self.btn_delete_venicle.setDefault(True)

        self.btn_add_venicle.clicked.connect(self.open_Add_venicle)
        self.btn_edit_venicle.clicked.connect(self.open_edit_venicle)
        self.btn_delete_venicle.clicked.connect(self.open_delete_venicle)

        self.btn_add_venicle.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_edit_venicle.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_delete_venicle.setFocusPolicy(QtCore.Qt.StrongFocus)

        self.tableWidget_venicle.setColumnCount(5)
        self.tableWidget_venicle.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_venicle.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_venicle.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_venicle.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_venicle.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_venicle.setHorizontalHeaderLabels(
            ("Водитель", "Модель машины", "Регистрационный номер", "Грузоподъемность в тоннах", "Последнее тех. обслуживание")
            )
        self.tableWidget_venicle.horizontalHeader().sectionClicked.connect(self.on_header_clicked_venicle)
        self.tableWidget_venicle.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.loaded_venicle = None
        self.search_btn_venicle.clicked.connect(lambda: self.loaddata_venicle(search_string=self.lineEdit_search_venicle.text()))
        self.loaddata_venicle()
        self.tableWidget_venicle.doubleClicked.connect(self.open_edit_venicle)
        self.lineEdit_search_venicle.setPlaceholderText("Поиск...")

        # Поставки
        self.btn_add_Delivery.setDefault(True)
        self.btn_edit_Delivery.setDefault(True)
        self.btn_delete_Delivery.setDefault(True)
        self.btn_delete_Delivery_2.setDefault(True)
        self.btn_otchet_Delivery.setDefault(True)

        self.btn_add_Delivery.clicked.connect(self.open_Add_delivery)
        self.btn_edit_Delivery.clicked.connect(self.open_edit_delivery)
        self.btn_delete_Delivery.clicked.connect(self.open_delete_delivery)
        self.btn_delete_Delivery_2.clicked.connect(self.open_delete_delivery_2)
        self.btn_otchet_Delivery.clicked.connect(self.open_otchet_Delivery)

        self.btn_add_Delivery.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_edit_Delivery.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_delete_Delivery.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_delete_Delivery_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_otchet_Delivery.setFocusPolicy(QtCore.Qt.StrongFocus)

        self.tableWidget_Delivery.setColumnCount(9)
        self.tableWidget_Delivery.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_Delivery.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_Delivery.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_Delivery.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_Delivery.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_Delivery.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_Delivery.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_Delivery.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_Delivery.horizontalHeader().setSectionResizeMode(8, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_Delivery.setHorizontalHeaderLabels(
            ("Номер поставки", "ТС", "Поставщик", "Товар", "Колличество т.", "Цена за 1 тонну", "Общая стоимость", "Дата заказа", "Дата поставки")
            )
        self.tableWidget_Delivery.horizontalHeader().sectionClicked.connect(self.on_header_clicked_delivery)
        self.tableWidget_Delivery.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.loaded_delivery = None
        self.search_btn_delivery.clicked.connect(lambda: self.loaddata_delivery(search_string=self.lineEdit_search_delivery.text()))
        self.loaddata_delivery()
        self.tableWidget_Delivery.doubleClicked.connect(self.open_edit_delivery)
        self.lineEdit_search_delivery.setPlaceholderText("Поиск...")

        # Клиенты
        self.btn_add_Clients.setDefault(True)
        self.btn_edit_Clients.setDefault(True)
        self.btn_delete_Clients.setDefault(True)

        self.btn_add_Clients.clicked.connect(self.open_Add_clients)
        self.btn_edit_Clients.clicked.connect(self.open_edit_clients)
        self.btn_delete_Clients.clicked.connect(self.open_delete_clients)

        self.btn_add_Clients.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_edit_Clients.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_delete_Clients.setFocusPolicy(QtCore.Qt.StrongFocus)

        self.tableWidget_Clients.setColumnCount(6)
        self.tableWidget_Clients.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_Clients.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_Clients.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_Clients.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_Clients.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_Clients.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_Clients.setHorizontalHeaderLabels(
            ("Имя", "Фамилия", "Отчество", "Номер телефона", "Адрес", "Город")
            )
        self.tableWidget_Clients.horizontalHeader().sectionClicked.connect(self.on_header_clicked_clients)
        self.tableWidget_Clients.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.loaded_client = None
        self.search_btn_clients.clicked.connect(lambda: self.loaddata_clients(search_string=self.lineEdit_search_clients.text()))
        self.loaddata_clients()
        self.tableWidget_Clients.doubleClicked.connect(self.open_edit_clients)
        self.lineEdit_search_clients.setPlaceholderText("Поиск...")

        # Заказы
        self.btn_add_orders.setDefault(True)
        self.btn_edit_order.setDefault(True)
        self.btn_delete_order.setDefault(True)
        self.btn_delete_order_2.setDefault(True)
        self.btn_otchet_order.setDefault(True)

        self.btn_add_orders.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_edit_order.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_delete_order.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_delete_order_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_otchet_order.setFocusPolicy(QtCore.Qt.StrongFocus)

        self.btn_add_orders.clicked.connect(self.open_Add_order)
        self.btn_edit_order.clicked.connect(self.open_edit_order)
        self.btn_delete_order.clicked.connect(self.open_delete_order)
        self.btn_delete_order_2.clicked.connect(self.open_delete_order_2)
        self.btn_otchet_order.clicked.connect(self.open_otchet_order)

        self.tableWidget_orders.setColumnCount(8)
        self.tableWidget_orders.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_orders.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_orders.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_orders.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_orders.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_orders.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_orders.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_orders.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_orders.setHorizontalHeaderLabels(
            ("Номер заказа", "ТС", "Клиенты", "Товар", "Количество т.", "Общая стоимость", "Дата заказа", "Дата поставки")
            )
        self.tableWidget_orders.horizontalHeader().sectionClicked.connect(self.on_header_clicked_order)
        self.tableWidget_orders.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.loaded_orders = None
        self.search_btn_order.clicked.connect(lambda: self.loaddata_order(search_string=self.lineEdit_search_order.text()))
        self.loaddata_order()
        self.tableWidget_orders.doubleClicked.connect(self.open_edit_order)
        self.lineEdit_search_order.setPlaceholderText("Поиск...")

    # товары --------------------------------------------------------------------------------------------------------------------------------------------
    def on_header_clicked_product(self, logicalIndex):
        self.sort_order = not self.sort_order
        self.loaddata_Product(logicalIndex=logicalIndex)

    def open_edit_Product(self):
        row = self.tableWidget_Product.currentRow()
        widget_item_name  = self.tableWidget_Product.item(row, 0)
        widget_item_supplier  = self.tableWidget_Product.item(row, 2)
        supplier = Suppliers.get(name=widget_item_supplier.text())
        if row >= 0 and row < self.tableWidget_Product.rowCount():
            product = Products.get(name=widget_item_name.text(), suppliers=supplier)
            self.edit_product = Addedit_Product(self, product)
            _translate = QtCore.QCoreApplication.translate
            self.edit_product.setWindowTitle(_translate("AddEditForm", "Изменить товар"))
            self.edit_product.edit_product(product)
            self.edit_product.show()

    def open_delete_Product(self):
        row = self.tableWidget_Product.currentRow()
        widget_item_name  = self.tableWidget_Product.item(row, 0)
        widget_item_supplier  = self.tableWidget_Product.item(row, 2)
        supplier = Suppliers.get(name=widget_item_supplier.text())
        if row >= 0 and row < self.tableWidget_Product.rowCount():
            product = Products.get(name=widget_item_name.text(), suppliers=supplier)
            self.edit_Product = Addedit_Product(self)
            self.edit_Product.delete_product(product)

    def loaddata_Product(self, logicalIndex=None, search_string=None):
        if search_string is not None:
            search_query = '%{}%'.format(search_string.replace(' ', '%'))
            self.loaded_products = Products.select().join(Suppliers).where(
                (Products.name.ilike(search_query)) |
                (Suppliers.name.ilike(search_query)) |
                (Products.quantity.cast('TEXT').ilike(search_query)) |
                (Products.price.cast('TEXT').ilike(search_query))
            )

            # Проверка на пустой результат
            if not self.loaded_products.exists():
                QtWidgets.QMessageBox.warning(self, "Ошибка поиска", "Ничего не найдено!")
                return

            self.lineEdit_search_product.setText("")
        else:
            # Загружаем все данные, если search_string не задан
            self.loaded_products = Products.select()

    # Сортировка загруженных данных
        if logicalIndex is not None:
            order = peewee.Asc if self.sort_order else peewee.Desc
            if logicalIndex == 0:
                self.loaded_products = self.loaded_products.order_by(order(Products.name))
            elif logicalIndex == 1:
                self.loaded_products = self.loaded_products.order_by(order(Products.quantity))
            elif logicalIndex == 2:
                self.loaded_products = self.loaded_products.order_by(order(Products.suppliers))
            elif logicalIndex == 3:
                self.loaded_products = self.loaded_products.order_by(order(Products.price))

        # Выводим отфильтрованные и отсортированные данные
        self.tableWidget_Product.setRowCount(len(self.loaded_products))
        tablerow = 0
        for row in self.loaded_products:
            self.tableWidget_Product.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row.name)))  # Преобразуем в строку
            self.tableWidget_Product.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row.quantity)))  # Преобразуем в строку
            self.tableWidget_Product.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row.suppliers.name)))  # Преобразуем в строку
            self.tableWidget_Product.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row.price)))  # Преобразуем в строку
            tablerow += 1
                
    # Поставщики -------------------------------------------------------------------------------------------------------------------------------------------
    
    
    def on_header_clicked_supliers(self, logicalIndex):
        self.sort_order = not self.sort_order
        self.loaddata_suppliers(logicalIndex=logicalIndex)
    
    def open_Add_suppliers(self):
        self.add_suppliers = Addedit_suppliers(self)
        self.add_suppliers.show()

    def open_edit_suppliers(self):
        row = self.tableWidget_suppliers.currentRow()
        widget_item  = self.tableWidget_suppliers.item(row, 0)
        if row >= 0 and row < self.tableWidget_suppliers.rowCount():
            suppliers = Suppliers.get(name=widget_item.text())
            self.edit_suppliers = Addedit_suppliers(self, suppliers)
            _translate = QtCore.QCoreApplication.translate
            self.edit_suppliers.setWindowTitle(_translate("AddEditForm", "Изменить поставщика"))
            self.edit_suppliers.edit_suppliers(suppliers)
            self.edit_suppliers.show()

    def open_delete_suppliers(self, suppliers):
        row = self.tableWidget_suppliers.currentRow()
        widget_item  = self.tableWidget_suppliers.item(row, 0)
        if row >= 0 and row < self.tableWidget_suppliers.rowCount():
            suppliers = Suppliers.get(name=widget_item.text())
            self.edit_suppliers = Addedit_suppliers(self)
            self.edit_suppliers.delete_suppliers(suppliers)

    def loaddata_suppliers(self, logicalIndex=None, search_string=None):
        if search_string is not None:
            search_query = '%{}%'.format(search_string.replace(' ', '%'))
            self.loaded_suppliers = Suppliers.select().where(
                (Suppliers.name.ilike(search_query)) |
                (Suppliers.сontactInfo.ilike(search_query))
            )
            if not self.loaded_suppliers.exists():
                QtWidgets.QMessageBox.warning(self, "Ошибка поиска", "Ничего не найдено!")
                return
            
            self.lineEdit_search_suppliers.setText("")
        else:
            self.loaded_suppliers = Suppliers.select()

        if logicalIndex is not None:
            order = peewee.Asc if self.sort_order else peewee.Desc
            if logicalIndex == 0:
                self.loaded_suppliers = self.loaded_suppliers.order_by(order(Suppliers.name))
            elif logicalIndex == 1:
                self.loaded_suppliers = self.loaded_suppliers.order_by(order(Suppliers.сontactInfo))

        self.tableWidget_suppliers.setRowCount(len(self.loaded_suppliers))
        tablerow = 0
        for row in self.loaded_suppliers:
            self.tableWidget_suppliers.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row.name)))  # Преобразуем в строку
            self.tableWidget_suppliers.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row.сontactInfo)))  # Преобразуем в строку
            tablerow += 1

    # staff --------------------------------------------------------------------------------------------------------------------------------------------
    def on_header_clicked_staff(self, logicalIndex):
        self.sort_order = not self.sort_order
        self.loaddata_staff(logicalIndex)
    
    def open_Add_staff(self):
        self.add_staff = Addedit_Staff(self)
        self.add_staff.show()
    
    def open_edit_staff(self):
        row = self.tableWidget_staff.currentRow()
        widget_item  = self.tableWidget_staff.item(row, 0)
        if row >= 0 and row < self.tableWidget_staff.rowCount():
            staff = Staff.get(firstName=widget_item.text())
            self.edit_staff = Addedit_Staff(self, staff)
            _translate = QtCore.QCoreApplication.translate
            self.edit_staff.setWindowTitle(_translate("AddEditForm", "Изменить сотрудника"))
            self.edit_staff.edit_Staff(staff)
            self.edit_staff.show()

    def open_delete_staff(self, staff):
        row = self.tableWidget_staff.currentRow()
        widget_item  = self.tableWidget_staff.item(row, 0)
        if row >= 0 and row < self.tableWidget_staff.rowCount():
            staff = Staff.get(firstName=widget_item.text())
            self.edit_staff = Addedit_Staff(self)
            self.edit_staff.delete_Staff(staff)

    def loaddata_staff(self, logicalIndex=None, search_string=None):
        if search_string is not None:
            search_query = '%{}%'.format(search_string.replace(' ', '%'))
            self.loaded_staff = Staff.select().where(
                (Staff.firstName.ilike(search_query)) |
                (Staff.lastName.ilike(search_query)) |
                (Staff.middleName.ilike(search_query)) |
                (Staff.сontactInfo.ilike(search_query)) |
                (Staff.position.ilike(search_query)) |
                (Staff.hireDate.cast('TEXT').ilike(search_query))
            )

            # Проверка на пустой результат
            if not self.loaded_staff.exists():
                QtWidgets.QMessageBox.warning(self, "Ошибка поиска", "Ничего не найдено!")
                return

            self.lineEdit_search_staff.setText("")
        else:
            # Загружаем все данные, если search_string не задан
            self.loaded_staff = Staff.select()

    # Сортировка загруженных данных
        if logicalIndex is not None:
            order = peewee.Asc if self.sort_order else peewee.Desc
            if logicalIndex == 0:
                self.loaded_staff = self.loaded_staff.order_by(order(Staff.firstName))
            elif logicalIndex == 1:
                self.loaded_staff = self.loaded_staff.order_by(order(Staff.lastName))
            elif logicalIndex == 2:
                self.loaded_staff = self.loaded_staff.order_by(order(Staff.middleName))
            elif logicalIndex == 3:
                self.loaded_staff = self.loaded_staff.order_by(order(Staff.сontactInfo))
            elif logicalIndex == 4:
                self.loaded_staff = self.loaded_staff.order_by(order(Staff.position))
            elif logicalIndex == 5:
                self.loaded_staff = self.loaded_staff.order_by(order(Staff.hireDate))

        # Выводим отфильтрованные и отсортированные данные
        self.tableWidget_staff.setRowCount(len(self.loaded_staff))
        tablerow = 0
        for row in self.loaded_staff:
            self.tableWidget_staff.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row.firstName)))  # Преобразуем в строку
            self.tableWidget_staff.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row.lastName)))  # Преобразуем в строку
            self.tableWidget_staff.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row.middleName)))  # Преобразуем в строку
            self.tableWidget_staff.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row.сontactInfo)))  # Преобразуем в строку
            self.tableWidget_staff.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row.position)))  # Преобразуем в строку
            self.tableWidget_staff.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row.hireDate)))  # Преобразуем в строку
            tablerow += 1

    # Транспортные средства-----------------------------------------------------------------------------------------------------------------------------
    def on_header_clicked_venicle(self, logicalIndex):
        self.sort_order = not self.sort_order
        self.loaddata_venicle(logicalIndex=logicalIndex)
    
    def open_Add_venicle(self):
        self.add_venicle = Addedit_venicle(self)
        self.add_venicle.show()

    def open_edit_venicle(self, venicle):
        row = self.tableWidget_venicle.currentRow()
        widget_item  = self.tableWidget_venicle.item(row, 2)
        if row >= 0 and row < self.tableWidget_venicle.rowCount():
            venicle = Venicle.get(registrationNumber=widget_item.text())
            self.edit_venicle = Addedit_venicle(self, venicle)
            _translate = QtCore.QCoreApplication.translate
            self.edit_venicle.setWindowTitle(_translate("AddEditForm", "Изменить транспортное средство"))
            self.edit_venicle.edit_venicle(venicle)
            self.edit_venicle.show()

    def open_delete_venicle(self, venicle):
        row = self.tableWidget_venicle.currentRow()
        widget_item  = self.tableWidget_venicle.item(row, 2)
        if row >= 0 and row < self.tableWidget_venicle.rowCount():
            venicle = Venicle.get(registrationNumber=widget_item.text())
            self.edit_venicle = Addedit_venicle(self)
            self.edit_venicle.delete_venicle(venicle)
    
    def loaddata_venicle(self, logicalIndex=None, search_string=None):
        if search_string is not None:
            search_query = '%{}%'.format(search_string.replace(' ', '%'))  # Замена пробелов на %

            self.loaded_venicle = Venicle.select().join(Staff).where(
                fn.CONCAT(Staff.lastName, ' ', Staff.firstName, ' ', Staff.middleName).ilike(search_query) |
                (Venicle.model.ilike(search_query)) |
                (Venicle.registrationNumber.ilike(search_query)) |
                (Venicle.capacity.cast('TEXT').ilike(search_query)) |
                (Venicle.maintenanceDate.cast('TEXT').ilike(search_query))
            )

            # Проверка на пустой результат
            if not self.loaded_venicle.exists():
                QtWidgets.QMessageBox.warning(self, "Ошибка поиска", "Ничего не найдено!")
                return

            self.lineEdit_search_venicle.setText("")
        else:
            # Загружаем все данные, если search_string не задан
            self.loaded_venicle = Venicle.select()

    # Сортировка загруженных данных
        if logicalIndex is not None:
            order = peewee.Asc if self.sort_order else peewee.Desc
            if logicalIndex == 0:
                self.loaded_venicle = self.loaded_venicle.order_by(order(Venicle.staff))
            elif logicalIndex == 1:
                self.loaded_venicle = self.loaded_venicle.order_by(order(Venicle.model))
            elif logicalIndex == 2:
                self.loaded_venicle = self.loaded_venicle.order_by(order(Venicle.registrationNumber))
            elif logicalIndex == 3:
                self.loaded_venicle = self.loaded_venicle.order_by(order(Venicle.capacity))
            elif logicalIndex == 4:
                self.loaded_venicle = self.loaded_venicle.order_by(order(Venicle.maintenanceDate))

        # Выводим отфильтрованные и отсортированные данные
        self.tableWidget_venicle.setRowCount(len(self.loaded_venicle))
        tablerow = 0
        for row in self.loaded_venicle:
            self.tableWidget_venicle.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(f"{row.staff.lastName} {row.staff.firstName} {row.staff.middleName}")))  # Преобразуем в строку
            self.tableWidget_venicle.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row.model)))  # Преобразуем в строку
            self.tableWidget_venicle.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row.registrationNumber)))  # Преобразуем в строку
            self.tableWidget_venicle.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row.capacity)))  # Преобразуем в строку
            self.tableWidget_venicle.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row.maintenanceDate)))  # Преобразуем в строку
            tablerow += 1
    
    # Поставки--------------------------------------------------------------------------------------------------------------------------------------------
    def on_header_clicked_delivery(self, logicalIndex):
        self.sort_order = not self.sort_order
        self.loaddata_delivery(logicalIndex=logicalIndex)

    def open_otchet_Delivery(self):
        row = self.tableWidget_Delivery.currentRow()
        widget_item  = self.tableWidget_Delivery.item(row, 0)
        if row >= 0 and row < self.tableWidget_Delivery.rowCount():
            delivery = Delivery.get(name=widget_item.text())
            self.edit_delivery = Addedit_delivery(self)
            self.edit_delivery.create_otchet(delivery)

    def open_Add_delivery(self):
        self.add_delivery = Addedit_delivery(self)
        self.add_delivery.show()

    def open_edit_delivery(self, delivery):
        row = self.tableWidget_Delivery.currentRow()
        widget_item  = self.tableWidget_Delivery.item(row, 0)
        if row >= 0 and row < self.tableWidget_Delivery.rowCount():
            delivery = Delivery.get(name=widget_item.text())
            self.edit_delivery = Addedit_delivery(self, delivery)
            _translate = QtCore.QCoreApplication.translate
            self.edit_delivery.setWindowTitle(_translate("AddEditForm", "Изменить поставку"))
            self.edit_delivery.edit_delivery(delivery)
            self.edit_delivery.show()

    def open_delete_delivery(self, delivery):
        row = self.tableWidget_Delivery.currentRow()
        widget_item  = self.tableWidget_Delivery.item(row, 0)
        if row >= 0 and row < self.tableWidget_Delivery.rowCount():
            delivery = Delivery.get(name=widget_item.text())
            self.edit_delivery = Addedit_delivery(self)
            self.edit_delivery.delete_delivery(delivery)
            
    def open_delete_delivery_2(self):
        row = self.tableWidget_Delivery.currentRow()
        widget_item  = self.tableWidget_Delivery.item(row, 0)
        if row >= 0 and row < self.tableWidget_Delivery.rowCount():
            delivery = Delivery.get(name=widget_item.text())
            self.edit_delivery = Addedit_delivery(self)
            self.edit_delivery.win_delivery(delivery)

    def loaddata_delivery(self, logicalIndex=None, search_string=None):
        if search_string is not None:
            search_query = '%{}%'.format(search_string.replace(' ', '%'))
            self.loaded_delivery = Delivery.select().join(Venicle).switch(Delivery).join(Suppliers).where(
                (Delivery.name.ilike(search_query)) |
                (Venicle.model.ilike(search_query)) |
                (Suppliers.name.ilike(search_query)) |
                (Delivery.product.ilike(search_query)) |
                (Delivery.startDate.cast('TEXT').ilike(search_query)) |
                (Delivery.quantity.cast('TEXT').ilike(search_query)) |
                (Delivery.deliveryDate.cast('TEXT').ilike(search_query)) |
                (Delivery.price.cast('TEXT').ilike(search_query)) |
                (Delivery.Total_price.cast('TEXT').ilike(search_query))
            )

            # Проверка на пустой результат
            if not self.loaded_delivery.exists():
                QtWidgets.QMessageBox.warning(self, "Ошибка поиска", "Ничего не найдено!")
                return

            self.lineEdit_search_delivery.setText("")
        else:
            # Загружаем все данные, если search_string не задан
            self.loaded_delivery = Delivery.select()

    # Сортировка загруженных данных
        if logicalIndex is not None:
            order = peewee.Asc if self.sort_order else peewee.Desc
            if logicalIndex == 0:
                self.loaded_delivery = self.loaded_delivery.order_by(order(Delivery.name))
            elif logicalIndex == 1:
                self.loaded_delivery = self.loaded_delivery.order_by(order(Delivery.venicle))
            elif logicalIndex == 2:
                self.loaded_delivery = self.loaded_delivery.order_by(order(Delivery.supplier))
            elif logicalIndex == 3:
                self.loaded_delivery = self.loaded_delivery.order_by(order(Delivery.product))
            elif logicalIndex == 4:
                self.loaded_delivery = self.loaded_delivery.order_by(order(Delivery.startDate))
            elif logicalIndex == 5:
                self.loaded_delivery = self.loaded_delivery.order_by(order(Delivery.deliveryDate))
            elif logicalIndex == 6:
                self.loaded_delivery = self.loaded_delivery.order_by(order(Delivery.quantity))
            elif logicalIndex == 7:
                self.loaded_delivery = self.loaded_delivery.order_by(order(Delivery.price))
            elif logicalIndex == 8:
                self.loaded_delivery = self.loaded_delivery.order_by(order(Delivery.Total_price))

        # Выводим отфильтрованные и отсортированные данные
        self.tableWidget_Delivery.setRowCount(len(self.loaded_delivery))
        tablerow = 0
        for row in self.loaded_delivery:
            self.tableWidget_Delivery.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row.name)))  # Преобразуем в строку
            self.tableWidget_Delivery.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row.venicle.model)))  # Преобразуем в строку
            self.tableWidget_Delivery.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row.supplier.name)))  # Преобразуем в строку
            self.tableWidget_Delivery.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row.product)))  # Преобразуем в строку
            self.tableWidget_Delivery.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row.quantity)))  # Преобразуем в строку
            self.tableWidget_Delivery.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row.price)))  # Преобразуем в строку
            self.tableWidget_Delivery.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row.Total_price)))  # Преобразуем в строку
            self.tableWidget_Delivery.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row.startDate)))  # Преобразуем в строку
            self.tableWidget_Delivery.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row.deliveryDate)))  # Преобразуем в строку
            tablerow += 1
    
    # Клиенты-------------------------------------------------------------------------------------------------------------------------------------------
    def on_header_clicked_clients(self, logicalIndex):
        self.sort_order = not self.sort_order
        self.loaddata_clients(logicalIndex=logicalIndex)
    
    def open_Add_clients(self):
        self.add_clients = Addedit_clients(self)
        self.add_clients.show()
    
    def open_edit_clients(self):
        row = self.tableWidget_Clients.currentRow()
        widget_item  = self.tableWidget_Clients.item(row, 3)
        if row >= 0 and row < self.tableWidget_Clients.rowCount():
            clients = Clients.get(contact=widget_item.text())
            self.edit_clients = Addedit_clients(self, clients)
            _translate = QtCore.QCoreApplication.translate
            self.edit_clients.setWindowTitle(_translate("AddEditForm", "Изменить клиента"))
            self.edit_clients.edit_clients(clients)
            self.edit_clients.show()

    def open_delete_clients(self, clients):
        row = self.tableWidget_Clients.currentRow()
        widget_item  = self.tableWidget_Clients.item(row, 3)
        if row >= 0 and row < self.tableWidget_Clients.rowCount():
            clients = Clients.get(contact=widget_item.text())
            self.edit_clients = Addedit_clients(self)
            self.edit_clients.delete_clients(clients)

    def loaddata_clients(self, logicalIndex=None, search_string=None):
        if search_string is not None:
            search_query = '%{}%'.format(search_string.replace(' ', '%'))
            self.loaded_client = Clients.select().where(
                (Clients.firstName.ilike(search_query)) |
                (Clients.lastName.ilike(search_query)) |
                (Clients.middleName.ilike(search_query)) |
                (Clients.contact.ilike(search_query)) |
                (Clients.Address.ilike(search_query)) |
                (Clients.City.ilike(search_query))
            )

            # Проверка на пустой результат
            if not self.loaded_client.exists():
                QtWidgets.QMessageBox.warning(self, "Ошибка поиска", "Ничего не найдено!")
                return

            self.lineEdit_search_clients.setText("")
        else:
            # Загружаем все данные, если search_string не задан
            self.loaded_client = Clients.select()

    # Сортировка загруженных данных
        if logicalIndex is not None:
            order = peewee.Asc if self.sort_order else peewee.Desc
            if logicalIndex == 0:
                self.loaded_client = self.loaded_client.order_by(order(Clients.firstName))
            elif logicalIndex == 1:
                self.loaded_client = self.loaded_client.order_by(order(Clients.lastName))
            elif logicalIndex == 2:
                self.loaded_client = self.loaded_client.order_by(order(Clients.middleName))
            elif logicalIndex == 3:
                self.loaded_client = self.loaded_client.order_by(order(Clients.contact))
            elif logicalIndex == 4:
                self.loaded_client = self.loaded_client.order_by(order(Clients.Address))
            elif logicalIndex == 5:
                self.loaded_client = self.loaded_client.order_by(order(Clients.City))

        # Выводим отфильтрованные и отсортированные данные
        self.tableWidget_Clients.setRowCount(len(self.loaded_client))
        tablerow = 0
        for row in self.loaded_client:
            self.tableWidget_Clients.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row.firstName)))  # Преобразуем в строку
            self.tableWidget_Clients.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row.lastName)))  # Преобразуем в строку
            self.tableWidget_Clients.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row.middleName)))  # Преобразуем в строку
            self.tableWidget_Clients.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row.contact)))  # Преобразуем в строку
            self.tableWidget_Clients.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row.Address)))  # Преобразуем в строку
            self.tableWidget_Clients.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row.City)))  # Преобразуем в строку
            tablerow += 1

    # Заказы-------------------------------------------------------------------------------------------------------------------------------------------
    def on_header_clicked_order(self, logicalIndex):
        self.sort_order = not self.sort_order
        self.loaddata_order(logicalIndex)
    
    def open_otchet_order(self):
        row = self.tableWidget_orders.currentRow()
        widget_item  = self.tableWidget_orders.item(row, 0)
        if row >= 0 and row < self.tableWidget_orders.rowCount():
            order = Orders.get(name=widget_item.text())
            self.edit_order = Addedit_orders(self)
            self.edit_order.create_otchet(order)
    
    def open_Add_order(self):
        self.add_order = Addedit_orders(self)
        self.add_order.show()
    
    def open_edit_order(self):
        row = self.tableWidget_orders.currentRow()
        widget_item  = self.tableWidget_orders.item(row, 0)
        if row >= 0 and row < self.tableWidget_orders.rowCount():
            order = Orders.get(name=widget_item.text())
            self.edit_order = Addedit_orders(self, order)
            _translate = QtCore.QCoreApplication.translate
            self.edit_order.setWindowTitle(_translate("AddEditForm", "Изменить заказ"))
            self.edit_order.edit_orders(order)
            self.edit_order.show()

    def open_delete_order(self, order):
        row = self.tableWidget_orders.currentRow()
        widget_item  = self.tableWidget_orders.item(row, 0)
        if row >= 0 and row < self.tableWidget_orders.rowCount():
            order = Orders.get(name=widget_item.text())
            self.edit_order = Addedit_orders(self)
            self.edit_order.delete_orders(order)

    def open_delete_order_2(self, order):
        row = self.tableWidget_orders.currentRow()
        widget_item  = self.tableWidget_orders.item(row, 0)
        if row >= 0 and row < self.tableWidget_orders.rowCount():
            order = Orders.get(name=widget_item.text())
            self.edit_order = Addedit_orders(self)
            self.edit_order.win_orders(order)

    def loaddata_order(self, logicalIndex=None, search_string=None):
        if search_string is not None:
            search_query = '%{}%'.format(search_string.replace(' ', '%'))
            self.loaded_orders = Orders.select().join(Clients).switch(Orders).join(Venicle).switch(Orders).join(Products).where(
                (Orders.name.ilike(search_query)) |
                fn.CONCAT(Clients.lastName, ' ', Clients.firstName, ' ', Clients.middleName).ilike(search_query) |
                (Products.name.ilike(search_query)) |
                (Orders.quanity.cast('TEXT').ilike(search_query)) |
                (Orders.Total_price.cast('TEXT').ilike(search_query)) |
                (Venicle.model.ilike(search_query)) |
                (Orders.startDate.cast('TEXT').ilike(search_query)) |
                (Orders.orderdate.cast('TEXT').ilike(search_query))
            )

            # Проверка на пустой результат
            if not self.loaded_orders.exists():
                QtWidgets.QMessageBox.warning(self, "Ошибка поиска", "Ничего не найдено!")
                return

            self.lineEdit_search_order.setText("")
        else:
            # Загружаем все данные, если search_string не задан
            self.loaded_orders = Orders.select()

    # Сортировка загруженных данных
        if logicalIndex is not None:
            order = peewee.Asc if self.sort_order else peewee.Desc
            if logicalIndex == 0:
                self.loaded_orders = self.loaded_orders.order_by(order(Orders.name))
            elif logicalIndex == 1:
                self.loaded_orders = self.loaded_orders.join(Venicle).switch(Orders).order_by(order(Venicle.model))
            elif logicalIndex == 2:
                self.loaded_orders = self.loaded_orders.join(Clients).switch(Orders).order_by(order(Clients.lastName))
            elif logicalIndex == 3:
                self.loaded_orders = self.loaded_orders.join(Products).switch(Orders).order_by(order(Products.name))
            elif logicalIndex == 4:
                self.loaded_orders = self.loaded_orders.order_by(order(Orders.quanity))
            elif logicalIndex == 5:
                self.loaded_orders = self.loaded_orders.order_by(order(Orders.Total_price))
            elif logicalIndex == 6:
                self.loaded_orders = self.loaded_orders.order_by(order(Orders.startDate))
            elif logicalIndex == 7:
                self.loaded_orders = self.loaded_orders.order_by(order(Orders.orderdate))

        # Выводим отфильтрованные и отсортированные данные
        self.tableWidget_orders.setRowCount(len(self.loaded_orders))
        tablerow = 0
        for row in self.loaded_orders:
            self.tableWidget_orders.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row.name)))  # Преобразуем в строку
            self.tableWidget_orders.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row.venicle.model)))  # Преобразуем в строку
            self.tableWidget_orders.setItem(tablerow, 2, QtWidgets.QTableWidgetItem((f"{row.clients.lastName} {row.clients.firstName} {row.clients.middleName}")))  # Преобразуем в строку
            self.tableWidget_orders.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(f"{row.product.name}|{row.product.suppliers.name}"))  # Преобразуем в строку
            self.tableWidget_orders.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row.quanity)))  # Преобразуем в строку
            self.tableWidget_orders.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row.Total_price)))  # Преобразуем в строку
            self.tableWidget_orders.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row.startDate)))  # Преобразуем в строку
            self.tableWidget_orders.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row.orderdate)))  # Преобразуем в строку
            tablerow += 1

        self.tableWidget_orders.resizeColumnsToContents()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec_())