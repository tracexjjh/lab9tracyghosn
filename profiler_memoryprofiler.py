
from memory_profiler import profile
import time


@profile
def slow_function():
    time.sleep(2)

    total = 0
    for i in range(10000):
        total += i ** 2

    return total


@profile
def optimized_fast_function():
    """Return the sum of squares from 0 through 99 without a loop."""
    n = 100
    return n * (n - 1) * (2 * n - 1) // 6


@profile
def memory_intensive_function():
    total = 0
    for i in range(10000000):
        total += i ** 2

    return total


def main():
    slow_function()
    optimized_fast_function()
    memory_intensive_function()


if __name__ == "__main__":
    main()
