def my_generator(iterable, iterable2):
    yield from iterable
    yield from iterable2


if __name__ == "__main__":
    array1 = [1, 2, 3]
    array2 = [4, 5, 6, 7]
    for value in my_generator(array1, array2):
        print(value)
