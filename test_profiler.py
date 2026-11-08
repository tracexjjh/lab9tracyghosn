
import time
import memory_profiler
import unittest

from profiler import slow_function, fast_function, memory_intensive_function


class TestProfiler(unittest.TestCase):

    def time_function(self, func):
        """Times the execution of a function."""
        start_time = time.time()
        func()  # Execute the function
        end_time = time.time()
        return end_time - start_time

    def test_slow_function(self):
        """Test the slow_function for execution time."""
        duration = self.time_function(slow_function)
        print(f"slow_function executed in {duration:.2f} seconds.")
        self.assertGreater(
            duration, 2,
            "slow_function should take more than 2 seconds."
        )

    def test_fast_function(self):
        """Test the fast_function for execution time."""
        duration = self.time_function(fast_function)
        print(f"fast_function executed in {duration:.2f} seconds.")
        self.assertLess(
            duration, 1,
            "fast_function should take less than 1 second."
        )

    def test_memory_intensive_function(self):
        """Test the memory_intensive_function and monitor memory usage."""
        mem_usage_before = memory_profiler.memory_usage()

        duration = self.time_function(memory_intensive_function)
        mem_usage_after = memory_profiler.memory_usage()

        print(f"memory_intensive_function executed in {duration:.2f} seconds.")
        print(
            f"Memory usage before: {mem_usage_before[0]:.2f} MiB, "
            f"after: {mem_usage_after[0]:.2f} MiB."
        )

        self.assertLess(
            duration, 5,
            "memory_intensive_function should take less than 5 seconds."
        )
        self.assertGreater(
            mem_usage_after[0], mem_usage_before[0],
            "Memory usage should increase after running "
            "memory_intensive_function."
        )


def main():
    unittest.main()


if __name__ == "__main__":
    main()
