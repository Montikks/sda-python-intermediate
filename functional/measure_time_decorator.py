import functools
import time

# Napis dekorator measure_time, ktory modifikuje funkciu tak,
# ze sa odstopuje cas, ktory trval pri vykonani funkcie a nasledne sa vypise.
# odporucam pouzit time.time()


def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'Function {wrapper.__name__} lasted {time.time() - start} seconds.')
        return result

    return wrapper


@measure_time
def bad_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


@measure_time
def good_sum(n):
    return n * (n + 1) // 2


if __name__ == "__main__":
    print(bad_sum(10**8))
    print(good_sum(10**8))
