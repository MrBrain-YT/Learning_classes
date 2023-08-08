""" monostate pattern """
from typing import Any


class Gun():
    shared_atr = {
        "Type":"M4A4",
        "count ammo":30
    }

    def __init__(self) -> None:
        self.__dict__ = Gun.shared_atr

a= Gun()
b= Gun()
b.Type = "hello"
print(a.__dict__)


print("_____________________________________________________________")

""" public privat and guarded metods """

class Account():

    def __init__(self, name, money, age) -> None:
        self.__age = age
        self.__name = name
        self.__money = money

    def show_data(self):
        print("All account data:")
        print(f"\t{self.__name}\n\t {self.__age}\n\t {self.__money}")

account1 = Account("Vasia", 100, 45)
account1.show_data()
# account1.__money | This class attribute privat
# print(account1._Account__name) | This variant get privat class attribute

print("_____________________________________________________________")

""" Property, set and get method """

class Account_2():

    def __init__(self, name, money, age) -> None:
        self.__age = age
        self.__name = name
        self.__money = money

    @property
    def money(self):
        return self.__money
    
    @money.setter
    def money(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("value not int or float")
        self.__money = value

    @money.deleter
    def money(self):
        del self.__money

    # balance = property(fget=get_money, fset=set_money, fdel=del_money)

account2 = Account_2("Fedor", 4000, 20)
account2.balance = 40
print(account2.balance)
# del account2.balance | This method delete money

print("_____________________________________________________________")

""" classmetod and static metod """

class Notebook():

    def __init__(self, model, year, ram) -> None:
        self.model = model
        self.year = year
        self.ram = ram
    
    @staticmethod
    def hello():
        print("Hello, user")

    @classmethod
    def class_hello(cls):
        print(f"Curent using class: {cls}")

""" staticmetod allows calling a method both from a class and from its instance """
Notebook("A520", 2020, 16).hello()
user = Notebook("A520", 2020, 16)
user.hello()

""" classmetod allows get class from instance """
Notebook("A520", 2020, 16).class_hello()
user = Notebook("A520", 2020, 16)
user.class_hello()

print("_____________________________________________________________")

""" __str__ , __repr__ , __len__ , __abs__ , __hash__ , __bool__ ,  and comparison methods """

class User():
    def __init__(self, name, money) -> None:
        self.name = name
        if isinstance(money, list):
            self.money = money
        else:
            raise TypeError("Money type is not a list")
        

    def __str__(self) -> str:
        # This string showing if you call print(instance name)
        return f"This username - {self.name}"
    
    def __repr__(self) -> str:
        # This string showing if you call instance
        return f"This object name - {self.name}"
    
    def __len__(self) -> int:
        # This metod sterted if you call len(instance name)
        return len(self.name)
    
    def __abs__(self) -> int:
        # This metod sterted if you call abs(instance name)
        return [abs(i) for i in self.money]
    
    def __add__(self, __value) -> float:
        # This metod sterted if you call (instance name + float)
        self.money[0] = float(self.money[0]) + float(__value)
        return self.money[0]
    
    def __mul__(self, __value) -> float:
        # This metod sterted if you call (instance name * float)
        self.money[0] = float(self.money[0]) * float(__value)
        return self.money[0]
    
    def __sub__(self, __value) -> float:
        # This metod sterted if you call (instance name - float)
        self.money[0] = float(self.money[0]) - float(__value)
        return self.money[0]
    
    def __truediv__(self, __value) -> float:
        # This metod sterted if you call (instance name / float)
        self.money[0] = float(self.money[0]) / float(__value)
        return self.money[0]
    
    """ comparison methods 
        != - __ne__
        == - __eq__
        <= - __le__
        >= - __ge__
        < - __lt__
        > - __gt__ """
    def __eq__(self, __value: object) -> bool:
        return self.name == __value
    
    def __hash__(self) -> int:
        return hash(self.name)
    
    def __bool__(self) -> bool:
        return bool(self.name)
    
    @classmethod
    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        return cls
    
user = User("Lavrenty", [-10000,500])
print(user)
print(len(user))
print(abs(user))
print(user + 7)
print(user * 7)
print(user - 7)
print(user / 7)
print(user == "vasia")
print(hash(user))
print(bool(user))
print(user())