'''
https://contest.yandex.ru/contest/26365/problems/C/

"Скользящее среднее"

Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Вам дана статистика по числу запросов в секунду к вашему любимому рекомендательному сервису.

Измерения велись n секунд.

В секунду i поступает qi запросов.

Примените метод скользящего среднего с длиной окна k к этим данным и выведите результат.

Формат ввода
В первой строке передаётся натуральное число n, количество секунд, в течение которых велись измерения. 1 ≤ n ≤ 105

Во второй строке через пробел записаны n целых неотрицательных чисел qi, каждое лежит в диапазоне от 0 до 103.

В третьей строке записано натуральное число k (1 ≤ k ≤ n) —– окно сглаживания.

Примечание для Go:

Заметьте, что в данной задаче достаточно большой размер ввода. Поэтому необходимо задавать размер буфера для сканнера хотя бы 600 Кб.

Формат вывода
Выведите через пробел результат применения метода скользящего среднего к серии измерений. Должно быть выведено n - k + 1 элементов, каждый элемент -— вещественное (дробное) число.
'''

def moving_average(n, timeseries, k):
    result = []
    current_sum = sum(timeseries[:k])
    result.append(current_sum / k)

    if n == k:
        return result

    for i in range(0, n - k):
        current_sum = current_sum - timeseries[i] + timeseries[k+i]
        result.append(current_sum / k)

    return result


with open('input.txt', 'r') as input_f, open('output.txt', 'w') as output_f:
    n, timeseries, k = [row.strip() for row in input_f.readlines()]
    timeseries = [int(num) for num in timeseries.split()]
    result = moving_average(int(n), timeseries, int(k))
    output_f.write(' '.join([str(num) for num in result]))
