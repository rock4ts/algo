'''
https://contest.yandex.ru/contest/23389/problems/C/

Соседи

Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его соседей. Соседним считается элемент, находящийся от текущего на одну ячейку влево, вправо, вверх или вниз. Диагональные элементы соседними не считаются.

Например, в матрице A соседними элементами для (0, 0) будут 2 и 0. А для (2, 1) –— 1, 2, 7, 7.



Формат ввода
В первой строке задано n — количество строк матрицы. Во второй — количество столбцов m. Числа m и n не превосходят 1000. В следующих n строках задана матрица. Элементы матрицы — целые числа, по модулю не превосходящие 1000. В последних двух строках записаны координаты элемента, соседей которого нужно найти. Индексация начинается с нуля.

Формат вывода
Напечатайте нужные числа в возрастающем порядке через пробел.
'''

import sys


def neighbours(n, m, matrix, x, y):
    neighbour_list = []
    row_ix_max = n - 1
    col_ix_max = m - 1

    if x == 0 and row_ix_max > 0:
        neighbour_list.append(matrix[x+1][y])
    elif x == row_ix_max and row_ix_max > 0:
        neighbour_list.append(matrix[x-1][y])
    elif x != 0 and row_ix_max > x:
        neighbour_list.extend([matrix[x-1][y], matrix[x+1][y]])

    if y == 0 and col_ix_max > 0:
        neighbour_list.append(matrix[x][y+1])
    elif y == col_ix_max and col_ix_max > 0:
        neighbour_list.append(matrix[x][y-1])
    elif y != 0 and col_ix_max > y:
        neighbour_list.extend([matrix[x][y-1], matrix[x][y+1]])

    neighbour_list = [int(elem) for elem in neighbour_list]
    neighbour_list.sort()
    return neighbour_list


def main():
    n, m = int(input()), int(input())

    matrix = []
    for i in range(n):
        line = sys.stdin.readline().rstrip()
        matrix.append(line.split())

    x, y = int(input()), int(input())
    print(' '.join([str(elem) for elem in neighbours(n, m, matrix, x, y)]))


if __name__ == '__main__':
    main()
