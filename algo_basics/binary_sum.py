def binary_sum(first_num, second_num):
    max_len = max(len(first_num), len(second_num))
    first_num = first_num.zfill(max_len)
    second_num = second_num.zfill(max_len)
    result = ''
    carrier = 0

    for i in range(max_len - 1, -1, -1):
        i_sum = carrier
        i_sum += 1 if first_num[i] == '1' else 0
        i_sum += 1 if second_num[i] == '1' else 0
        result = str(i_sum % 2) + result
        carrier = 0 if i_sum < 2 else 1

    if carrier > 0:
        result = '1' + result

    return result


def main():
    first_num, second_num = input(), input()
    print(binary_sum(first_num, second_num))


if __name__ == '__main__':
    main()
