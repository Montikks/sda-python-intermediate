import functools
# Napis funkciu compose, ktora zoberie lubovolny pocet funkcii a vrati funkciu, ktora
# vsetky tieto funkcie zavola tak, ze sa medzi nimi predavaju vysledky.
# Ide o takzvanu kompoziciu funkcii, kde pri volani compose(f, g, h...) sa nam vrati funkcia,
# ktora pocita f(g(h(...(x))))
