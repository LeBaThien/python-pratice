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
