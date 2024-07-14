class House:
    def __init__(self):
        self.windows = None
        self.doors = None
        self.roof = None
        self.garage = None

    def __str__(self):
        return f'house with {self.windows} windows and {self.doors} doors and {self.roof} roof'


class Apartment:
    def __init__(self):
        self.windows = None
        self.doors = None
        self.roof = None

    def __str__(self):
        return f'apartment with {self.windows} windows and {self.doors} doors and {self.roof} roof'


class HouseBuilder():
    def __init__(self):
        self.house = House()
        self.apartment = Apartment()

    def set_windows(self, number):
        self.house.windows = number
        return self

    def set_doors(self, number):
        self.house.doors = number
        return self

    def set_roof(self, number):
        self.house.roof = number
        return self

    def set_garage(self, number):
        self.house.garage = number
        return self

    def build(self, type):
        if type == 'house':
            return self.house
        elif type == 'apartment':
            return self.apartment
        else:
            return NotImplemented


if __name__ == '__main__':
    builder = HouseBuilder()
    house = (builder
             .set_windows(1)
             .set_doors(1)
             .set_roof('shingle')
             .set_garage('attached')
             .build('house'))

    builder1 = HouseBuilder()
    building = (builder1
                .set_windows(2)
                .set_doors(2)
                .set_roof('shingle2')
                .build('apartment'))

    print(house)
    print(building)
