# Napis context manager (class), vdaka ktoremu sa vsetky vyhodene vynimky vo with bloku
# budu iba vypisovat, ale uz sa dalej nebudu vyhadzovat


class SupressExceptionMixin:
    exception_to_suppress = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # No exception occurred
        if exc_type is None and exc_val is None and exc_tb is None:
            return True

        if self.exception_to_suppress is None or isinstance(
            exc_val, self.exception_to_suppress
        ):
            print(
                f"Suppressed <{exc_type.__name__}> at {self.__class__.__name__}: {exc_val}"
            )
            return True
        return False


class Foo(SupressExceptionMixin):
    exception_to_suppress = ValueError


if __name__ == "__main__":
    with Foo() as foo:
        print("I am here")
        raise IndexError('hello')
        print('not here')

    print('...and here')
