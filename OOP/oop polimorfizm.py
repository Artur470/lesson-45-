

#####            Полиморфизм     ########


#
#
# def addv (a : int , b: int):
#     return a + b
#
# def add (a : str , b : str):
#     return f" {a} {b} "
#
# def add (a: float , b: float):
#     return round (a + b, 3)
#
# if __name__ == '__main__':
#     add ("1.5","1.7")






from abc import ABC , abstractmethod
import math


#  Базовый класс Shape (Фигура)

class Shape(ABC):
    @ abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length , width):
        self.length  = length
        self.width = width

    def calculate_area(self):
        return self.length  * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math

# rectangle = Rectangle(4,5)
# circle = Circle(3)
# print("Площадь прямоугольника:", rectangle.calculate_area())
# print("Площадь круга:", circle.calculate_area())
#



"""Тапшырма создать класс Vehicle (транспортное средство)
метод transport ылдыйкы кичине класс ачып 
Car (машина)
Bicycle (велосипед)
Boat (лодка)
пример едит по дороге (автомобиль)
       едит по велосипедной дорожке (велосипед)
       плывет по воде (лодка) деп чыксын 
       
       
"""



from abc import ABC , abstractmethod
class Vehicle(ABC):
    def transport(self):
       pass

class Car(Vehicle):
    def transport(self):
        return "едит на дороге"

class Bicycle(Vehicle):
    def transport(self):
        return "едит по велосипедной дорожке"

class Boat(Vehicle):
    def transport(self):
        return "плывет по воде "



car = Car()
bicycle = Bicycle()
boat = Boat()

print("Действие автомобиля ", car.transport())
print("Действие  велосипеда ", bicycle.transport())
print("Действие лодки ", boat.transport())
