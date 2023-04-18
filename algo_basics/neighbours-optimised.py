import sys


def neighbours(matrix, num_of_rows, num_of_cols, x, y):
    neighbours_list = []

    for i in range(-1 , 2):
        for j in range(-1, 2):
            x_j = x + j
            y_i = y + i
            if (i != 0 and j != 0) or (i == 0 and j == 0):
                continue
            if x_j < 0 or x_j > (num_of_cols - 1):
                continue
            if y_i < 0 or y_i > (num_of_rows - 1):
                continue
            neighbours_list.append(matrix[y_i][x_j])
    return neighbours_list


if __name__ == '__main__':
    lines = sys.stdin.readlines()
    matrix = [row.split() for row in lines[2: -2]]
    num_or_rows, num_of_cols = int(lines[0]), int(lines[1])
    x, y = int(lines[-1]), int(lines[-2])

    result = neighbours(matrix, num_or_rows, num_of_cols,  x, y)
    print(' '.join([neighbour for neighbour in sorted(result)]))
