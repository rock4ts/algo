
def purchase_day(savings, price, left, right):
    if right <= left:
        return -1

    mid = (right + left) // 2

    if (mid == 0 or savings[mid-1] < price) and price <= savings[mid]:
        return mid + 1
    elif price <= savings[mid]:
        return purchase_day(savings, price, left, mid)
    else:
        return purchase_day(savings, price, mid+1, right)


if __name__ == '__main__':
    num_of_days = int(input())
    savings = list(map(int, input().split()))
    price = int(input())
    double_price = price * 2

    print(
        purchase_day(savings, price, 0, num_of_days),
        purchase_day(savings, double_price, 0, num_of_days)
    )
