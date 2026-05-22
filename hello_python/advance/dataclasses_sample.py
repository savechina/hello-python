from dataclasses import dataclass, field
from typing import List


def basic_dataclass_sample():
    """Demonstrates basic @dataclass usage."""

    @dataclass
    class Point:
        x: float
        y: float

    @dataclass
    class Person:
        name: str
        age: int
        email: str = "unknown@example.com"

    p = Point(3.0, 4.0)
    alice = Person("Alice", 30)
    bob = Person("Bob", 25, "bob@example.com")

    print(f"Point: {p}")
    print(f"Alice: {alice}")
    print(f"Bob: {bob}")
    print(f"p == Point(3.0, 4.0): {p == Point(3.0, 4.0)}")


def field_and_frozen_sample():
    """Demonstrates field() options and frozen dataclasses."""

    @dataclass(frozen=True)
    class Config:
        host: str = "localhost"
        port: int = 8080
        debug: bool = False

    @dataclass
    class Team:
        name: str
        members: List[str] = field(default_factory=list)

    config = Config()
    team = Team("Python Team")
    team.members.append("Alice")
    team.members.append("Bob")

    print(f"Config: host={config.host}, port={config.port}")
    print(f"Team: {team}")


def post_init_sample():
    """Demonstrates __post_init__ for validation."""

    @dataclass
    class Rectangle:
        width: float
        height: float
        area: float = field(init=False)

        def __post_init__(self):
            self.area = self.width * self.height

    rect = Rectangle(5.0, 3.0)
    print(f"Rectangle {rect.width}x{rect.height}, area={rect.area}")


if __name__ == "__main__":
    basic_dataclass_sample()
    print()
    field_and_frozen_sample()
    print()
    post_init_sample()
