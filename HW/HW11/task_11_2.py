# Создать пять классов описывающие реальные объекты.
# Каждый класс должен содержать минимум три приватных атрибута,
# конструктор, геттеры и сеттеры для каждого атрибута, два метода.

from random import randint


# 1 класс - лампа
class Lamp:
    def __init__(self, model, color, light_brightness=0):
        self.model = model
        self.__color = color
        self.__light_brightness = light_brightness

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def light_brightness(self):
        return self.__light_brightness

    @light_brightness.setter
    def light_brightness(self, light_brightness=1):
        self.__light_brightness += light_brightness

    def lamp_off(self):
        self.__light_brightness = 0
        print('Lamp is off')

    def is_lamp_on(self):
        if self.__light_brightness > 0:
            return True
        else:
            return False


# 2 класс - книга
class Book:
    def __init__(self, author, length, pages):
        self.author = author
        self.__length = length
        self.__pages = pages

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        self.__author = author

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages):
        self.__pages = pages

    def check_length(self, bag_length):
        if self.__length > bag_length:
            print('This book will not fit in this bag')
        else:
            print("It's OK")

    def random_page(self):
        print(f"The book is opened at page {randint(1,500)}")


# 3 класс - банк
class Bank:
    def __init__(self, name, address, phone, usd_byn_rate, account):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__usd_byn_rate = usd_byn_rate
        self.__account = account

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def usd_byn_rate(self):
        return self.__usd_byn_rate

    @usd_byn_rate.setter
    def usd_byn_rate(self, usd_byn_rate):
        self.__usd_byn_rate = usd_byn_rate

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, account):
        self.__account = account

    def exchange(self, usd):
        byn = usd * self.__usd_byn_rate
        return byn

    def pay_bill(self, bill):
        account = self.__account - bill
        return f'After paying the bill you have {account}$ on your bank account'

    def transfer(self, money):
        account = self.__account + money
        return f'Now you have {account}$ on your bank account'