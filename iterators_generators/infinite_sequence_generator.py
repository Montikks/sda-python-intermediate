def my_count():
    num = 0
    while True:
        yield num
        num += 1


for i in my_count():
    print(i)
    if i > 5:
        break
