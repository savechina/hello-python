from typing import List, Dict, Optional, TypedDict


def basic_annotations_sample():
    """Demonstrates basic function type annotations."""

    def greet(name: str, age: int) -> str:
        return f"{name} is {age} years old"

    def get_average(numbers: List[float]) -> float:
        return sum(numbers) / len(numbers)

    def find_user(uid: int) -> Optional[str]:
        users: Dict[int, str] = {1: "Alice", 2: "Bob"}
        return users.get(uid)

    print(greet("Alice", 30))
    print(f"Average: {get_average([1.0, 2.0, 3.0])}")
    print(f"User 1: {find_user(1)}")
    print(f"User 3: {find_user(3)}")


def union_type_sample():
    """Demonstrates Union and X | Y syntax (Python 3.10+)."""

    def process_value(value: str | int | float) -> str:
        match value:
            case str(s):
                return f"String: {s.upper()}"
            case int(n) | float(n):
                return f"Number: {n * 2}"

    ScoreBoard = dict[str, list[int]]
    def get_top_student(scores: ScoreBoard) -> str | None:
        if not scores:
            return None
        best = max(scores, key=lambda k: max(scores[k]))
        return best

    scores: ScoreBoard = {"Alice": [90, 95], "Bob": [80, 85]}
    print(process_value("hello"))
    print(process_value(42))
    print(f"Top student: {get_top_student(scores)}")


def typed_dict_sample():
    """Demonstrates TypedDict and Protocol."""

    class User(TypedDict):
        name: str
        age: int
        email: str

    def format_user(user: User) -> str:
        return f"{user['name']} ({user['age']}) - {user['email']}"

    alice: User = {"name": "Alice", "age": 30, "email": "alice@example.com"}
    print(format_user(alice))


if __name__ == "__main__":
    basic_annotations_sample()
    print()
    union_type_sample()
    print()
    typed_dict_sample()
