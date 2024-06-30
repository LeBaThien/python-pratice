Trong Python, single-dispatch functions là một tính năng của module functools, cho phép bạn tạo các hàm đa hình (
polymorphic) mà hành vi của chúng thay đổi tùy thuộc vào kiểu của đối số đầu tiên. Điều này có nghĩa là bạn có thể định
nghĩa nhiều phiên bản của cùng một hàm, mỗi phiên bản xử lý một kiểu đối số khác nhau.

# Cách sử dụng functools.singledispatch
1. Import singledispatch: Bạn cần import singledispatch từ module functools.
2. Tạo hàm cơ sở: Bạn bắt đầu bằng cách định nghĩa một hàm cơ sở và trang trí nó bằng @singledispatch. 
3. Đăng ký các hàm cụ thể: Sử dụng phương thức register của hàm cơ sở để đăng ký các hàm cụ thể cho từng kiểu đối số.

Ví dụ minh họa
Dưới đây là một ví dụ về cách sử dụng singledispatch:
````python
from functools import singledispatch

# Hàm cơ sở
@singledispatch
def process(data):
    raise NotImplementedError("Cannot process data of this type")

@process.register(int)
def _(data: int):
    print(f"Processing an integer: {data}")

@process.register(float)
def _(data: float):
    print(f"Processing a float: {data}")

@process.register(list)
def _(data: list):
    print(f"Processing a list: {data}")
````
# Sử dụng các hàm đã đăng ký
=> Minh hoạ cho tính đa hình.

process(42)       # Output: Processing an integer: 42
process(3.14)     # Output: Processing a float: 3.14
process([1, 2, 3]) # Output: Processing a list: [1, 2, 3]


# Lợi ích của Single-dispatch Functions
* Đa hình: Cho phép tạo ra các hàm có thể xử lý nhiều kiểu dữ liệu khác nhau mà không cần phải sử dụng cấu trúc điều kiện (if/elif/else) phức tạp.
* Mở rộng dễ dàng: Dễ dàng mở rộng thêm các kiểu dữ liệu mới mà không cần thay đổi hàm cơ bản.
* Tách biệt mã nguồn: Giúp tách biệt các logic xử lý cho từng kiểu dữ liệu vào các hàm riêng biệt, làm cho mã nguồn dễ đọc và bảo trì hơn.


# Khi nào sử dụng Single-dispatch Functions
* Khi bạn có một hàm cần xử lý logic khác nhau tùy thuộc vào kiểu của đối số đầu tiên.
* Khi bạn muốn tránh sử dụng nhiều cấu trúc điều kiện để kiểm tra kiểu của đối số và xử lý tương ứng.
* Khi bạn muốn dễ dàng mở rộng hàm để hỗ trợ thêm các kiểu dữ liệu mới trong tương lai mà không làm thay đổi logic hiện có.