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


print("_" * 60)

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

print("_" * 60)

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

print("_" * 60)

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

print("_" * 60)

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


print("_" * 60)

#  __bool__

class Point_obj():
    
    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y
        self.__alive = True
    
    def __bool__(self) -> bool:
        return self.__alive
    
    def delete(self) -> None:
        self.__alive = False
    
    
point = Point_obj(10, 10)
print(bool(point))
point.delete()
print(bool(point))

print("_" * 60)

# polimorphism

class square():
    
    def __init__(self, x:float) -> None:
        self.x = x
        
    def get_area(self) -> float:
        return self.x**2
        
        
class rectangle():
    
    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y
        
    def get_area(self) -> float:
        return self.x*self.y
    
sq = square(2)
rect = rectangle(2,5)

for figure in [sq, rect]:
    print(figure.get_area())
    
    
print("_" * 60)

# __getitem__ , __setitem__ , __delitem__

class Vector():
    
    def __init__(self, *args) -> None:
        self.values = list(args)
        
    def __str__(self) -> Any:
        return str(self.values)
    
    def __getitem__(self, index:int) -> Any:
        return self.values[index]
    
    def __setitem__(self, index:int, value:int) -> None:
        self.values[index] = value
    
    def __delitem__(self, index:int) -> None:
        del self.values[index]
    
vector_1 = Vector(1,2,3,235)
print(vector_1)
print(vector_1[2])
vector_1[2] = 24
print(vector_1)
del vector_1[2]
print(vector_1)


print("_" * 60)

# __iter__ , __next__

class Vector():
    
    def __init__(self, *args) -> None:
        self.values = list(args)
        self.index = -1
        
    def __getitem__(self, index:int) -> Any:
        return self.values[index]
    
    def __len__(self) -> int:
        return len(self.values)
        
    def __iter__(self):
        # for value in self.values:
        #     yield value
        
        return iter(self.values)
    
    def __next__(self):
        if self.index + 1 >= len(self.values):
            raise StopIteration
        self.index += 1
        return self.values[self.index]
        
        
        
vector_2 = Vector(1,23,33,35,456)

for i in vector_2:
    print(i)
    
print("_" * 10)

for i in range(len(vector_2)):
    print(next(vector_2))
    
    
print("_" * 60)

# inheritance from object

class human:
    pass

print(issubclass(human, object))
# print(dir(object))
# print(dir(human))
# print(dir(object) == dir(human))


print("_" * 60)

class human:
    
    def walk(self):
        print("Человек идёт")
        
    def sleep(self):
        print("Человек спит")
        
    def combination(self):
        self.walk()
        self.sleep()
        
        
class doctor(human):
    
    def walk(self):
        print("Доктор идёт")
        
        
        
hum = human()      
doc = doctor()   

doc.combination()  



print("_" * 60)

# delegating 

class human:
    
    def __init__(self, name:str, surname:str) -> None:
        self.name = name
        self.surname = surname
        
    def info(self):
        print(self.name, self.surname)
        if hasattr(self, "age"):
            print(self.age)
        
        
class doctor(human):
    
    def __init__(self, name: str, surname: str, age:int) -> None:
        self.age = age
        super().__init__(name, surname)
    
    def walk(self):
        print("Доктор идёт")
        super().walk()
             

hum = human("Petua", "Popov")
hum.info()
print("-" *10)

doc = doctor("Vasia", "Petrov", 23)   
doc.info()  


print("_" * 60)

# mro
class human:
    
    def __init__(self, name:str, surname:str) -> None:
        self.name = name
        self.surname = surname
        
    def info(self):
        print(self.name, self.surname)
        if hasattr(self, "age"):
            print(self.age)
        
        
class doctor(human):
    
    def __init__(self, name: str, surname: str, age:int) -> None:
        self.age = age
        super().__init__(name, surname)
    
    def walk(self):
        print("Доктор идёт")
        super().walk()
        
class SuperHuman(doctor, human):
    
    def __init__(self, name: str, surname: str, age: int) -> None:
        super().__init__(name, surname, age)
        
print(SuperHuman.__mro__)

print("_" * 60)

# Slots, property

class Rectangle:
    
    __slots__ = ("x", "y")

    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y
    
    @property
    def perimeter(self) -> float:
        return 2*(self.x + self.y)
    
    @property
    def area(self) -> float:
        return self.x*self.y
        
# Point.__slots__ = ("x", "y", "z")
print(Rectangle.__slots__)

print("_" * 60)
# My excetion

class MyError(Exception):
    
    def __init__(self, *args):
        self.message = " ".join(map(str, args))
    
    def __str__(self):
        return self.message

try:
    raise MyError("This is my custom error")
finally:
    print("Is error handled")