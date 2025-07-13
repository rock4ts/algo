
def linear_seave(n):
    lp = [0] * (n + 1)
    primes = []

    for i in range(2, n + 1):
        if lp[i] == 0:
            primes.append(i)
            lp[i] = i

        for p in primes:
            x = p * i
            if (p <= lp[i]) and (x <= n):
                lp[x] = p

    return lp, primes


def main():
    n = int(input())
    print(', '.join([str(p) for p in linear_seave(n)[1]]))


if __name__ == '__main__':
    main()
