
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        # opening and sharing of resources
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, type, value, traceback):
        # cleaning, release of resources
        self.file.close()


if __name__ == "__main__":
    with FileManager("test.txt", 'w') as f:
        f.write("Test")
