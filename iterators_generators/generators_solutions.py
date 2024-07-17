import random


# Task 1
def even_numbers():
    num = 0
    while True:
        yield num
        num += 2


# Task 2
def my_range(start, stop, step=1):
    if step == 0:
        raise ValueError('Step cannot be 0')

    current = start
    if step >= 1:
        while current < stop:
            yield current
            current += step

    else:
        while current > stop:
            yield current
            current += step


# Task 3
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Task 4
def read_file(file_name):
    with open(file_name) as file:
        for line in file:
            yield line.strip()


# Task 5
def randgen(start, end):
    while True:
        yield random.randint(start, end)


# Task 6
def my_map(func, iterable):
    for obj in iterable:
        yield func(obj)


def my_filter(func, iterable):
    for obj in iterable:
        if func(obj):
            yield obj


if __name__ == "__main__":
    even_gen = even_numbers()
    for _ in range(5):
        print(next(even_gen))
    print()

    for number in my_range(5, 1, -1):
        print(number)
    print()

    fib_gen = fib()
    for _ in range(10):
        print(next(fib_gen))
    print()

    for line in read_file('text.txt'):
        print(line)
    print()

    rand_gen = randgen(1, 10)
    for _ in range(5):
        print(next(rand_gen), end=' ')
    print('\n')

    print(
        list(map(lambda x: -x, range(-10, 11)))
        == list(my_map(lambda x: -x, range(-10, 11)))
    )

    print(
        list(filter(lambda x: x % 2 == 0, range(-10, 11)))
        == list(my_filter(lambda x: x % 2 == 0, range(-10, 11)))
    )
