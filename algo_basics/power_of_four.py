def is_power_of_four(num):
    nth_power_of_four = 1
    while num >= nth_power_of_four:
        if num == nth_power_of_four:
            return True
        nth_power_of_four = nth_power_of_four * 4
    return False


def main():
    num = int(input())
    print(is_power_of_four(num))


if __name__ == '__main__':
    main()
