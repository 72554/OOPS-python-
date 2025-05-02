
# 1. Car class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2022)


# 2. BankAccount with encapsulation
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


# 3. Inheritance: Animal, Dog, Cat
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"


# 4. Polymorphism with make_sound()
def make_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()
make_sound(dog)
make_sound(cat)


# 5. Abstraction with abstract class
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# 6. Employee class
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.emp_id}")


# 7. Method overriding with Vehicle and Bike
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Bike(Vehicle):
    def move(self):
        print("Bike is moving fast")


# 8. Class vs instance variables
class Student:
    count = 0  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable
        Student.count += 1


# 9. Calculator with static methods
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b if b != 0 else "Cannot divide by zero"


# 10. Alternate constructor with class method
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_string(cls, product_str):
        name, price = product_str.split("-")
        return cls(name, float(price))


# 11. __str__ vs __repr__
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"

    def __repr__(self):
        return f"Person('{self.name}')"

p = Person("Alice")
print(str(p))
print(repr(p))


# 12. Multiple inheritance
class Writer:
    def write(self):
        print("Writing...")

class Singer:
    def sing(self):
        print("Singing...")

class Personality(Writer, Singer):
    pass


# 13. Property decorator with Temperature
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, f):
        self._celsius = (f - 32) * 5/9


# 14. Singleton using metaclass
class SingletonMeta(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class Singleton(metaclass=SingletonMeta):
    pass


# 15. Using super()
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")


# 16. Order class with private attributes
class Order:
    def __init__(self, item, quantity):
        self.__item = item
        self.__quantity = quantity

    def get_item(self):
        return self.__item

    def set_item(self, item):
        self.__item = item

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity


# 17. Library class to manage books
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def list_books(self):
        for book in self.books:
            print(book)
