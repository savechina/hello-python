import functools
import time


def basic_decorator_sample():
    """Demonstrates basic decorator patterns."""

    def log(func):
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__}")
            result = func(*args, **kwargs)
            print(f"{func.__name__} returned {result}")
            return result
        return wrapper

    @log
    def add(a, b):
        return a + b

    @log
    def greet(name):
        return f"Hello, {name}"

    print(add(3, 4))
    print(greet("Alice"))


def decorator_with_args_sample():
    """Demonstrates decorators with arguments."""

    def repeat(times):
        def decorator(func):
            def wrapper(*args, **kwargs):
                for i in range(times):
                    print(f"Iteration {i + 1}")
                    func(*args, **kwargs)
            return wrapper
        return decorator

    @repeat(3)
    def say_hello():
        print("  Hello!")

    say_hello()


def wraps_sample():
    """Demonstrates functools.wraps for preserving metadata."""

    def timer(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start
            print(f"{func.__name__} took {elapsed:.6f}s")
            return result
        return wrapper

    @timer
    def compute(n):
        total = sum(i * i for i in range(n))
        return total

    result = compute(100000)
    print(f"compute(100000) = {result}")
    print(f"Function name preserved: {compute.__name__}")
    print(f"Docstring preserved: {compute.__doc__}")


if __name__ == "__main__":
    basic_decorator_sample()
    print()
    decorator_with_args_sample()
    print()
    wraps_sample()
