"""
String Advanced Sample.
Demonstrates re module, string methods, and advanced f-string formatting.
"""

import re


def re_module_sample():
    """Demonstrates re.search, re.findall, and re.sub."""
    text = "Order #1234, total: ¥89.50. Order #5678, total: ¥120.00"

    # findall — extract all order numbers
    orders = re.findall(r"#(\d+)", text)
    print(f"order ids: {orders}")

    # re.sub — replace
    redacted = re.sub(r"¥\d+\.\d{2}", "***", text)
    print(f"redacted: {redacted}")

    # re.search with groups
    match = re.search(r"total: ¥(\d+\.\d{2})", text)
    if match:
        print(f"first total: {match.group(1)}")


def string_methods_sample():
    """Demonstrates split, join, strip, and replace."""
    csv = "name,age,city\nAlice,30,Shanghai\nBob,25,Beijing"

    lines = csv.strip().split("\n")
    for line in lines:
        fields = line.split(",")
        print(f"  fields: {fields}")

    # join
    reversed_csv = "\n".join(line for line in reversed(lines))
    print(f"reversed:\n{reversed_csv}")


def fstring_advanced_sample():
    """Demonstrates advanced f-string format specs."""
    name = "Alice"
    score = 95.678
    count = 42

    print(f"name: {name:>10}")
    print(f"score: {score:8.2f}")
    print(f"count (binary): {count:b}")
    print(f"count (hex): {count:x}")


if __name__ == "__main__":
    re_module_sample()
    print("---")
    string_methods_sample()
    print("---")
    fstring_advanced_sample()
