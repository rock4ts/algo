
def purchase_day(savings, price, left, right):
    if right - left <= 1 and price <= savings[left]:
        return left + 1
    elif right - left <= 1 and price <= savings[right]:
        return right + 1
    elif right == left:
        return -1

    mid = (left + right) // 2

    if price <= savings[mid]:
        return purchase_day(savings, price, left, mid)
    else:
        return purchase_day(savings, price, mid + 1, right)


if __name__ == '__main__':
    num_of_days = int(input())
    savings = list(map(int, input().split()))
    price = int(input())
    double_price = price * 2

    print(
        purchase_day(savings, price, 0, num_of_days - 1),
        purchase_day(savings, double_price, 0, num_of_days - 1)
    )
