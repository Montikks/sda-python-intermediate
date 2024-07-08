import abc
import math
# Napis triedu Shape, ktora bude mat 2 abstraktne metody `perimeter()` a `area()`.
# Dalej napis triedy Rectangle, Circle a Triangle (jednostranny), ktore dedia zo Shape.
# Kazda bude tieto 2 metody prepisovat a pocitat obvod, respektive obsah podla toho, co je to za utvar.
# Init bude rozdielny podla toho, ake udaje o geometrickom tvare nas budu zaujimat.
# HINT: Inspiruj sa ucebnymi materialmi


class Shape(abc.ABC):
    @abc.abstractmethod
    def perimeter(self):
        pass

    @abc.abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * self.r * math.pi

    def area(self):
        return math.pi * self.r ** 2


class Triangle(Shape):
    def __init__(self, size):
        self.size = size

    def perimeter(self):
        return self.size * 3

    def area(self):
        return self.size * math.sqrt(3) / 4


if __name__ == "__main__":
    rectangle = Rectangle(10, 4)
    print(rectangle.perimeter(), rectangle.area())

    circle = Circle(1 / math.sqrt(math.pi))
    print(circle.perimeter(), circle.area())

    triangle = Triangle(5)
    print(triangle.perimeter(), triangle.area())
