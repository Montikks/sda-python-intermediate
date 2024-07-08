from dataclasses import dataclass


@dataclass()
class Rectangle:
    a: int = 0
    b: int = 0

    def circuit(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


if __name__ == "__main__":
    rec = Rectangle()
    print(rec)
