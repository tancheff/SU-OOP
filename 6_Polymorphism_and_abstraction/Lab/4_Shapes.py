import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius: int):
        self.__radius = radius

    def calculate_area(self):
        a = math.pi*(self.__radius**2)
        return a

    def calculate_perimeter(self):
        p = 2*math.pi*self.__radius
        return p


class Rectangle(Shape):
    def __init__(self, height: int, width: int):
        self.__width = width
        self.__height = height

    def calculate_area(self):
        a = self.__height * self.__width
        return a

    def calculate_perimeter(self):
        p = 2 * (self.__width + self.__height)
        return p


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
