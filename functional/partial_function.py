from functools import wraps

# Napis funkciu partial, ktora berie funkciu a vracia novu funkciu, ktora sa da ciastocne zavolat.
# Ciastocne zavolana funkcia vrati funkciu, ktora sa sprava tak, ze ma zafixovane predane parametre a
# pri dalsom volani berie uz iba zvysne (nie nutne berie dalsie parametre)


def my_partial(func, *args, **kwargs):
    if not callable(func):
        raise TypeError(f'First parameter of `my_partial` must be callable. {func} is not.')

    @wraps(func)
    def wrapper(*new_args, **new_kwargs):
        return func(*args, *new_args, **kwargs, **new_kwargs)

    return wrapper


def int_sum(a, b):
    return a + b


def default_sum(iter_, init=None):
    """
    :param iter_: Iterable whose elements are summed
    :param init: Initial value of the sum. If None (default), first element of iter_ becomes init.
                 If init not specified and iter_ is empty, returns None
    :return: Sum of elements
    """
    result = init
    for elem in iter_:
        if result is None:
            result = elem
            continue
        result += elem

    return result


if __name__ == '__main__':
    plus_ten = my_partial(int_sum, 10)
    print(plus_ten(5))  # 15
    premade_sum = my_partial(int_sum, 10, 20)
    print(premade_sum())  # 30

    string_sum = my_partial(default_sum, init='')
    print(string_sum(['a', 'b', 'c']))  # 'abc'

    try:
        my_partial(1, 2)
    except TypeError:
        print('ok')
    else:
        print("Should've returned TypeError")

    # Too many arguments before
    try:
        my_partial(int_sum, 10, 20, 30)()
    except Exception as e:
        print('ok:', e)
    else:
        print("Should've returned an Exception")

    # Too many arguments after
    try:
        my_partial(int_sum, 10, 20)('oops')
    except Exception as e:
        print('ok:', e)
    else:
        print("Should've returned an Exception")
