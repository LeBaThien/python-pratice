# Concurrency

Trong Python, concurrency (đồng thời) là khả năng xử lý nhiều tác vụ một cách độc lập hoặc đồng thời. Điều này có thể
đạt được bằng cách sử dụng nhiều kỹ thuật và thư viện khác nhau. Dưới đây là một số kỹ thuật chính để triển khai
concurrency trong Python:

**1. Multi-threading (Đa luồng)**
Multi-threading cho phép nhiều luồng (threads) chạy song song trong cùng một tiến trình (process). Tuy nhiên, Python có
Global Interpreter Lock (GIL), một cơ chế nhằm bảo vệ việc thực thi bytecode của Python, do đó các luồng thực sự không
thể chạy song song trong các tác vụ CPU-bound. Tuy nhiên, multi-threading vẫn hữu ích cho các tác vụ I/O-bound.

Example

```python
import threading
import time


def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)


def print_letter():
    for letter in 'abcde':
        print(letter)
        time.sleep(1)


if __name__ == "__main__":
    t1 = threading.Thread(target=print_numbers())
    t2 = threading.Thread(target=print_letter())

    t1.start()
    t2.start()

    t1.join()
    t2.join()
```

**2. Multi-processing (Đa tiến trình)**
Multi-processing khởi tạo nhiều tiến trình con (subprocesses) để thực hiện các tác vụ song song. Điều này hữu ích cho
các tác vụ CPU-bound vì mỗi tiến trình có GIL riêng của nó.

```python
import multiprocessing
import time


def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)


def print_letters():
    for letter in "abcde":
        print(letter)
        time.sleep(1)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=print_numbers)
    p2 = multiprocessing.Process(target=print_letters)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
```

**3. Asyncio**
Asyncio là một thư viện chuẩn trong Python để viết các chương trình đồng thời sử dụng cú pháp async/await. Nó hữu ích
cho các tác vụ I/O-bound, cho phép xử lý không đồng bộ mà không cần tạo nhiều luồng hoặc tiến trình.

```python

import asyncio


async def print_numbers():
    for i in range(5):
        print(i)
        await asyncio.sleep(1)


async def print_letters():
    for letter in 'abcde':
        print(letter)
        await asyncio.sleep(1)


async def main():
    await asyncio.gather(print_numbers(), print_letters())


asyncio.run(main())

```

**4. Concurrent Futures**
concurrent.futures là một mô-đun trong thư viện chuẩn của Python cung cấp một cách dễ dàng để chạy các tác vụ song song
bằng cách sử dụng luồng (ThreadPoolExecutor) hoặc tiến trình (ProcessPoolExecutor).

Ví dụ: Sử dụng concurrent.futures.ThreadPoolExecutor

```python
from concurrent.futures import ThreadPoolExecutor
import time


def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)


def print_letters():
    for letter in 'abcde':
        print(letter)
        time.sleep(1)


if __name__ == "__main__":
    with ThreadPoolExecutor() as executor:
        executor.submit(print_numbers)
        executor.submit(print_letters)

```

Ví dụ: Sử dụng concurrent.futures.ProcessPoolExecutor

```python
from concurrent.futures import ProcessPoolExecutor
import time


def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)


def print_letters():
    for letter in 'abcde':
        print(letter)
        time.sleep(1)


if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        executor.submit(print_numbers)
        executor.submit(print_letters)

```

**Khi nào nên sử dụng từng kỹ thuật?**
    **Multi-threading:** Tốt nhất cho các tác vụ I/O-bound, nơi mà thời gian chờ là chủ yếu.
    **Multi-processing:** Tốt nhất cho các tác vụ CPU-bound, nơi mà sử dụng nhiều lõi CPU có thể tăng hiệu suất.
    **Asyncio:** Tốt nhất cho các tác vụ I/O-bound với khả năng không đồng bộ, như xử lý mạng hoặc giao tiếp với các dịch vụ
    web.
    **Concurrent Futures:** Cung cấp một giao diện dễ sử dụng cho cả luồng và tiến trình, thích hợp cho các tác vụ đơn giản hoặc
    các kịch bản cần triển khai nhanh chóng.

# 1. What is multithreading

# 2. An example of a threaded application

# 3. Using one thread per item

# 4. Using a thread pool

# 5. Using two-wat queues

# 6. Dealing with errors in threads

# 7. Throttling

# 8. Multiprocessing

# 9. The built-in multiprocessing module

# 10. Using process pools

# 11. Using multiprocessing.dummy as the multithreading interface

# 12. Python async and await keywords

# 13. A practical example of asynchronous programming

# 14. Intergrating non-asynchronous code with async using futures


