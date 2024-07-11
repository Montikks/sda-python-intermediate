import re


# Task 5
# Napis funkciu, ktora dostane na vstupe string a zisti, ci sa jedna o IPv4 adresu.
# IPv4 adresa je vo formate {cislo v rozmedzi 0-255}.{cislo v rozmedzi 0-255}.{cislo v rozmedzi 0-255}.{cislo v rozmedzi 0-255}


def is_ipv4_address(string):
    try:
        return all(int(num) <= 255 for num in (string.split('.')))
    except Exception:
        return False


if __name__ == "__main__":
    ip1 = '1.1.1.1'
    ip2 = '255.255.255.255'
    nonip1 = '256.255.255.255'
    nonip2 = 'asdf'
    print(is_ipv4_address(ip1))
    print(is_ipv4_address(ip2))
    print(is_ipv4_address(nonip1))
    print(is_ipv4_address(nonip2))
    print()
