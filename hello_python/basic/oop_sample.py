"""
Object-Oriented Programming (OOP) Sample.
Demonstrates class definition, inheritance, and dunder methods.
"""


class Animal:
    """Base class demonstrating __init__, self, and instance attributes."""

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return "..."

    def __str__(self):
        return f"{self.name} ({self.species})"


class Dog(Animal):
    """Inheritance — overrides speak and adds breed attribute."""

    def __init__(self, name, breed):
        super().__init__(name, species="狗")
        self.breed = breed

    def speak(self):
        return "汪汪！"

    def __repr__(self):
        return f"Dog('{self.name}', '{self.breed}')"


class Cat(Animal):
    """Another subclass with different speak behavior."""

    def speak(self):
        return "喵~"


def class_definition_sample():
    """Demonstrates basic class creation and instantiation."""
    pet = Animal("Buddy", "Dog")
    print(pet)


def inheritance_sample():
    """Demonstrates class inheritance and method overriding."""
    dog = Dog("旺财", "金毛")
    cat = Cat("咪咪", "猫")

    for animal in [dog, cat]:
        print(f"  {animal.name}: {animal.speak()}")


def dunder_methods_sample():
    """Demonstrates __str__, __repr__, and __len__."""
    dog = Dog("大黄", "田园犬")
    print(f"str:  {dog}")
    print(f"repr: {repr(dog)}")


if __name__ == "__main__":
    class_definition_sample()
    print("---")
    inheritance_sample()
    print("---")
    dunder_methods_sample()
