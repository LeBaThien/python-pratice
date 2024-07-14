class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()

    print(s1 is s2)
