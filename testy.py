def my_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result


def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
print(my_map(double, numbers))



def my_filter(func, iterable):
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result


def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
print(my_filter(is_even, numbers))