def twosum_extra_ds(numbers, k):
    seen_nums = set()
    for num in numbers:
        required_num = k - num
        if required_num in seen_nums:
            return f'{required_num} {num}'
        seen_nums.add(num)
    return 'None'


with open('input.txt', 'r') as input_f, open('output.txt', 'w') as output_f:
    n, numbers, k = [row.strip() for row in input_f.readlines()]
    numbers = [int(num) for num in numbers.split()]
    output_f.write(twosum_extra_ds(numbers, int(k)))
