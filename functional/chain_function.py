import functools
# Napis funkciu compose, ktora zoberie lubovolny pocet funkcii a vrati funkciu, ktora
# vsetky tieto funkcie zavola tak, ze sa medzi nimi predavaju vysledky.
# Ide o takzvanu kompoziciu funkcii, kde pri volani compose(f, g, h...) sa nam vrati funkcia,
# ktora pocita f(g(h(...(x))))


def compose(*functions):
    def compose_two(f, g):
        return lambda *args, **kwargs: f(g(*args, **kwargs))

    return functools.reduce(compose_two, functions)


if __name__ == "__main__":
    sum_len = compose(sum, functools.partial(map, len))
    print(sum_len(["hello", "world", '!', '']))
