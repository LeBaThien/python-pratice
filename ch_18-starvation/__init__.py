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