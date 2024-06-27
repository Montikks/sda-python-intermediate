# Napis funkciu append_text(filename, text), ktora doplni text `text` do suboru s nazvom `filename`.
# Ak je subor readonly, osetri tento pripad tak, ze vypises na vystup "Cannot write to file <filename>"
# Pre windows userov, ako nastavit, aby bol subor readonly:
# https://adamtheautomator.com/how-to-make-a-file-read-only/

# Modul os: Importujeme modul os, který nám umožňuje pracovat s atributy souborů.
import os

def append_text(filename, text):
    """
       Funkce append_text přidá text na konec souboru s názvem filename.
       Pokud je soubor pouze pro čtení, vypíše zprávu, že není možné do souboru zapisovat.
       """
    if os.access(filename, os.W_OK):
        try:
            with open(filename, 'a') as file:
                file.write(text)
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print(f"Cannot write to file {filename}")

# Příklad použití
filename = 'example.txt'
append_text(filename, "Appended text\n")


# Pro testování jsem vytvořil soubor example.txt a zkusil ho nastavit jako pouze pro čtení. Na Windows můžete nastavit atributy souboru následovně:
#
# Klikněte pravým tlačítkem na soubor.
# Vyberte "Vlastnosti".
# Zaškrtněte "Jen pro čtení" a klikněte na "OK".

# Následně jem zkusil  spustit funkci append_text s tímto souborem a vidím že vypíše zprávu "Cannot write to file example.txt".
# A pokud se přepne na read only napíše se "Cannot write to file"