def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def add_hello_print(func):
    def wrapper(*args, **kwargs):
        print('hello')
        return func(*args, **kwargs)

    return wrapper


new_add = add_hello_print(add)
new_sub = add_hello_print(sub)

print(new_add(1, 2))
print(new_sub(1, 2))

print(add_hello_print(len)('banana'))


@add_hello_print
def power2_x(x):
    return x ** 2


print(power2_x(10))
