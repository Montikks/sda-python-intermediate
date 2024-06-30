from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        # Použití Heronova vzorce pro výpočet obsahu
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

def main():
    shapes = []
    while True:
        shape_type = input("Zadejte typ tvaru (rectangle, circle, triangle) nebo 'exit' pro ukončení: ").lower()
        if shape_type == 'exit':
            break
        elif shape_type == 'rectangle':
            width = float(input("Zadejte šířku obdélníku: "))
            height = float(input("Zadejte výšku obdélníku: "))
            shapes.append(Rectangle(width, height))
        elif shape_type == 'circle':
            radius = float(input("Zadejte poloměr kruhu: "))
            shapes.append(Circle(radius))
        elif shape_type == 'triangle':
            a = float(input("Zadejte délku strany a trojúhelníku: "))
            b = float(input("Zadejte délku strany b trojúhelníku: "))
            c = float(input("Zadejte délku strany c trojúhelníku: "))
            shapes.append(Triangle(a, b, c))
        else:
            print("Neplatný typ tvaru. Zkuste to znovu.")

    for shape in shapes:
        print(f"{shape.__class__.__name__} perimeter: {shape.perimeter()}")
        print(f"{shape.__class__.__name__} area: {shape.area()}")

if __name__ == "__main__":
    main()
