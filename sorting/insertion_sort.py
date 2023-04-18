
def insertion_sort(array):
    for i in range(1, len(array)):
        value_to_insert = array[i]
        while i > 0 and value_to_insert < array[i-1]:
            array[i] = array[i-1]
            i -= 1
        array[i] = value_to_insert
    return array
