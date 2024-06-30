from threading import Thread, Lock

thread_visit = 0
thread_visit_lock = Lock()


def visit_counter():
    global thread_visit
    for i in range(100_000):
        with thread_visit_lock:
            thread_visit += 1


if __name__ == '__main__':
    thread_count = 1000
    threads = [Thread(target=visit_counter) for _ in range(thread_count)]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f"{thread_count=}, {thread_visit=}")