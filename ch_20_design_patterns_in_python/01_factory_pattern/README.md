Factory Pattern là một trong những mẫu (Design patterns) thuộc nhóm creational patterns.
Nó cung cấp một phương thức để tạo ra đối tượng mà không cần chỉ định chính xác lớp của dối tượng đó.
Điều này cho phép bạn tách rời quá trình khởi tạo đối tượng khỏi phần còn lại của mã, giúp mã
dễ bảo trì và mở rộng hơn

Các loại Factory Patterns

1. Simple Factory: Cung cấp một phương thức để tạo đối tượng
2. Factory Method: Định nghĩa một giao diện (interface) để tạo đối tượng, nhưng để các lớp con quuyết định lớp nào sẽ
   được khởi tạo.
3. Abstract Factory: Cung cấp một giao diện để tạo các họ (family) liên quan hoặc phụ thuộc
   của các dối tượng mà khồn chỉ định các lớp cụ thể của chúng.

Lợi ích của Factory Pattern:

1. Giảm sự phụ thuộc lẫn nhau: Gíup tách rời mã khởi tạo đối tượng khỏi mã sử dụng đối tượng./
2. Dễ mở rộng: Dễ dàng thêm các lớp mới mà không cần thay đổi mã hiện tại.
3. Đơn giản hoá mã: Tạo đối tượng phức tạp trở nên đơn giản hơn bằng cách uỷ thác công việc này
   cho lớp Factory.

Use cases:

For example, one factory method might be responsible for connecting you to different databases (MySQL and SQLite),
another factory method might be responsible for creating the geometrical object that you've requested (circle and
triangle), and so on.

The factory method is also useful when you want to decouple object creation from object usage. We are not coupled/bound
to a specific class when creating an object; we just provide partial information about what we want by calling a
function. This means that introducing changes to the function is easy and does not require any changes to be made to the
code that uses it.

