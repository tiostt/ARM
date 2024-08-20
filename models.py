from peewee import *

db = PostgresqlDatabase('sklad', user='sklad', password='qwerty', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Suppliers(BaseModel):

    name = CharField(max_length=150, unique=True)
    сontactInfo = CharField(max_length=150, unique=True)


class Products(BaseModel):

    name = CharField(max_length=150)
    quantity = FloatField()
    suppliers = ForeignKeyField(Suppliers)
    price = DecimalField(max_digits=7, decimal_places=2)


class Staff(BaseModel):

    firstName = CharField(max_length=150)
    lastName = CharField(max_length=150)
    middleName  = CharField(max_length=150)
    сontactInfo = CharField(max_length=150, unique=True)
    position = CharField(max_length=150)
    hireDate = DateField()


class Venicle(BaseModel):

    staff = ForeignKeyField(Staff)
    model = CharField(max_length=150)
    registrationNumber = CharField(max_length=150, unique=True)
    capacity = FloatField()
    maintenanceDate = DateField()


class Delivery(BaseModel):

    name = CharField(max_length=150, unique=True)
    quantity = FloatField()
    venicle = ForeignKeyField(Venicle)
    supplier = ForeignKeyField(Suppliers)
    product = CharField(max_length=150)
    startDate = DateField()
    deliveryDate = DateField()
    price = DecimalField(max_digits=10, decimal_places=2)
    Total_price = DecimalField(max_digits=10, decimal_places=2)


class Clients(BaseModel):

    firstName = CharField(max_length=150)
    lastName = CharField(max_length=150)
    middleName  = CharField(max_length=150)
    contact = CharField(max_length=150, unique=True)
    Address = CharField(max_length=150)
    City = CharField(max_length=150)


class Orders(BaseModel):

    name = CharField(max_length=150, unique=True)
    startDate = DateField()
    orderdate = DateField()
    quanity = FloatField()
    Total_price = DecimalField(max_digits=10, decimal_places=2)
    clients = ForeignKeyField(Clients)
    product = ForeignKeyField(Products)
    venicle = ForeignKeyField(Venicle)


if __name__ == "__main__":
    db.create_tables([Products, Suppliers, Delivery, Venicle, Staff, Clients, Orders])