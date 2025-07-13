'''
https://contest.yandex.ru/contest/23389/problems/H/

Двоичная система

Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Тимофей записал два числа в двоичной системе счисления и попросил Гошу вывести их сумму, также в двоичной системе.
Встроенную в язык программирования возможность сложения двоичных чисел применять нельзя.
Помогите Гоше решить задачу.

Решение должно работать за O(N), где N –— количество разрядов максимального числа на входе.

Формат ввода
Два числа в двоичной системе счисления, каждое на отдельной строке.
Длина каждого числа не превосходит 10 000 символов.

Формат вывода
Одно число в двоичной системе счисления.
'''

def binary_sum(first_num, second_num):
    max_len = max(len(first_num), len(second_num))
    first_num = first_num.zfill(max_len)
    second_num = second_num.zfill(max_len)
    result = ''
    carrier = 0

    for i in range(max_len - 1, -1, -1):
        i_sum = carrier
        i_sum += 1 if first_num[i] == '1' else 0
        i_sum += 1 if second_num[i] == '1' else 0
        result = str(i_sum % 2) + result
        carrier = i_sum // 2

    if carrier == 1:
        result = '1' + result

    return result


def main():
    first_num, second_num = input(), input()
    print(binary_sum(first_num, second_num))


if __name__ == '__main__':
    main()
