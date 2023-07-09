# Напишите функцию для транспонирования матрицы
def to_transposition_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i, len((matrix[i]))):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

first_matrix = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
print(*first_matrix, sep="\n")
to_transposition_matrix(first_matrix)
print()
print(*first_matrix, sep="\n")
