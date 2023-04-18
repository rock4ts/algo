
def fib_naive(n):
    if n in (0, 1):
        return 1
    return fib_naive(n-1) + fib_naive(n-2)


def fib_effective(n):
    fib_list = [1, 1]
    for _ in range(2, n+1):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[-1]


def fib_memo(n, computed={0: 1, 1: 1}):
    if n not in computed:
        computed[n] = fib_memo(n-1, computed) + fib_memo(n-2, computed)
    return computed[n]


def fib_stacking(n):
    n_minus_two, n_minus_one = 0, 1

    for _ in range(n):
        n_minus_two, n_minus_one = n_minus_one, n_minus_two + n_minus_one
    return n_minus_one


if __name__ == '__main__':
    n = int(input())
    print(fib_stacking(n))
