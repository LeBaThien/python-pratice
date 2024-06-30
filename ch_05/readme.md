Trong Python, khái niệm "interfaces" không được hỗ trợ trực tiếp như trong một số ngôn ngữ lập trình khác như Java hay
C#. Tuy nhiên, Python vẫn có thể đạt được hành vi tương tự như interfaces thông qua việc sử dụng các lớp trừu tượng (
abstract base classes - ABCs) từ module abc. Các lớp trừu tượng cho phép bạn định nghĩa một tập hợp các phương thức mà
các lớp con bắt buộc phải triển khai.

# 1.Sử dụng một framework của bên thứ ba như zope.interface:

zope.interface là một thư viện của bên thứ ba cung cấp khái niệm interfaces cho Python. Nó cho phép bạn định nghĩa và
kiểm tra các interfaces trong ứng dụng Python của bạn.

# 2. Sử dụng Abstract Base Classes (ABCs):

Lớp trừu tượng (Abstract Base Classes - ABCs) trong module abc của Python cho phép bạn tạo ra các lớp trừu tượng với các
phương thức trừu tượng. Các lớp con kế thừa từ các lớp này phải triển khai các phương thức trừu tượng, giúp tạo ra các
giao diện nhất quán.

# 3. Sử dụng typing annotation, typing.Protocol, và static type analyzers:

typing annotation và typing.Protocol là các công cụ mạnh mẽ trong Python để định nghĩa và kiểm tra kiểu dữ liệu.
typing.Protocol cho phép bạn định nghĩa các giao diện mà không cần phải tạo ra các lớp trừu tượng.
Các công cụ phân tích tĩnh (static type analyzers) như mypy có thể kiểm tra tính nhất quán của các kiểu dữ liệu trong mã
nguồn của bạn, giúp bạn phát hiện lỗi liên quan đến kiểu dữ liệu trước khi chạy chương trình.

1. zope.interface:

```python
from zope.interface import Interface, implementer


class IAnimal(Interface):
    def make_sound():
        """Make a sound"""

    def move():
        """Move the animal"""

```

2. Abstract Base Classes (ABCs)
   ABCs cho phép bạn định nghĩa các lớp trừu tượng và các phương thức trừu tượng mà các lớp con phải triển khai. Điều
   này giúp tạo ra các giao diện rõ ràng cho các lớp con tuân theo.

Example

```python
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> str:
        pass

    @abstractmethod
    def move(self) -> str:
        pass

```

Kết hợp Function Annotations và ABCs

Example:

```python
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> str:
        """Return the sound the animal makes"""
        pass

    @abstractmethod
    def move(self) -> str:
        """Return the movement style of the animal"""
        pass


class Dog(Animal):
    def make_sound(self) -> str:
        return "Bark"

    def move(self) -> str:
        return "Run"


class Bird(Animal):
    def make_sound(self) -> str:
        return "Chirp"

    def move(self) -> str:
        return "Fly"

```

=> Kiểm tra tính hợp lệ của các lớp con
Bạn có thể sử dụng công cụ mypy để kiểm tra tính hợp lệ của các kiểu dữ liệu trong mã nguồn của bạn.

```shell
mypy your_file.py
```

3. Using @runtime_checkable
   Trong Python, decorator @runtime_checkable được sử dụng kết hợp với typing.Protocol để cho phép kiểm tra kiểu trong
   thời gian chạy. typing.Protocol là một tính năng trong Python để định nghĩa giao diện nhẹ (interface) mà các lớp có
   thể tuân theo, mà không cần phải kế thừa từ một lớp cơ sở cụ thể. @runtime_checkable mở rộng tính năng này, cho phép
   sử dụng hàm isinstance() để kiểm tra xem một đối tượng có tuân theo một Protocol hay không tại thời gian chạy.

**@runtime_checkable:** Decorator này được sử dụng để cho phép kiểm tra giao diện của một Protocol trong thời gian chạy
bằng
cách sử dụng isinstance().

