import re


def find_hashtags(text):
    return re.findall(r'#\w+', text)


if __name__ == "__main__":
    print(find_hashtags("# #a"))
    print(find_hashtags("Love the new features in #Python3.10! #coding #developer #regex"))
