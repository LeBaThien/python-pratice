Builder Pattern là một trong những mẫu thiết kế thuộc nhóm creational patterns, cho phép tách rời việc xây dựng một đối
tượng phức tạp khỏi phần biểu diễn của nó để cùng một quá trình xây dựng có thể tạo ra các biểu diễn khác nhau. Nó
thường được sử dụng khi việc tạo ra một đối tượng phức tạp đòi hỏi nhiều bước.

Khi nào nên sử dụng Builder Pattern?
Khi bạn có một đối tượng phức tạp với nhiều thuộc tính và các thuộc tính đó có thể có giá trị mặc định hoặc có thể không
được thiết lập.
Khi việc khởi tạo đối tượng bao gồm nhiều bước phức tạp.
Khi bạn muốn tạo ra các biểu diễn khác nhau của cùng một đối tượng.

Ví dụ về Builder Pattern
Giả sử bạn có một lớp House với nhiều thuộc tính như windows, doors, roof, và garage. Sử dụng Builder Pattern để xây
dựng đối tượng House:

Định nghĩa lớp House

```python
class House:
    def __init__(self):
        self.windows = None
        self.doors = None
        self.roof = None
        self.garage = None

    def __str__(self):
        return f'House with {self.windows} windows, {self.doors} doors, {self.roof} roof, and {self.garage} garage.'

```

Định nghĩa lớp Builder

```python
class HouseBuilder:
    def __init__(self):
        self.house = House()

    def set_windows(self, number):
        self.house.windows = number
        return self

    def set_doors(self, number):
        self.house.doors = number
        return self

    def set_roof(self, roof_type):
        self.house.roof = roof_type
        return self

    def set_garage(self, garage_type):
        self.house.garage = garage_type
        return self

    def build(self):
        return self.house

```

Sử dụng Builder Pattern để tạo đối tượng House

```python
builder = HouseBuilder()
house = (builder
         .set_windows(4)
         .set_doors(2)
         .set_roof('shingle')
         .set_garage('attached')
         .build())

print(house)  # Output: House with 4 windows, 2 doors, shingle roof, and attached garage.
```

Ưu điểm của Builder Pattern

* Tách biệt việc xây dựng và biểu diễn đối tượng: Việc tạo đối tượng được tách biệt khỏi biểu diễn của nó, giúp dễ dàng
  thay đổi quá trình tạo ra đối tượng mà không ảnh hưởng đến mã sử dụng đối tượng.
* Dễ dàng mở rộng: Dễ dàng thêm các bước xây dựng mới mà không cần thay đổi mã hiện tại.
* Giảm thiểu số lượng tham số trong hàm tạo: Thay vì truyền nhiều tham số vào hàm tạo, bạn có thể thiết lập các thuộc
  tính
  từng bước.
  Builder Pattern là một công cụ mạnh mẽ khi bạn cần tạo ra các đối tượng phức tạp với nhiều thuộc tính hoặc các thuộc
  tính tùy chọn. Nó giúp mã của bạn dễ đọc, dễ bảo trì và dễ mở rộng hơn. Sử dụng Builder Pattern khi việc tạo ra một
  đối tượng phức tạp đòi hỏi nhiều bước hoặc khi bạn cần tạo ra nhiều biến thể của cùng một đối tượng.

Use cases:

We use the builder pattern when we know that an object must be created in multiple steps, and different representations
of the same construction are required. These requirements exist in many applications, such as page generators (for
example, the HTML page generator mentioned in this chapter), document converters, and user interface (UI)
form creators (j.mp/pipbuild).

