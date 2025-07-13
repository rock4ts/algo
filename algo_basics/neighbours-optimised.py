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


def neighbours(matrix, num_of_rows, num_of_cols, x, y):
    neighbours_list = []

    for i in range(-1 , 2):
        for j in range(-1, 2):
            x_i = x + i
            y_j = y + j
            if (i != 0 and j != 0) or (i == 0 and j == 0):
                continue
            if x_i < 0 or x_i > (num_of_cols - 1):
                continue
            if y_j < 0 or y_j > (num_of_rows - 1):
                continue
            neighbours_list.append(matrix[y_j][x_i])
    neighbours_list = [int(elem) for elem in neighbours_list]
    neighbours_list.sort()
    return neighbours_list


if __name__ == '__main__':
    lines = sys.stdin.readlines()
    matrix = [row.split() for row in lines[2: -2]]
    num_or_rows, num_of_cols = int(lines[0]), int(lines[1])
    x, y = int(lines[-1]), int(lines[-2])

    result = neighbours(matrix, num_or_rows, num_of_cols,  x, y)
    print(' '.join([str(neighbour) for neighbour in result]))
