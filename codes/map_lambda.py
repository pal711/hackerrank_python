#!/bin/python3

cube = lambda x: x**3

def fibo():
    a = 0
    yield 0
    b= 1
    yield 1
    while True:
        c = a + b
        yield c
        a = b
        b = c


def fibonacci(n):
    fib = fibo()
    return [next(fib) for x in range(n)]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

