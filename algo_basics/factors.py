from math import sqrt


def factors(n):
    factors = []
    j = 2

    while n > 1:
        for i in range(j, int(sqrt(n)) + 1):
            if n % i == 0:
                n //= i
                factors.append(i)
                break
        else:
            factors.append(n)
            break
    
    return factors


def main():
    n = int(input())
    print(' '.join([str(f) for f in factors(n)]))


if __name__ == '__main__':
    main()
