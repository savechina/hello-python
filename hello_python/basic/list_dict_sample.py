"""
List & Dict Sample.
Demonstrates list comprehensions, dict operations, set, and tuple unpacking.
"""


def list_comprehension_sample():
    """Demonstrates list comprehensions (simple, with conditions, nested)."""
    # Simple comprehension
    squares = [x * x for x in range(5)]
    print(f"squares of 0-4: {squares}")

    # With condition
    evens = [x for x in range(10) if x % 2 == 0]
    print(f"evens 0-9: {evens}")

    # Nested comprehension
    matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
    print(f"3x3 multiplication matrix: {matrix}")


def dict_operations_sample():
    """Demonstrates dict creation, access, and common methods."""
    user = {"name": "Alice", "age": 30, "city": "Shanghai"}

    # Access with .get() — safe default
    print(f"name: {user.get('name')}")
    print(f"missing key (None): {user.get('phone')}")

    # Iterate with .items()
    for key, value in user.items():
        print(f"  {key}: {value}")

    # Update / merge
    user.update({"email": "alice@example.com"})
    print(f"after update: {user}")


def set_tuple_sample():
    """Demonstrates set operations and tuple unpacking."""
    # Set operations
    a = {1, 2, 3}
    b = {3, 4, 5}
    print(f"union: {a | b}")
    print(f"intersection: {a & b}")
    print(f"difference: {a - b}")

    # Tuple unpacking
    point = (10, 20)
    x, y = point
    print(f"point ({x}, {y})")


if __name__ == "__main__":
    list_comprehension_sample()
    print("---")
    dict_operations_sample()
    print("---")
    set_tuple_sample()
