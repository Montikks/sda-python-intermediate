import threading

# Task 1
# Napis program, ktory vytvori 10 threadov a spusti ich.
# Funkcia priradena threadu bude vypisovat aktualny nazov threadu cez
# threading.current_thread().name


def print_thread_names():
    print(f"Current thread name: {threading.current_thread().name}")


threads = []
for i in range(10):
    thread = threading.Thread(target=print_thread_names)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
