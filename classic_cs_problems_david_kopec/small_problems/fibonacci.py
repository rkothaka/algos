from typing import Generator


def fibonacci(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1

    last: int = 0
    current: int = 1
    for _ in range(1, n):
        last, current = current, last + current
        yield current


if __name__ == '__main__':
    for i in fibonacci(50):
        print(i)
