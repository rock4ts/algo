
def str_sum_comporator(num_one: str, num_two: str):
    one_two = num_one + num_two
    two_one = num_two + num_one

    if int(one_two) > int(two_one):
        return True
    return False


def combine_to_biggest_number(num_array, array_len, str_sum_comporator):
    for i in range(1, array_len):
        num_to_insert = num_array[i]

        while i > 0 and str_sum_comporator(num_to_insert, num_array[i-1]):
            num_array[i] = num_array[i-1]
            i -= 1
        num_array[i] = num_to_insert
    return num_array


if __name__ == '__main__':
    array_len = int(input())
    num_array = input().split()
    print(
        ''.join(combine_to_biggest_number(
                    num_array,
                    array_len,
                    str_sum_comporator
            )
        )
    )
