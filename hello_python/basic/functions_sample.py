"""
Functions Sample.
Demonstrates def, *args, **kwargs, lambda, and variable scope.
"""

def def_functions_sample():
    """Demonstrates basic function definition with parameters and return."""
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"

    print(greet("Python"))
    print(greet("Python", "你好"))


def args_kwargs_sample():
    """Demonstrates *args and **kwargs."""
    def show_info(*args, **kwargs):
        for arg in args:
            print(f"  positional: {arg}")
        for key, value in kwargs.items():
            print(f"  keyword: {key} = {value}")

    show_info("Python", "3.13", version="3.13", type="tutorial")


def lambda_scope_sample():
    """Demonstrates lambda and LEGB scope rule."""
    square = lambda x: x * x
    print(f"square(5) = {square(5)}")

    x = "global"
    def outer():
        x = "enclosing"
        def inner():
            x = "local"
            print(f"inner: {x}")
        inner()
        print(f"outer: {x}")
    outer()
    print(f"global: {x}")


if __name__ == "__main__":
    def_functions_sample()
    print("---")
    args_kwargs_sample()
    print("---")
    lambda_scope_sample()
