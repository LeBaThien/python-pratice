Starvation (thiếu tài nguyên) trong Python xảy ra khi một thread hoặc process bị ngăn chặn không thể truy cập tài nguyên
cần thiết (như CPU, bộ nhớ, hoặc một khóa) trong một khoảng thời gian dài vì các thread hoặc process khác liên tục chiếm
tài nguyên đó. Điều này thường xảy ra trong các hệ thống đa luồng hoặc đa tiến trình khi có sự cạnh tranh không công
bằng hoặc không hiệu quả về tài nguyên.

Ví dụ về Starvation
Giả sử bạn có nhiều thread và một số thread có thể liên tục chiếm khóa (lock), ngăn cản các thread khác truy cập tài
nguyên chia sẻ.

```python
import threading
import time

lock = threading.Lock()


def task(name, sleep_time):
    while True:
        if lock.acquire(timeout=1):  # Thử lấy khóa trong 1 giây
            print(f'{name} acquired the lock')
            time.sleep(sleep_time)  # Giả lập việc sử dụng tài nguyên
            lock.release()
            print(f'{name} released the lock')
            break
        else:
            print(f'{name} could not acquire the lock')


if __name__ == '__main__':
    thread1 = threading.Thread(target=task, args=('Thread 1', 5))
    thread2 = threading.Thread(target=task, args=('Thread 2', 1))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
```

Trong ví dụ này, thread1 chiếm khóa trong 5 giây mỗi lần, trong khi thread2 chỉ chiếm khóa trong 1 giây mỗi lần. Điều
này có thể dẫn đến tình trạng thread2 bị đói tài nguyên nếu thread1 liên tục chiếm khóa.

Giải pháp để tránh Starvation

Sử dụng lock với thời gian chờ (timeout): Điều này cho phép thread khác có cơ hội lấy khóa nếu không thể có được nó ngay
lập tức.

Ưu tiên công bằng (fair scheduling): Một số cơ chế đồng bộ hóa như queue.Queue có tính năng FIFO (First In, First Out),
giúp đảm bảo rằng các thread được phục vụ theo thứ tự công bằng.

Công bằng trong phân phối tài nguyên: Đảm bảo rằng tài nguyên được phân phối công bằng giữa các thread hoặc process.

Dưới đây là một ví dụ cải thiện với hàng đợi (queue) để đảm bảo công bằng:

```python
import threading
import queue
import time

resource_queue = queue.Queue()

def task(name, sleep_time):
    while True:
        resource_queue.put(name)
        acquired = False
        while not acquired:
            if resource_queue.queue[0] == name and lock.acquire(timeout=1):
                acquired = True
                resource_queue.get()
                print(f'{name} acquired the lock')
                time.sleep(sleep_time)
                lock.release()
                print(f'{name} released the lock')
                break
            else:
                print(f'{name} could not acquire the lock, retrying...')
                time.sleep(1)

lock = threading.Lock()

thread1 = threading.Thread(target=task, args=('Thread 1', 5))
thread2 = threading.Thread(target=task, args=('Thread 2', 1))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

```