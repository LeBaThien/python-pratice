class Coffee:
    def cost(self):
        return 10

    def description(self):
        return "simple coffee"


#  Create decorator class
class CoffeeDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()


class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

    def description(self):
        return self._coffee.description() + ", milk"


class SugarDecorator(CoffeeDecorator):

    def cost(self):
        return super().cost()

    def description(self):
        return super().description() + ", sugar"

    

if __name__ == '__main__':
    # Tạo đối tượng Coffee cơ bản
    simple_coffee = Coffee()
    print(f"Cost: ${simple_coffee.cost()}, Description: {simple_coffee.description()}")

    # Thêm Milk vào Coffee
    milk_coffee = MilkDecorator(simple_coffee)
    print(f"Cost: ${milk_coffee.cost()}, Description: {milk_coffee.description()}")

    # Thêm Sugar vào Milk Coffee
    milk_sugar_coffee = SugarDecorator(milk_coffee)
    print(f"Cost: ${milk_sugar_coffee.cost()}, Description: {milk_sugar_coffee.description()}")
