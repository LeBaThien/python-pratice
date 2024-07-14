The Bridge Pattern là một mẫu thiết kế thuộc nhóm Structural Patterns, giúp tách biệt sự trừu tượng của một lớp khỏi sự
triển khai của nó để cả hai có thể thay đổi độc lập với nhau. Nó là một giải pháp để "tách giao diện ra khỏi việc triển
khai", giúp giảm sự phụ thuộc giữa hai phần và làm cho mã nguồn dễ bảo trì và mở rộng hơn

Tình huống giả định
Giả sử bạn có các hình dạng khác nhau (ví dụ: Circle và Square) và các màu sắc khác nhau (ví dụ: Red và Blue). Bạn muốn
kết hợp các hình dạng và màu sắc mà không cần tạo các lớp cho mọi kết hợp có thể.


```python
class Shape:
    def __init__(self, color):
        self.color = color

    def apply_color(self):
        raise NotImplementedError("You should implement this method!")

class Color:
    def fill(self):
        raise NotImplementedError("You should implement this method!")

class RedColor(Color):
    def fill(self):
        return "Coloring with Red"

class BlueColor(Color):
    def fill(self):
        return "Coloring with Blue"

class Circle(Shape):
    def apply_color(self):
        return f"Circle filled with {self.color.fill()}"

class Square(Shape):
    def apply_color(self):
        return f"Square filled with {self.color.fill()}"

class Circle(Shape):
    def apply_color(self):
        return f"Circle filled with {self.color.fill()}"

class Square(Shape):
    def apply_color(self):
        return f"Square filled with {self.color.fill()}"
if __name__ == '__main__':
    # Tạo đối tượng RedColor và BlueColor
    red = RedColor()
    blue = BlueColor()
    
    # Tạo đối tượng Circle và Square với màu sắc cụ thể
    red_circle = Circle(red)
    blue_circle = Circle(blue)
    red_square = Square(red)
    blue_square = Square(blue)
    
    # Sử dụng các đối tượng và in kết quả
    print(red_circle.apply_color())  # Output: Circle filled with Coloring with Red
    print(blue_circle.apply_color())  # Output: Circle filled with Coloring with Blue
    print(red_square.apply_color())  # Output: Square filled with Coloring with Red
    print(blue_square.apply_color())  # Output: Square filled with Coloring with Blue

```

Use cases:

Using the bridge pattern is a good idea when you want to share an implementation among multiple objects. Basically, instead of implementing several specialized classes, defining all that is required within each class, you can define the following special components:
• An abstraction that applies to all the classes
• A separate interface for the different objects involved
