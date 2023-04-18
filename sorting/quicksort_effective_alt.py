# 83682535

def sepatate_by_pivot(array, left, right):
    pivot = array[left]
    i, j = left + 1, right

    while True:
        if i <= j and array[j] > pivot:
            j -= 1
        elif i <= j and array[i] < pivot:
            i += 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
        else:
            array[left], array[j] = array[j], array[left]
            return j


def quicksort_effective(array, left, right):
    if right - left > 0:
        pivot_ix = sepatate_by_pivot(array, left, right)
        quicksort_effective(array, left, pivot_ix - 1)
        quicksort_effective(array, pivot_ix + 1, right)


def prepare_competitor_data(competitor: list) -> tuple:
    competitor[1] = -int(competitor[1])
    competitor[2] = int(competitor[2])
    return (competitor[1], competitor[2], competitor[0])


if __name__ == '__main__':
    number_of_competitors = int(input())
    competitors = [
        prepare_competitor_data(input().split()) for competitor in range(
            number_of_competitors
        )
    ]
    quicksort_effective(competitors, 0, number_of_competitors - 1)
    print(*(list(zip(*competitors))[2]), sep='\n')
