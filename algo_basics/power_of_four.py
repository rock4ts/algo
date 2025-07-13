'''
https://contest.yandex.ru/contest/23389/problems/I/

Степень четырёх

Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Напишите программу, которая определяет, будет ли положительное целое число степенью четвёрки.

Подсказка: степенью четвёрки будут все числа вида 4n, где n – целое неотрицательное число.

Формат ввода
На вход подаётся целое число в диапазоне от 1 до 10000.

Формат вывода
Выведите «True», если число является степенью четырёх, «False» –— в обратном случае.

Пример 1
Ввод	Вывод
15      False
Пример 2
Ввод	Вывод
16      True
'''

def is_power_of_four(num):
    nth_power_of_four = 1
    while nth_power_of_four <= num:
        if num == nth_power_of_four:
            return True
        nth_power_of_four = nth_power_of_four * 4
    return False


def main():
    num = int(input())
    print(is_power_of_four(num))


if __name__ == '__main__':
    main()
