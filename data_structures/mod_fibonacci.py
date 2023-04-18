
def fib_modulo(n, k):
    a, b = 0, 1
    modulo_divisor = 10 ** k

    for _ in range(n):
        if b > modulo_divisor:
            b_remainder = b % modulo_divisor
            a, b = b_remainder, a + b_remainder
        else:
            a, b = b, a + b
    return b % modulo_divisor


if __name__ == '__main__':
    n, k = map(int, input().split())
    print(fib_modulo(n, k))
