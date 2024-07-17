import re


res = re.findall(r'\+420[0-9]{9}', '+420123456432 +420888666555 more text')
print(res)
res = re.finditer(r'\+420[0-9]{9}', '+420123456890 +420888666555 more text')
print(res)
for obj in res:
    print(obj)
    print(obj.group())
