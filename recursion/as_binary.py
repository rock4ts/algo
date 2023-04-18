
def as_binary_string(n):
    if n < 0:
        return '-' + as_binary_string(-n)
    if n == 0 or n == 1:
        return str(n)
    last_digit = n % 2
    return as_binary_string(n // 2) + str(last_digit)


if __name__ == '__main__':
    n = int(input())
    print(as_binary_string(n))
