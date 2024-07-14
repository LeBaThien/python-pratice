Ngoài Builder Pattern, còn có một số mẫu thiết kế (design patterns) thuộc nhóm creational patterns. Dưới đây là một số
mẫu thiết kế phổ biến trong nhóm này:

1. Singleton Pattern:
   Singleton Pattern đảm bảo rằng một lớp chỉ có duy nhất một instance và cung cấp một điểm truy cập toàn cục tới
   instance đó.

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


# Sử dụng Singleton
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # Output: True

```

Use cases:
 * Controlling concurrent access to a shared resource; for example, an object class that
manages the connection to a database.
 * A service or resource that is transversal in the sense that it can be accessed from 
different parts of the application or by different users and does its work, for example,
the class at the core of the logging system or utility



2. Prototype Pattern:
   Prototype Pattern cho phép sao chép đối tượng hiện có mà không cần phụ thuộc vào lớp của nó. Điều này rất hữu ích khi
   việc tạo ra một đối tượng là tốn kém (về thời gian hoặc tài nguyên).

```python
import copy


class Prototype:
    def __init__(self):
        self.value = None

    def clone(self):
        return copy.deepcopy(self)


# Sử dụng Prototype
prototype = Prototype()
prototype.value = 42

clone = prototype.clone()
print(clone.value)  # Output: 42

```
Use cases:


Khi nào nên sử dụng Prototype Pattern:

1. Khi việc tạo đối tượng là tốn kém:

Nếu việc tạo ra một đối tượng mới từ đầu tốn kém về tài nguyên hoặc thời gian (ví dụ, khởi tạo một đối tượng bao gồm
nhiều bước phức tạp, tải dữ liệu từ cơ sở dữ liệu, đọc từ tệp tin, v.v.), bạn có thể sử dụng Prototype Pattern để sao
chép đối tượng hiện có thay vì tạo mới từ đầu.

2. Khi có nhiều cấu hình cho đối tượng:

Khi bạn có một số cấu hình hoặc biến thể của một đối tượng và việc khởi tạo lại tất cả các biến thể này là phức tạp, bạn
có thể tạo một số prototype cơ bản và sau đó sao chép chúng khi cần thiết.
3. Khi bạn cần tách rời việc khởi tạo đối tượng khỏi logic sử dụng đối tượng:

Prototype Pattern cho phép tách rời logic khởi tạo đối tượng khỏi việc sử dụng nó, giúp mã của bạn dễ dàng mở rộng và
bảo trì hơn.

4. Khi các đối tượng phải có trạng thái ban đầu giống nhau:

Khi bạn cần nhiều đối tượng có trạng thái ban đầu giống nhau nhưng có thể thay đổi sau đó, bạn có thể sử dụng Prototype
Pattern để sao chép một prototype ban đầu.