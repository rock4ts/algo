def least_primes_linear(n):
    lp = [0] * (n + 1)
    primes = []

    for i in range(2, n + 1):
        if lp[i] == 0:
            primes.append(i)
            lp[i] = i
        
        for p in primes:
            x = p * i
            if (p > lp[i]) or (x > n):
                break
            lp[x] = p
    
    return lp, primes


def main():
    n = int(input())
    print(', '.join([str(p) for p in least_primes_linear(n)[1]]))


if __name__ == '__main__':
    main()
