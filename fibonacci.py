from re import A


def fibonacci(num):
    a = 0
    b = 1
    for i in range(2, num + 1):
        a, b = b + a, a
    return b