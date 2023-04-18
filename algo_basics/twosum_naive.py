def twosum(n, values, k):
    for i in range(n):
        first_value = values[i]
        for j in range(i+1, n):
            second_value = values[j]
            if (first_value + second_value) == k:
                return str(first_value) + ' ' + str(second_value)
    return 'None'

with open('input.txt', 'r') as input_f, open('output.txt', 'w') as output_f:
    n, values, k = (
        [row.strip() for row in input_f.readlines()]
    )
    values = [int(value) for value in values.split()]
    output_f.write(twosum(int(n), values, int(k)))
