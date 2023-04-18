def list_form_sum(len_x, x, k):
    k = [int(d) for d in k]
    len_k = len(k)
    max_len = max(len_x, len_k)
    x = [0] * (max_len - len_x) + x
    k = [0] * (max_len - len_k) + k
    result = []
    carrier = 0

    for i in range(max_len - 1, - 1, -1):
        r = carrier
        r += x[i] + k[i]
        result.insert(0, r % 10)
        carrier = 1 if r > 9 else 0
    
    if carrier > 0:
        result.insert(0, 1)

    return result


def main():
    len_x = int(input())
    x = [int(d) for d in input().split()]
    k = input()
    print(' '.join([str(d) for d in list_form_sum(len_x, x, k)]))


if __name__ == '__main__':
    main()
