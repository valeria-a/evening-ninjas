import math
from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, units: str, color: str):
        self._units = units
        self._color = color

    def get_color(self):
        return self._color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, height, width, units, color):

        super().__init__(units, color)

        self._height = height
        self._width = width

    def area(self):
        return self._width * self._height

    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius, units, color):

        super().__init__(units, color)

        self._radius = radius

    def area(self):
        return math.pi * (self._radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self._radius



if __name__ == '__main__':
    # s = Shape('mm', 'red')
    r = Rectangle(3, 4, 'm', 'blue')
    r.get_color()