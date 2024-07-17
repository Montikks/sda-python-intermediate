a = [1, 2, 3, 4]
for item in a:
    print(item)

a = "Alice has a cat"
for item in a:
    print(item)

a = {'name': "Adam", 'surname': "Smith"}
for item in a.items():
    print(item)


# for i in list(range(10)):
#     print(i)


from itertools import count

for i in count():
    print(i)
    if i > 100:
        break

print(list(count()))
