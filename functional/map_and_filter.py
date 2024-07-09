def my_map(func, iterable):
    result = []
    for obj in iterable:
        result.append(func(obj))
    return result


def my_filter(func, iterable):
    result = []
    for obj in iterable:
        if func(obj):
            result.append(obj)
    return result


def is_even(x):
    return x % 2 == 0


print(list(map(abs, [-1, -2, 0])))
print(list(filter(abs, [-1, -2, 0, 5, 0, 0, 2])))

print(list(my_map(abs, [-1, -2, 0])))
print(list(my_filter(is_even, [-1, -2, 0, 5, 2])))
