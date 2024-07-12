Race condition (điều kiện tranh chấp) trong Python xảy ra khi hai hoặc nhiều thread hoặc process cùng truy cập và thay
đổi một tài nguyên chung (như một biến) mà không có sự đồng bộ hóa, dẫn đến hành vi không mong muốn hoặc không thể đoán
trước. Điều này thường xảy ra trong các ứng dụng đa luồng hoặc đa tiến trình.

Ví dụ về Race Condition
Giả sử bạn có một biến toàn cục counter và bạn muốn tăng giá trị của nó trong nhiều thread:

```python
import threading

counter = 0


def increment():
    global counter
    for _ in range(100000):
        counter += 1


# Tạo hai thread
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# Bắt đầu cả hai thread
thread1.start()
thread2.start()

# Đợi cả hai thread hoàn thành
thread1.join()
thread2.join()

print(f'Final counter value: {counter}')

```

Kết quả in ra của đoạn mã này có thể không phải là 200000 như mong đợi vì counter += 1 không phải là một thao tác nguyên
tử (atomic operation). Nó thực sự bao gồm ba bước: đọc giá trị hiện tại của counter, tăng giá trị đó lên 1, và sau đó
ghi giá trị mới trở lại counter. Nếu hai thread thực hiện các bước này cùng một lúc, chúng có thể đọc cùng một giá trị
của counter và cả hai sẽ ghi lại cùng một giá trị, dẫn đến một lần tăng bị mất.

Cách khắc phục Race Condition
Để tránh race condition, bạn có thể sử dụng khóa (lock) để đồng bộ hóa quyền truy cập vào tài nguyên chia sẻ. Python
cung cấp lớp Lock trong module threading để giải quyết vấn đề này.

```python
import threading

counter = 0
lock = threading.Lock()


def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1


# Tạo hai thread
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# Bắt đầu cả hai thread
thread1.start()
thread2.start()

# Đợi cả hai thread hoàn thành
thread1.join()
thread2.join()

print(f'Final counter value: {counter}')

```

Trong đoạn mã này, chúng ta sử dụng một khóa lock để đảm bảo rằng chỉ có một thread có thể truy cập và thay đổi giá trị
của counter tại một thời điểm. Sử dụng câu lệnh with lock đảm bảo rằng khóa được tự động giải phóng sau khi đoạn mã
trong khối with kết thúc.

Một số khái niệm liên quan:

    Atomic operation: Một thao tác không thể bị gián đoạn giữa chừng bởi bất kỳ thread nào khác. Trong ví dụ trên,
    counter += 1 không phải là một thao tác nguyên tử.
    
    Lock: Một cơ chế để đồng bộ hóa quyền truy cập vào tài nguyên chia sẻ. Chỉ có một thread có thể giữ khóa tại một thời
    điểm.
    
    Critical section: Phần của mã mà truy cập tài nguyên chia sẻ, nơi chỉ một thread nên thực thi tại một thời điểm.
    
    Deadlock: Một tình huống trong đó hai hoặc nhiều thread chờ đợi lẫn nhau giữ khóa, dẫn đến tất cả các thread bị treo.
    
    GIL (Global Interpreter Lock): Một mutex đặc biệt trong CPython cho phép chỉ một thread thực thi mã Python tại một thời
    điểm. GIL không giải quyết vấn đề race condition và đôi khi còn gây thêm khó khăn trong việc tận dụng lợi thế của đa
    luồng.

