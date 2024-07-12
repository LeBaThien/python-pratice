import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1_task():
    while True:
        acquired_lock1 = lock1.acquire(timeout=1)
        if acquired_lock1:
            print('Thread 1 acquired lock1')
            time.sleep(0.5) # Gỉa lập công việc đang thực hiện.
            acquired_lock2 = lock2.acquire(timeout=1)
            if acquired_lock2:
                print('Thread 1 acquired lock2')
                lock2.release()
                print('Thread 1 released lock2')
            lock1.release()
            print('Thread 1 released lock1')
            if acquired_lock1 and acquired_lock2:
                break
            else:
                time.sleep(0.5) # Giả lập công việc khác trước khi thử lại
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