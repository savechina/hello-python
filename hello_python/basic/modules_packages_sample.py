"""
Modules & Packages Sample.
Demonstrates import, from...import, __name__, and __all__.
"""

import math
from datetime import datetime


def import_basics():
    """Demonstrates import module and from...import."""
    print(f"pi = {math.pi:.4f}")
    print(f"now = {datetime.now().strftime('%Y-%m-%d %H:%M')}")


def name_check():
    """Demonstrates __name__ == '__main__' guard behavior."""
    if __name__ == "__main__":
        print("This module is run directly")
    else:
        print("This module is imported by another module")


__all__ = ["import_basics"]


def internal_helper():
    """This function is NOT exported via __all__."""
    return "internal"


if __name__ == "__main__":
    import_basics()
    print("---")
    name_check()
