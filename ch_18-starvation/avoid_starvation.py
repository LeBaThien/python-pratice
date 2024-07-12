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


if __name__ == '__main__':

    lock = threading.Lock()

    thread1 = threading.Thread(target=task, args=('Thread 1', 5))
    thread2 = threading.Thread(target=task, args=('Thread 2', 1))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
