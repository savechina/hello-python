"""
Loops Sample.
Demonstrates for loops, while loops, enumerate, and zip.
"""

def for_loop_sample():
    """Demonstrates for loop with range and list iteration."""
    # range()
    for i in range(3):
        print(f"range({i}): {i}")

    # iterating over a list
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(f"fruit: {fruit}")


def while_loop_sample():
    """Demonstrates while loop with break and else clause."""
    count = 0
    while count < 3:
        print(f"count: {count}")
        count += 1
    else:
        print("loop completed without break")


def enumerate_zip_sample():
    """Demonstrates enumerate() and zip()."""
    # enumerate
    colors = ["red", "green", "blue"]
    for index, color in enumerate(colors):
        print(f"index {index}: {color}")

    # zip
    names = ["Alice", "Bob"]
    ages = [30, 25]
    for name, age in zip(names, ages):
        print(f"{name} is {age} years old")


if __name__ == "__main__":
    for_loop_sample()
    print("---")
    while_loop_sample()
    print("---")
    enumerate_zip_sample()
