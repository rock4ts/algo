# id посылки 81537580, сорри за невнимательность

def distances_to_zero(numbers_count, numbers):
    distances_to_zero = []
    distance = numbers_count

    for num in numbers:
        if num == '0':
            distance = 0
        else:
            distance += 1
        distances_to_zero.append(distance)

    return distances_to_zero


def closest_zero_distance(numbers_count, numbers):
    distances_to_left_zero = distances_to_zero(numbers_count, numbers)
    distances_to_right_zero = (
        list(reversed(distances_to_zero(numbers_count, reversed(numbers))))
    )

    return [
        min(distances_to_left_zero[i], distances_to_right_zero[i])
        for i in range(numbers_count)
    ]


if __name__ == '__main__':
    numbers_count = int(input())
    numbers = input().split()

    print(
        ' '.join(
            [str(d) for d in closest_zero_distance(numbers_count, numbers)]
        )
    )
