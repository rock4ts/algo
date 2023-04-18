
# def sort_clothes_counting(array, k):
#     count_vals = [0] * k
#     for val in array:
#         count_vals[val] += 1
#     ix = 0
#     for val in range(k):
#         for _ in range(count_vals[val]):
#             array[ix] = val
#             ix += 1


def sort_clothes_quick(array):
    pivot = 1
    pink, yellow, crimson = '', '', ''
    for elem in array:
        if elem < pivot:
            pink += '0 '
        elif elem == pivot:
            yellow += '1 '
        else:
            crimson += '2 '
    return pink + yellow + crimson


if __name__ == '__main__':
    num_of_vals = int(input())
    array = list(map(int, input().split()))
    # sort_clothes_counting(array, 3)
    # print(' '.join([str(elem) for elem in array]))
    sorted_clothes = sort_clothes_quick(array)
    print(sorted_clothes)
