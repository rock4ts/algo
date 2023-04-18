
def bubble_sort(array, number_of_elems):
    for i in range(0, number_of_elems - 1):
        has_swaps = False
        for j in range(0, number_of_elems - i - 1):
            if array[j+1] < array[j]:
                array[j], array[j+1] = array[j+1], array[j]
                has_swaps = True
        if has_swaps or (i == 0):
            print(' '.join([str(elem) for elem in array]))
        if not has_swaps:
            return


if __name__ == '__main__':
    number_of_elems = int(input())
    array_to_sort = list(map(int, input().split()))

    bubble_sort(array_to_sort, number_of_elems)
