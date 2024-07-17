import threading
import time

# Task 2
# Napis program, ktory dostane na vstupe list cisel a vyuzije 4 thready na ich
# spocitanie.


class SumThread(threading.Thread):
    def __init__(self, target, args=(), kwargs=None):
        if kwargs is None:
            kwargs = {}
        self.target = target
        self.args = args
        self.kwargs = kwargs
        self.result = None
        super().__init__()

    def run(self):
        self.result = self.target(*self.args, **self.kwargs)

    def join(self, timeout=None):
        super().join(timeout)
        return self.result


def sum_from_to(array, i, j):
    return sum(array[i:j])


my_array = list(range(1, 100000001))
start = time.time()
threads = []
quarter = len(my_array) // 4
for i in range(0, len(my_array), quarter):
    threads.append(SumThread(target=sum_from_to, args=(my_array, i, i + quarter)))
    threads[-1].start()

result = 0
for thread in threads:
    result += thread.join()


print(result)
print(time.time() - start)

start = time.time()
result = sum(my_array)
print(result)
print(time.time() - start)
