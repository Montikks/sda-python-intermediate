import re

# Task 2
# Napis funkciu, ktora dostane na vstupe string a rozhodne, ci je to validna emailova adresa
# definujme si znaky basic = {vsetky pismena anglickej abecedy} | {vsetky cislice} | {.}
# emailova adresa je validna, pokial obsahuje aspon jeden znak z mnoziny `basic`, za ktorym nasleduje zavinac '@',
# dalej znovu aspon jeden znak z `basic - {.}` (bez bodky), bodka (.) a aspon 2 znaky anglickej abecedy.
# Disclaimer - toto nie je definicia realnej validnej emailovej adresy, iba velmi podobna definicia.
# Najlepsie je pouzivat v praxi validatory z uz naimplementovanych kniznic.

# Task 2.1
# Napis funkciu, ktora dostane text a vrati z neho zoznam vsetkych emailovych adries

email_pattern = r'[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}'


def is_valid_email(string):
    return bool(re.fullmatch(email_pattern, string))


def extract_all_emails(text):
    return re.findall(email_pattern, text)


if __name__ == "__main__":
    text = "Please contact us at support@example.com or sales.info@example.com for further information."
    email1 = 'email@mail.com'
    email2 = 'F.i@asdf.co'
    email3 = '.@gmail.com'
    nonemail1 = '@a.co'
    nonemail2 = 'ab@.com'
    nonemail3 = '@gmail.com'

    print(is_valid_email(email1))
    print(is_valid_email(email2))
    print(is_valid_email(email3))
    print(is_valid_email(nonemail1))
    print(is_valid_email(nonemail2))
    print(is_valid_email(nonemail3))

    print(extract_all_emails(text))
