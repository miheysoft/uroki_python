import threading
from time import sleep


def print_number():
    for i in range(10):
        print(i)
        sleep(1)


def print_letter():
    for letter in ["a", "b", "c", "d", "e"]:
        print(letter)
        sleep(1)


if __name__ == "__main__":
    t1 = threading.Thread(target=print_number)
    t2 = threading.Thread(target=print_letter)
    t1.start()
    t2.start()
    print("Done1")
    t1.join()
    t2.join()

    print("Done2")
