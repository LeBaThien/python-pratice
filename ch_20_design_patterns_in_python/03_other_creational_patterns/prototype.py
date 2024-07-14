import copy


class Prototype:
    def __init__(self):
        self.value = None

    def clone(self):
        return copy.deepcopy(self)


if __name__ == '__main__':
    prototype = Prototype()
    prototype.value = 42

    clone = prototype.clone()
    print(clone.value)