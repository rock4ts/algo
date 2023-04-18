
def merge(arr: list, left: int, mid: int, right: int) -> list:
    left_arr, right_arr = arr[left:mid], arr[mid:right]
    k = left
    l, r = 0, 0

    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] <= right_arr[r]:
            arr[k] = left_arr[l]
            l += 1
        else:
            arr[k] = right_arr[r]
            r += 1
        k += 1

    while l < len(left_arr):
        arr[k] = left_arr[l]
        l += 1
        k += 1
    while r < len(right_arr):
        arr[k] = right_arr[r]
        r += 1
        k += 1

    return arr


def merge_sort(arr: list, left: int, right: int) -> None:
    if right - left < 2:
        return
    merge_sort(arr, left, (left+right)//2)
    merge_sort(arr, (left+right)//2, right)
    merge(arr, left, (left+right)//2, right)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0 , 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected
