import threading
import time


def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)


def print_letter():
    for letter in 'abcde':
        print(letter)
        time.sleep(1)


if __name__ == "__main__":
    t1 = threading.Thread(target=print_numbers())
    t2 = threading.Thread(target=print_letter())

    t1.start()
    t2.start()

    t1.join()
    t2.join()