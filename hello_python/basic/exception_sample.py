"""
Exception Handling Sample.
Demonstrates try/except/finally, multiple except clauses, and custom exceptions.
"""


def try_except_simple():
    """Basic try/except with integer parsing."""
    raw = "not a number"
    try:
        value = int(raw)
        print(f"value: {value}")
    except ValueError as e:
        print(f"ValueError: cannot convert '{raw}' to int — {e}")


def try_except_finally():
    """Demonstrates except, else, and finally clauses."""
    numbers = [10, 2, 0]
    for n in numbers:
        try:
            result = 100 / n
        except ZeroDivisionError:
            print(f"  n={n}: cannot divide by zero")
        else:
            print(f"  n={n}: 100 / {n} = {result}")
        finally:
            print(f"  n={n}: cleanup done")


class InvalidAgeError(Exception):
    """Custom exception for invalid age values."""

    def __init__(self, age, message="年龄必须在 0-150 之间"):
        self.age = age
        self.message = f"{message}，当前值: {age}"
        super().__init__(self.message)


def custom_exception_sample():
    """Demonstrates custom exception class and raise."""
    ages = [25, -3, 200]
    for age in ages:
        try:
            if age < 0 or age > 150:
                raise InvalidAgeError(age)
            print(f"  age {age}: valid")
        except InvalidAgeError as e:
            print(f"  age {age}: {e}")


if __name__ == "__main__":
    try_except_simple()
    print("---")
    try_except_finally()
    print("---")
    custom_exception_sample()
