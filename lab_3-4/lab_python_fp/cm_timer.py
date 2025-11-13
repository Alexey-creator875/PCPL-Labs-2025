import time
from time import sleep

from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.execution_time = self.end_time - self.start_time
        print(f"time: {self.execution_time:.4f}")


@contextmanager
def cm_timer_2():
    start_time = time.time()
    yield
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"time: {execution_time:.4f}")


SLEEP_TIME = 5.5

if __name__ == "__main__":
    print("Test 1. cm_timer_1 (class-based)")
    with cm_timer_1():
        sleep(SLEEP_TIME)

    print("\nTest 2. cm_timer_2 (contextlib-based)")
    with cm_timer_2():
        sleep(SLEEP_TIME)
