Data classes:

Data classes trong Python là một tính năng được giới thiệu từ phiên bản Python 3.7 thông qua module dataclasses. Data
classes cung cấp một cách đơn giản để tạo các lớp dữ liệu, tự động thêm các phương thức như __init__, __repr__, __eq__,
và nhiều phương thức khác, giúp giảm thiểu boilerplate code khi làm việc với các lớp chỉ dùng để lưu trữ dữ liệu.

Cách sử dụng data classes
Để sử dụng data classes, bạn cần import dataclass từ module dataclasses và sử dụng nó như một decorator trên lớp của
bạn.

```python
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


# Sử dụng lớp Person
p1 = Person(name="Alice", age=30)
p2 = Person(name="Bob", age=25)

print(p1)  # Output: Person(name='Alice', age=30)
print(p2)  # Output: Person(name='Bob', age=25)
print(p1 == p2)  # Output: False

```

Các tính năng bổ sung của data classes

1. Các giá trị mặc định:

```python
from dataclasses import dataclass,


@dataclass
class Person:
    name: str
    age: int = 0
```

2. Trường dữ liệu với giá trị mặc định bằng field:
   Sử dụng field để chỉ định các thuộc tính bổ sung cho trường dữ liệu.

```python
from dataclasses import dataclass, field


@dataclass
class Person:
    name: str
    age: int = 0
    hobbies: list = field(default_factory=list)
```

3. post_init xử lý:
Đôi khi bạn cần thực hiện thêm xử lý sau khi __init__ chạy xong, bạn có thể sử dụng phương thức __post_init__.

```python
from dataclasses import dataclass
@dataclass
class Person:
    name: str
    age: int

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")
```

4. Các tham số của dataclass:
Data classes có các tham số có thể thay đổi hành vi mặc định:

init: Nếu False, không tạo ra phương thức __init__.
repr: Nếu False, không tạo ra phương thức __repr__.
eq: Nếu False, không tạo ra phương thức __eq__.
order: Nếu True, thêm các phương thức so sánh (__lt__, __le__, __gt__, __ge__).
frozen: Nếu True, biến lớp thành immutable (không thể thay đổi sau khi khởi tạo).
unsafe_hash: Nếu True, thêm phương thức __hash__.

Example:
```python
from dataclasses import dataclass
@dataclass(frozen=True, order=True)
class Person:
    name: str
    age: int

```