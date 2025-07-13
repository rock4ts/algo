'''
https://contest.yandex.ru/contest/23389/problems/K/

Списочная форма

Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Вася просил Аллу помочь решить задачу. На этот раз по информатике.

Для неотрицательного целого числа X списочная форма –— это массив его цифр слева направо. К примеру, для 1231 списочная форма будет [1,2,3,1]. На вход подается количество цифр числа Х, списочная форма неотрицательного числа Х и неотрицательное число K. Число К не превосходят 10000. Длина числа Х не превосходит 1000.

Нужно вернуть списочную форму числа X + K.

Формат ввода
В первой строке — длина списочной формы числа X. На следующей строке — сама списочная форма с цифрами записанными через пробел.

В последней строке записано число K, 0 ≤ K ≤ 10000.

Формат вывода
Выведите списочную форму числа X+K.

Пример 1
Ввод	    Вывод
4           1 2 3 4
1 2 0 0
34

Пример 2
Ввод	    Вывод
2           1 1 2
9 5
17
'''

def list_form_sum(len_x, x, k):
    k = [int(d) for d in k]
    len_k = len(k)
    min_len = min(len_x, len_k)
    result = x if len_k == min_len else k
    adder = x if k == result else k
    result = [0] + result
    len_diff = len(result) - min_len
    carrier = 0

    for i in range(min_len - 1, -1, -1):
        sum_i = result[len_diff + i] + adder[i] + carrier
        result[len_diff + i] = sum_i % 10
        carrier = 1 if sum_i > 9 else 0

    if carrier > 0:
        for j in range(len_diff - 1, -1, -1):
            sum_j = result[j] + carrier
            result[j] = sum_j % 10
            carrier = 1 if sum_j > 9 else 0
            if carrier == 0:
                break

    return result if result[0] != 0 else result[1:]


def main():
    len_x = int(input())
    x = [int(d) for d in input().split()]
    k = input()
    print(' '.join([str(d) for d in list_form_sum(len_x, x, k)]))


if __name__ == '__main__':
    main()