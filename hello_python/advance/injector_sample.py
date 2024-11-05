from dataclasses import dataclass
from typing import NewType

from injector import Binder, Injector, Module, inject, provider, singleton

Name = NewType("Name", str)
Description = NewType("Description", str)


class User:
    @inject
    def __init__(self, name: Name, description: Description):
        self.name = name
        self.description = description


class UserModule(Module):
    def configure(self, binder: Binder):
        binder.bind(User)


class UserAttributeModule(Module):
    def configure(self, binder: Binder):
        binder.bind(Name, to="Sherlock")

    @provider
    def describe(self, name: Name) -> Description:
        return "%s is a man of astounding insight" % name


# from pydantic import BaseModel
# Step 1: Define some classes with dependencies
class ServiceA:
    def say_hello(self):
        return "Hello from ServiceA"


class ServiceB:
    @inject
    def __init__(self, service_a: ServiceA):
        self.service_a = service_a

    def say_hello(self):
        return f"Hello from ServiceB, with {self.service_a.say_hello()}"


# Step 2: Create an Injector for Dependency Injection
class MyServiceModule(Module):
    def configure(self, binder):
        # Dynamically register classes here
        binder.bind(ServiceA, to=ServiceA, scope=singleton)
        binder.bind(ServiceB, to=ServiceB, scope=singleton)


class Greeter:
    """Greeter class"""

    @inject
    def __init__(self, name: str):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")


class Inner:
    """Inner"""

    def __init__(self):
        self.forty_two = 42


# @dataclass
class Outer:
    """Outer"""

    @inject
    def __init__(self, inner: Inner):
        self.inner = inner


def inject_main():
    """Container setup"""
    container = Injector([MyServiceModule(), UserModule(), UserAttributeModule()])
    container.binder.bind(str, to="World")

    greeter = container.get(Greeter)
    greeter.greet()

    outer = container.get(Outer)
    print("outer:", outer.inner.forty_two)

    # Dynamically getting an instance of ServiceB which has a dependency on ServiceA
    service_b_instance = container.get(ServiceB)

    # Step 4: Use the injected instance
    print(
        service_b_instance.say_hello()
    )  # Output: Hello from ServiceB, with Hello from ServiceA

    name = container.get(Name)
    print("name:", name)

    print("description:", container.get(Description))

    user = container.get(User)
    print("user is User Class", isinstance(user, User))

    print(f"user: {user.name},description: {user.description}")
