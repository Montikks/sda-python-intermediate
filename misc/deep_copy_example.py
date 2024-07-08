from copy import deepcopy
from dataclasses import dataclass


@dataclass()
class Rectangle:
    a: int = 0
    b: int = 0

    def circuit(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


p1 = Rectangle(3, 4)
lst = [1, p1, 3]
shallow_copy_lst = list(lst)
shallow_copy_lst = lst[:]
shallow_copy_lst = lst.copy()
deep_copy_lst = deepcopy(lst)
lst[1].a = 5  # we change the value of the side of the rectangle
print(lst, shallow_copy_lst, deep_copy_lst)
