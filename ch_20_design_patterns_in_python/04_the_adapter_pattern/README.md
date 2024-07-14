The Adapter Pattern là một mẫu thiết kế thuộc nhóm Structural Patterns. Nó cho phép các interface không tương thích làm
việc cùng nhau. Adapter Pattern hoạt động như một cầu nối giữa hai interface khác nhau, cho phép một lớp sử dụng
interface của một lớp khác.

Ứng dụng của Adapter Pattern
Adapter Pattern rất hữu ích trong các trường hợp sau:

1. Tích hợp hệ thống cũ và mới: Khi bạn cần tích hợp một hệ thống mới với một hệ thống cũ có các interface không tương
   thích.
2. Thay thế các thành phần trong hệ thống: Khi bạn muốn thay thế một thành phần trong hệ thống bằng một thành phần khác
   có
   interface khác biệt.
3. Sử dụng lại mã nguồn hiện có: Khi bạn muốn sử dụng lại các lớp hiện có mà không cần sửa đổi mã nguồn của chúng.
   Một ví dụ phức tạp hơn

Giả sử chúng ta có một hệ thống đăng nhập với hai loại người dùng: FacebookUser và GoogleUser, và chúng ta muốn một
Adapter để thống nhất cách đăng nhập.

```python
class FacebookUser:
    def login_facebook(self):
        return "User logged in with Facebook"


class GoogleUser:
    def login_google(self):
        return "User logged in with Google"


class LoginAdapter:
    def __init__(self, user, login_method):
        self.user = user
        self.login_method = login_method

    def login(self):
        return getattr(self.user, self.login_method)()


# Sử dụng Adapter
facebook_user = FacebookUser()
google_user = GoogleUser()

facebook_adapter = LoginAdapter(facebook_user, "login_facebook")
google_adapter = LoginAdapter(google_user, "login_google")

print(facebook_adapter.login())  # Output: User logged in with Facebook
print(google_adapter.login())  # Output: User logged in with Google

```

Trong ví dụ này, LoginAdapter có thể sử dụng bất kỳ phương thức đăng nhập nào từ các lớp khác nhau mà không cần thay đổi
các lớp ban đầu.


Use case:

Using an adapter to make thins work after they have been implemented is a good approach
because it does not require access to the source code of foreign interface.


