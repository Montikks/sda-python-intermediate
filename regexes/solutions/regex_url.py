import re


def find_urls_easy(text):
    return re.findall(r"https?://[A-Za-z0-9-]+\.[A-Za-z]{2,6}\s", text)


def find_urls(text):
    return [match.group() for match in re.finditer(r"(https?://)?(([A-Za-z0-9-]+\.)+[A-Za-z]{2,6})", text)]


if __name__ == "__main__":
    print(find_urls_easy("http://example.com nonsense asdf $@ https: https://asdf.jkl.cz test.com test"))
    print(find_urls("http://example.com nonsense asdf $@ https: https://asdf.jkl.cz test.com test"))
