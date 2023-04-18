def moving_average(n, timeseries, k):
    result = list()
    current_sum = sum(timeseries[:k])
    result.append(current_sum / k)

    if n == k:
        return 

    for i in range(0, n - k):
        current_sum = current_sum - timeseries[i] + timeseries[k+i]
        result.append(current_sum / k)

    return result


with open('input.txt', 'r') as input_f, open('output.txt', 'w') as output_f:
    n, timeseries, k = [row.strip() for row in input_f.readlines()]
    timeseries = [int(num) for num in timeseries.split()]
    result = moving_average(int(n), timeseries, int(k))
    output_f.write(' '.join([str(num) for num in result]))
