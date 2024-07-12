Deadlock (khoá chết) trong Python xảy ra khi hai hoặc nhiều thread hoặc process chờ nhau giải phóng tài nguyên, dẫn đến
tình trạng chờ vô hạn và không có thread hoặc process nào có thể tiến hành. Deadlock là một vấn đề phổ biến trong lập
trình đa luồng và cần được xử lý cẩn thận để tránh ảnh hưởng đến hiệu suất và độ ổn định của ứng dụng.

Ví dụ về Deadlock
Giả sử chúng ta có hai thread và mỗi thread cố gắng lấy hai khóa theo thứ tự ngược lại:

```python
import threading

lock1 = threading.Lock()
lock2 = threading.Lock()


def thread1_task():
    with lock1:
        print('Thread 1 acquired lock1')
        with lock2:
            print('Thread 1 acquired lock2')
    print('Thread 1 finished')


def thread2_task():
    with lock2:
        print('Thread 2 acquired lock2')
        with lock1:
            print('Thread 2 acquired lock1')
    print('Thread 2 finished')


t1 = threading.Thread(target=thread1_task)
t2 = threading.Thread(target=thread2_task)

t1.start()
t2.start()

t1.join()
t2.join()

```

Trong ví dụ này, thread1 cố gắng lấy lock1 trước rồi mới đến lock2, trong khi thread2 cố gắng lấy lock2 trước rồi mới
đến lock1. Nếu thread1 đã lấy lock1 và thread2 đã lấy lock2, cả hai thread sẽ bị chờ vô hạn để lấy khóa còn lại, dẫn đến
deadlock.

Cách Phòng Tránh Deadlock
Tránh khóa chồng chéo (Nested Locks): Cố gắng tránh việc giữ nhiều khóa cùng lúc. Nếu không thể tránh, hãy đảm bảo rằng
tất cả các thread lấy khóa theo cùng một thứ tự.

Sử dụng timeout với khóa (Lock Timeout): Đặt thời gian chờ khi cố gắng lấy khóa để tránh chờ vô hạn.

Tránh khóa vòng (Circular Waiting): Đảm bảo rằng không có chu kỳ trong đồ thị chờ khóa.

```python
import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()


def thread1_task():
    while True:
        acquired_lock1 = lock1.acquire(timeout=1)
        if acquired_lock1:
            print('Thread 1 acquired lock1')
            time.sleep(0.5)  # Giả lập công việc đang thực hiện
            acquired_lock2 = lock2.acquire(timeout=1)
            if acquired_lock2:
                print('Thread 1 acquired lock2')
                # Thực hiện công việc
                lock2.release()
                print('Thread 1 released lock2')
            lock1.release()
            print('Thread 1 released lock1')
            if acquired_lock1 and acquired_lock2:
                break
            else:
                time.sleep(0.5)  # Giả lập công việc khác trước khi thử lại
        else:
            print('Thread 1 could not acquire lock1, retrying...')


def thread2_task():
    while True:
        acquired_lock2 = lock2.acquire(timeout=1)
        if acquired_lock2:
            print('Thread 2 acquired lock2')
            time.sleep(0.5)  # Giả lập công việc đang thực hiện
            acquired_lock1 = lock1.acquire(timeout=1)
            if acquired_lock1:
                print('Thread 2 acquired lock1')
                # Thực hiện công việc
                lock1.release()
                print('Thread 2 released lock1')
            lock2.release()
            print('Thread 2 released lock2')
            if acquired_lock2 and acquired_lock1:
                break
            else:
                time.sleep(0.5)  # Giả lập công việc khác trước khi thử lại
        else:
            print('Thread 2 could not acquire lock2, retrying...')


t1 = threading.Thread(target=thread1_task)
t2 = threading.Thread(target=thread2_task)

t1.start()
t2.start()

t1.join()
t2.join()

```

Trong ví dụ này, mỗi thread cố gắng lấy khóa với thời gian chờ. Nếu không thể lấy được khóa trong thời gian chờ, thread
sẽ thử lại sau một khoảng thời gian, tránh tình trạng chờ vô hạn và giúp ngăn chặn deadlock.

