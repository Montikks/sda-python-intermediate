class MyContextManager:
    def __enter__(self):
        print('entering')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('closing with', exc_type, exc_val, exc_tb)
        return True


with MyContextManager() as obj:
    raise ValueError('just raised inside of with block')
    print(obj)
