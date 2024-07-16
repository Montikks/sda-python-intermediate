import timeit


def get_interval_sum(array, queries):
    result = []
    for start, end in queries:
        result.append(sum(array[start:end + 1]))
    return result


def get_interval_sum_effective(array, queries):
    prefix_sums = [0]
    for value in array:
        prefix_sums.append(prefix_sums[-1] + value)

    result = []
    for start, end in queries:
        result.append(prefix_sums[end + 1] - prefix_sums[start])
    return result


if __name__ == "__main__":
    array = [1, 5, 8, 3, 0, 0, 10]
    queries = [
        (0, 0),
        (0, 4),
        (2, 2),
        (3, 5),
        (6, 6),
        (0, 6),
    ]
    n = 1000
    array_long = list(range(n))
    queries_long = [(0, n - 1)] * n

    setup = "from __main__ import array, queries, array_long, queries_long, get_interval_sum, get_interval_sum_effective"
    print(
        "simple basic:",
        timeit.timeit('get_interval_sum(array, queries)', setup)
    )
    print(
        "simple effective:",
        timeit.timeit('get_interval_sum_effective(array, queries)', setup)
    )
    print(
        "simple basic:",
        timeit.timeit('get_interval_sum(array_long, queries_long)', setup, number=1000)
    )
    print(
        "simple effective:",
        timeit.timeit('get_interval_sum_effective(array_long, queries_long)', setup, number=1000)
    )
