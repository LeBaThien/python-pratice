import sys

sys.setrecursionlimit(1 << 30)


def crasher():
    return crasher()


if __name__ == '__main__':
    crasher()
