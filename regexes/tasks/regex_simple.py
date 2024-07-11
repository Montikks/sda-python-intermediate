# Task 1
# Napis funkciu, ktora dostane na vstupe text a vrati v zozname vsetky telefonne cisla
# s ceskou predvolbou +420, ktore sa v texte nachadzaju. Predpokladaj, ze za predvolbou
# moze nasledovat iba prave 9 cislic


# Task 2
# Napis funkciu, ktora dostane na vstupe string a rozhodne, ci je to validna emailova adresa
# definujme si znaky basic = {vsetky pismena anglickej abecedy} | {vsetky cislice} | {.}
# emailova adresa je validna, pokial obsahuje aspon jeden znak z mnoziny `basic`, za ktorym nasleduje zavinac '@',
# dalej znovu aspon jeden znak z `basic - {.}` (bez bodky), bodka (.) a aspon 2 znaky anglickej abecedy.
# Disclaimer - toto nie je definicia realnej validnej emailovej adresy, iba velmi podobna definicia.
# Najlepsie je pouzivat v praxi validatory z uz naimplementovanych kniznic.

# Task 2.1
# Napis funkciu, ktora dostane text a vrati z neho zoznam vsetkych emailovych adries


# Task 3
# Napis funkciu, ktora dostane datum v stringu a skontroluje, ci je vo formate mm-dd-yyyy. Ak nie, vratime None.
# Ak ano, prevedieme ho na format dd/mm/yyyy a vratime ho ako vysledok.


# Task 4
# Napis funkciu, ktora vrati vsetky webove adresy zo stringu vo formate
# https://{hocico}<whitespace>
# alebo
# http://{hocico}<whitespace>
# Ak mas cas navyse, mozes si skusit napisat taky regex, ktory korektne validuje celu URL.


# Task 5
# Napis funkciu, ktora dostane na vstupe string a zisti, ci sa jedna o IPv4 adresu.
# IPv4 adresa je vo formate {cislo v rozmedzi 0-255}.{cislo v rozmedzi 0-255}.{cislo v rozmedzi 0-255}.{cislo v rozmedzi 0-255}