**typing.Protocol:** Giao diện nhẹ để định nghĩa các phương thức mà các lớp phải triển khai. Nó không yêu cầu các lớp
phải
kế thừa trực tiếp từ Protocol.

**Lợi ích của @runtime_checkable:**

**- Kiểm tra linh hoạt**: Cho phép kiểm tra linh hoạt tại thời gian chạy, giúp phát hiện các đối tượng có tuân theo giao
diện đã định nghĩa hay không mà không cần ép buộc các lớp phải kế thừa từ một lớp cơ sở cụ thể.

**- Dễ dàng tích hợp**: Protocol có thể dễ dàng tích hợp vào các hệ thống hiện có mà không cần thay đổi cấu trúc kế thừa
của các lớp.

Example:

```python
from typing import Protocol, runtime_checkable


@runtime_checkable
class Animal(Protocol):
    def make_sound(self) -> str:
        ...


class Dog:
    def make_sound(self) -> str:
        return "Bark"


class Bird:
    def make_sound(self) -> str:
        return "Chirp"


class Fish:
    def swim(self) -> str:
        return "Swim"


dog = Dog()
bird = Bird()
fish = Fish()

print(isinstance(dog, Animal))  # Output: True
print(isinstance(bird, Animal))  # Output: True
print(isinstance(fish, Animal))  # Output: False
```

# 4. Inversion of control in application

**Inversion of Control (IoC)**: là một nguyên lý trong thiết kế phần mềm mà việc kiểm soát dòng thực thi của chương
trình
được "đảo ngược" từ luồng chính sang các thành phần con hoặc các đối tượng khác. IoC không phải là một mẫu thiết kế (
design pattern) cụ thể, mà là một đặc tính của các thiết kế phần mềm.

**IoC thông qua Đa hình (Polymorphism)**: đa hình cho phép các lớp con định nghĩa lại các phương thức của lớp cha, và
lớp cha có thể gọi các phương thức này mà không cần biết chi tiết cụ thể của lớp con.

```python
class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def make_sound(self):
        return "Bark"


class Cat(Animal):
    def make_sound(self):
        return "Meow"


def let_animal_make_sound(animal: Animal):
    print(animal.make_sound())


dog = Dog()
cat = Cat()

let_animal_make_sound(dog)  # Output: Bark
let_animal_make_sound(cat)  # Output: Meow
```

**IoC thông qua Truyền tham số (Argument passing)**: có thể truyền đối tượng vào hàm và hàm đó có thể gọi các phương
thức của đối tượng được truyền vào.

```python
class Logger:
    def log(self, message):
        print(f"LOG': {message}")


def process(data, logger: Logger):
    logger.log(f"Processing data: {data}")


logger = Logger()
process("my_data", logger)

```

**IoC thông qua Decorators**: Decorators trong Python cho phép bạn mở rộng hoặc thay đổi hành vi của hàm bằng cách đóng
gói nó trong một hàm khác.

```python
def my_decorator(func):
    def wrapper():
        print("something is happening before the function is called")
        func()
        print("Something is happening after the function is called")

    return wrapper


@my_decorator
def say_hello():
    print("Hello")


say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
```

**IoC thông qua Closures**: Closures là các hàm được định nghĩa bên trong một hàm khác và có thể truy cập các biến của
hàm bao quanh nó ngay cả sau khi hàm bao quanh kết thúc.

```python
def outer_function(message):
    def inner_function():
        print(f"Message: {message}")

    return inner_function


my_closure = outer_function("Hello, World!")
my_closure()  # Output: Message: Hello, World!
```

Ở đây, inner_function truy cập biến message của outer_function, ngay cả sau khi outer_function đã kết thúc. Đây là một
ví dụ về IoC thông qua closures, nơi mà inner_function kiểm soát việc sử dụng biến message.


