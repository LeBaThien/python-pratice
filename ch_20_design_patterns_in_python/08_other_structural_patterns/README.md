Flyweight Pattern là một mẫu thiết kế cấu trúc (structural design pattern) nhằm giảm bớt số lượng đối tượng được tạo ra
để tiết kiệm bộ nhớ và tăng hiệu suất. Mẫu thiết kế này sử dụng chia sẻ đối tượng để giảm tiêu thụ bộ nhớ khi có nhiều
đối tượng có trạng thái giống nhau.

Khi nào sử dụng Flyweight Pattern?
* Khi một ứng dụng cần tạo ra số lượng lớn đối tượng.
* Khi việc lưu trữ đối tượng gây tiêu tốn bộ nhớ đáng kể.
* Khi có thể chia sẻ trạng thái giữa các đối tượng thay vì tạo ra các đối tượng mới cho mỗi trường hợp.

Cách triển khai Flyweight Pattern trong Python
Giả sử chúng ta có một ứng dụng vẽ hình ảnh với nhiều vòng tròn. Chúng ta có thể sử dụng Flyweight Pattern để chia sẻ
các thuộc tính giống nhau của các vòng tròn.

```python
class Circle:
    def __init__(self, color):
        self.color = color
        self.x = 0
        self.y = 0
        self.radius = 0

    def draw(self):
        print(f"Circle: Draw() [Color : {self.color}, x : {self.x}, y : {self.y}, radius : {self.radius}]")

class ShapeFactory:
    _circle_map = {}

    @staticmethod
    def get_circle(color):
        circle = ShapeFactory._circle_map.get(color)

        if circle is None:
            circle = Circle(color)
            ShapeFactory._circle_map[color] = circle
            print(f"Creating circle of color : {color}")
        
        return circle

def main():
    colors = ["Red", "Green", "Blue", "White", "Black"]
    
    for i in range(20):
        circle = ShapeFactory.get_circle(colors[i % len(colors)])
        circle.x = i * 10
        circle.y = i * 20
        circle.radius = 100
        circle.draw()

if __name__ == "__main__":
    main()

```

1. Circle class: Đây là lớp đại diện cho các đối tượng có thể chia sẻ (flyweight). Nó có các thuộc tính như color, x, y, và radius.
2. ShapeFactory class: Đây là lớp quản lý các đối tượng flyweight. Nó có một từ điển _circle_map để lưu trữ và chia sẻ các đối tượng Circle dựa trên thuộc tính color.
3. get_circle method: Phương thức này kiểm tra xem đối tượng Circle với màu sắc đã tồn tại trong từ điển hay chưa. Nếu chưa, nó tạo ra một đối tượng mới và lưu vào từ điển, sau đó trả về đối tượng đó.
4. main function: Hàm này mô phỏng việc vẽ 20 vòng tròn với các màu sắc khác nhau. Nó sử dụng ShapeFactory để lấy các đối tượng Circle và thiết lập các thuộc tính như x, y, và radius trước khi gọi phương thức draw để vẽ chúng. 

Flyweight Pattern trong ví dụ này giúp tiết kiệm bộ nhớ bằng cách chia sẻ các đối tượng Circle có cùng màu sắc thay vì tạo ra một đối tượng mới mỗi khi cần vẽ một vòng tròn.