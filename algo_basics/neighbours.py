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
        neighbour_list.extend([matrix[x+1][y], matrix[x-1][y]])
    
    if y == 0 and col_ix_max > 0:
        neighbour_list.append(matrix[x][y+1])
    elif y == col_ix_max and col_ix_max > 0:
        neighbour_list.append(matrix[x][y-1])
    elif y != 0 and col_ix_max > y:
        neighbour_list.extend([matrix[x][y+1], matrix[x][y-1]])

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
