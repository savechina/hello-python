from contextlib import contextmanager, suppress
import time


def custom_cm_sample():
    """Demonstrates custom context manager with __enter__/__exit__."""

    class Timer:
        def __enter__(self):
            self.start = time.time()
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            elapsed = time.time() - self.start
            print(f"Elapsed: {elapsed:.6f}s")
            return False

    with Timer():
        total = sum(range(1000000))
    print(f"Sum: {total}")


def contextmanager_decorator_sample():
    """Demonstrates @contextmanager decorator."""

    @contextmanager
    def open_file(filename, mode):
        print(f"Opening {filename}")
        try:
            f = open(filename, mode)
            yield f
        finally:
            print(f"Closing {filename}")
            f.close()

    with open_file("/tmp/test_cm.txt", "w") as f:
        f.write("Hello, Context Manager!")

    with open_file("/tmp/test_cm.txt", "r") as f:
        content = f.read()
        print(f"Content: {content}")


def suppress_sample():
    """Demonstrates contextlib.suppress for ignoring exceptions."""

    nums = ["1", "two", "3"]
    for num in nums:
        with suppress(ValueError):
            print(int(num))


if __name__ == "__main__":
    custom_cm_sample()
    print()
    contextmanager_decorator_sample()
    print()
    suppress_sample()
