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


if __name__ == "__main__":
    even_gen = even_numbers()
    for _ in range(5):
        print(next(even_gen))

    for number in my_range(5, 1, -1):
        print(number)
