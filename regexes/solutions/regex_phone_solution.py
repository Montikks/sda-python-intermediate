import re


# Task 1
# Napis funkciu, ktora dostane na vstupe text a vrati v zozname vsetky telefonne cisla
# s ceskou predvolbou +420, ktore sa v texte nachadzaju. Predpokladaj, ze za predvolbou
# moze nasledovat iba prave 9 cislic

def find_phone_numbers(string):
    for obj in re.finditer(r'(\+|00)420\d{9}\D', string):
        yield obj.group()[:-1]


if __name__ == "__main__":
    text = """
    +420123456432 +420888666555 more text 
    +421123456789
    +123456789000 bbb+420111222333
    +4209998887772 <- invalid
    00420123456789
    """
    print(list(find_phone_numbers(text)))
