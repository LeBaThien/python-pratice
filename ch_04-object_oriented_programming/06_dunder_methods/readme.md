Dunder methods, còn được gọi là "magic methods" hoặc "special methods", là các phương thức trong Python có tên bắt đầu
và kết thúc bằng hai dấu gạch dưới (double underscores), chẳng hạn như __init__, __str__, __len__, v.v. Những phương
thức này cho phép bạn định nghĩa cách các đối tượng của lớp tương tác với các toán tử và hàm tích hợp sẵn của Python.
Dưới đây là một số dunder methods phổ biến và cách sử dụng chúng.


# Một số dunder method phổ biến
1. __init__(self, ...):
- Được gọi khi một đối tượng mới của lớp được khởi tạo.
- Dùng để khởi tạo các thuộc tính của đối tượng.

```python
class MyClass:
    def __init__(self, value):
        self.value = value

```
2. __str__(self)

- Được gọi khi bạn sử dụng hàm str() hoặc print() trên một đối tượng.
- Dùng để trả về một chuỗi đại diện cho đối tượng.

```python
class MyClass:
    def __str__(self):
        return f"MyClass with value {self.value}"
```

3. __repr__(self):

- Được gọi khi bạn sử dụng hàm repr() hoặc khi đối tượng được in ra trong shell Python.
- Dùng để trả về một chuỗi đại diện chính xác cho đối tượng.
 
```python
class MyClass:
    def __repr__(self):
        return f"MyClass({self.value})"
```

4. __len__(self):

- Được gọi khi bạn sử dụng hàm len() trên đối tượng.
- Dùng để trả về độ dài của đối tượng.

```python
class MyClass:
    def __len__(self):
        return len(self.value)
```
5. __getitem__(self, key):

- Được gọi khi bạn truy cập một phần tử bằng cú pháp obj[key].
- Dùng để lấy giá trị của một phần tử với khóa key.

```python
class MyClass:
    def __getitem__(self, key):
        return self.value[key]
```

6. __setitem__(self, key, value):

- Được gọi khi bạn gán giá trị cho một phần tử bằng cú pháp obj[key] = value.
- Dùng để đặt giá trị cho phần tử với khóa key.

```python
class MyClass:
    def __setitem__(self, key, value):
        self.value[key] = value
```

7. __delitem__(self, key):

- Được gọi khi bạn xóa một phần tử bằng cú pháp del obj[key].
- Dùng để xóa phần tử với khóa key.

```python
class MyClass:
    def __delitem__(self, key):
        del self.value[key]
```

8. __iter__(self):

- Được gọi khi bạn sử dụng vòng lặp for trên đối tượng.
- Dùng để trả về một iterator cho đối tượng.

```python
class MyClass:
    def __iter__(self):
        return iter(self.value)
```

9.__next__(self):

- Được gọi để lấy phần tử tiếp theo từ iterator.
- Dùng trong iterator để trả về phần tử tiếp theo.

```python
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
```

10. __call__(self, ...):

- Được gọi khi bạn gọi một đối tượng như một hàm.
- Dùng để định nghĩa hành vi khi đối tượng được gọi như một hàm.

```python
class MyClass:
    def __call__(self, x):
        return x * 2
```