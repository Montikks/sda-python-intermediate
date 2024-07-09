def foo(x):
    return x**2


print(dir(foo))
print(callable(foo))
print(callable(31))


# def callable(obj):
#     return hasattr(obj, '__call__')
#

class Foo:
    def __call__(self, x):
        return x ** 2


instance = Foo()
print(instance(3))
print(callable(instance))


def bar(x, y):
    return x(y)
    # evaluates as
    # return abs(-3)


print(bar(abs, -3))


# Lambda

def is_even(x):
    return x % 2 == 0


print(list(filter(lambda x: x % 2 == 0, [-1, -2, 0, 5, 0, 0, 2])))
print((lambda x: x)('hi'))

(lambda x: print(f'{x} Hii'))(3)


array = [(1, 4), (2, 0), (3, 3)]

print(sorted(array, key=lambda tup: (tup[1], tup[0])))

# Task 1
# Napiste 1 riadok, ktory najde najvacsiu hodnotu v zozname, kde najvacsia hodnota reprezentuje najdlhsi retazec
array = ['banana', 'apple', 'orange', 'pineapple']
print(max(array, key=len))


"""
Task 2
Napis funkciu, ktora na vstupe dostane cele cislo n >= 0 a vrati dictionary, kde klucmi budu cisla i a
    hodnotami funkcie, ktore beru najviac jeden argument vracaju konstantnu hodnotu 2**i, pre kazde i od 0 po n-1.
    Priklad:
        function_factory(2) ~> {0: <function object>, 1: <function object>}
    Hint:
        Pozor, aby kazda funkcia nerobila to iste!
"""


def function_factory(n):
    result_dict = {}
    for i in range(n):
        result_dict[i] = lambda x=i: 2 ** x
    return result_dict


for key, func in function_factory(10).items():
    print(key, func())
