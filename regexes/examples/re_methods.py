import re


string1 = "SDAcademy"
string2 = "SDAcademy and more"
string3 = "before SDAcademy after"
pattern = "SDAcademy"


# match hocikde
print(re.search(pattern, string3))
# match od zaciatku
print(re.match(pattern, string3))
# match pri celom retazci
print(re.fullmatch(pattern, string3))
