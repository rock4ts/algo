def decimal_to_binary(decimal_n):
    binary_n = []
    
    if decimal_n == 0:
        return '0'

    while decimal_n != 1:
        remainder = decimal_n % 2
        binary_n.insert(0, str(remainder))
        decimal_n = decimal_n // 2
    binary_n.insert(0, str(decimal_n))

    return ''.join(binary_n)


def main():
    decimal_n = int(input())
    print(decimal_to_binary(decimal_n))


if __name__ == '__main__':
    main()
