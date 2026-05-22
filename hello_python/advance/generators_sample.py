def fibonacci_sample():
    """Demonstrates generator function for fibonacci sequence."""

    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b

    fib = fibonacci(10)
    for num in fib:
        print(num, end=" ")
    print()


def generator_expression_sample():
    """Demonstrates generator expression vs list comprehension."""

    nums = [1, 2, 3, 4, 5]
    gen = (x * x for x in nums)
    print("Generator expression:")
    for val in gen:
        print(val, end=" ")
    print()

    gen2 = (x * x for x in nums)
    print("First:", next(gen2))
    print("Second:", next(gen2))


def send_sample():
    """Demonstrates generator send() method."""

    def accumulator():
        total = 0
        while True:
            value = yield total
            if value is not None:
                total += value

    acc = accumulator()
    next(acc)
    print("After 5:", acc.send(5))
    print("After 10:", acc.send(10))
    print("After -3:", acc.send(-3))
    acc.close()


if __name__ == "__main__":
    fibonacci_sample()
    print()
    generator_expression_sample()
    print()
    send_sample()
