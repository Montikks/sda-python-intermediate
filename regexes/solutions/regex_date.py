import re

# Task 3
# Napis funkciu, ktora dostane datum v stringu a skontroluje, ci je vo formate mm-dd-yyyy. Ak nie, vratime None.
# Ak ano, prevedieme ho na format dd/mm/yyyy a vratime ho ako vysledok.


def convert_date_format(string):
    if match := re.fullmatch(r'(\d{2})-(\d{2})-(\d{4})', string):
        return f'{match.group(2)}/{match.group(1)}/{match.group(3)}'


if __name__ == "__main__":
    print(convert_date_format('12-24-1990'))
