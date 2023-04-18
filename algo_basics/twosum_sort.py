def twosum_sort(n, numbers, k):
    numbers.sort()
    left_ix = 0
    right_ix = n - 1
    
    while left_ix < right_ix:
        left_num = numbers[left_ix]
        right_num = numbers[right_ix]
        current_sum = left_num + right_num
        if current_sum == k:
            return f'{left_num} {right_num}'
        if current_sum < k:
            left_ix += 1
        else:
            right_ix -= 1
    return 'None'


with open('input.txt', 'r') as input_f, open('output.txt', 'w') as output_f:
    n, numbers, k = [row.strip() for row in input_f.readlines()]
    n, numbers, k = int(n), [int(num) for num in numbers.split()], int(k)
    output_f.write(twosum_sort(n, numbers, k))
