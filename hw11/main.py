# Создайте класс Матрица.
# Добавьте методы для:
# вывода на печать,
# проверку на равенство,
# сложения,
# *умножения матриц

from matrix_class import Matrix

m1_prefill = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
m2_prefill = [[1, 4, 7],
              [2, 5, 8],
              [3, 6, 9]]
m1 = Matrix(m1_prefill)
m2 = Matrix(m2_prefill)
print(m1 == m2)
m3 = m1 + m2
m4 = m1 * m2
m3.print_matrix()
m4.print_matrix()
