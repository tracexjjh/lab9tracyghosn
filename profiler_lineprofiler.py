
from line_profiler import LineProfiler
import time


def slow_function():
    time.sleep(2)

    total = 0
    for i in range(10000):
        total += i ** 2

    return total


def optimized_fast_function():
    """Return the sum of squares from 0 through 99 without a loop."""
    n = 100
    return n * (n - 1) * (2 * n - 1) // 6


def memory_intensive_function():
    total = 0
    for i in range(10000000):
        total += i ** 2

    return total


def main():
    slow_function()
    optimized_fast_function()
    memory_intensive_function()


def profile_main():
    profiler = LineProfiler()

    profiler.add_function(slow_function)
    profiler.add_function(optimized_fast_function)
    profiler.add_function(memory_intensive_function)

    profiler.runcall(main)

    profiler.print_stats()


if __name__ == "__main__":
    profile_main()
