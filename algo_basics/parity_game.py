def parity_check(a, b, c):
    if a % 2 == b % 2 and a % 2 == c % 2:
        return 'WIN'
    return 'FAIL'


a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

print(parity_check(a, b, c))