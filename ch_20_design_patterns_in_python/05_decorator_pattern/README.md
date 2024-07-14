Decorator Pattern là một mẫu thiết kế thuộc nhóm Structural Patterns, cho phép bạn thêm hành vi hoặc trách nhiệm vào đối
tượng một cách linh hoạt mà không cần thay đổi mã nguồn của lớp đó. Trong Python, Decorator Pattern có thể được triển
khai dễ dàng bằng cách sử dụng các decorators.

Dưới đây là một ví dụ về cách triển khai Decorator Pattern trong Python.

Tình huống giả định
Giả sử bạn có một lớp Coffee và bạn muốn thêm các thành phần bổ sung như sữa, đường mà không thay đổi lớp Coffee

```python
class Coffee:
    def cost(self):
        return 5

    def description(self):
        return "Simple coffee"

```

Tạo lớp Decorator
Bây giờ chúng ta sẽ tạo một lớp Decorator cơ bản và các Decorator cụ thể để thêm các thành phần bổ sung.

```python

class Coffee:
    def cost(self):
        return 5

    def description(self):
        return "Simple coffee"


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
        return self._coffee.cost() + 0.5

    def description(self):
        return self._coffee.description() + ", sugar"


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

```

Decorator Pattern trong Python với Function Decorators
Python cung cấp một cách mạnh mẽ và dễ sử dụng để triển khai Decorator Pattern bằng cách sử dụng decorators cho hàm.
Dưới đây là một ví dụ đơn giản:

```python
def make_bold(fn):
    def wrapped():
        return f"<b>{fn()}</b>"
    return wrapped

def make_italic(fn):
    def wrapped():
        return f"<i>{fn()}</i>"
    return wrapped

@make_bold
@make_italic
def hello():
    return "Hello, World!"

print(hello())

```
Use cases:

Used for implementing cross-cutting converns
* Data validation
* Caching
* Logging
* Monitoring
* Debugging
* Business rules
* Encryption


