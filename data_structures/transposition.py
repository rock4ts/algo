
def transposition(num_of_rows, num_of_cols, matrix):
    for i in range(num_of_cols):
        for j in range(num_of_rows):
            print(matrix[j][i], end=' ')
        print()


if __name__ == '__main__':
    num_of_rows = int(input())
    num_of_cols = int(input())
    matrix = [
        input().split() for row in range(num_of_rows)
    ]
    transposition(num_of_rows, num_of_cols, matrix)
