
def binarySearch(arr, x, left, right):
    if right <= left:
        return -1

    mid = (left + right) // 2

    if arr[mid] == x:
        return mid
    elif x < arr[mid]:
        return binarySearch(arr, x, left, mid)
    else:
        return binarySearch(arr, x, mid + 1, right)


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    arr.sort()
    x = int(input())

    print(binarySearch(arr, x, left=0, right=len(arr)))
