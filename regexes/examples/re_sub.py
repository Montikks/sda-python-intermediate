import re

text = "Hello world!!"
result = re.sub(r"world", "SDA", text)
print(result)
print()

text = "hello world and hello everyone!"
result = re.sub(r"hello", "hi", text)
result_n = re.subn(r"hello", "hi", text)
print(result)
print(result_n)
