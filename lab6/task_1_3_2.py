from prettytable import PrettyTable
from functools import wraps
import copy
import math


def sorting_decorator(func):
    """Декоратор для ввімкнення/вимкнення сортування."""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.sorting_enabled:
            self.matrix = self.selection_sort_columns(self.matrix)
        return func(self, *args, **kwargs)
    return wrapper


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.sorting_enabled = True

    def print_table(self, title="Matrix"):
        """Вивід матриці у вигляді таблиці."""
        print(f"{title}:")
        print(self)
        print("\n")

    def rows_sums(self):
        """Обчислення суми елементів у кожному рядку."""
        return [sum(row) for row in self.matrix]

    def geometric_avg(self, values):
        """Обчислення середнього геометричного значення."""
        values_count = len(values)
        values_product = math.prod(values)
        return values_product ** (1 / values_count)

    def selection_sort_columns(self, matrix):
        """Сортування стовпців методом вибору."""
        rows = len(matrix)
        cols = len(matrix[0])
        sorted_matrix = copy.deepcopy(matrix)
        for col in range(cols):
            for row in range(rows - 1):
                min_index = row
                for j in range(row + 1, rows):
                    if sorted_matrix[j][col] < sorted_matrix[min_index][col]:
                        min_index = j
                sorted_matrix[row][col], sorted_matrix[min_index][col] = (
                    sorted_matrix[min_index][col],
                    sorted_matrix[row][col],
                )
        return sorted_matrix

    @sorting_decorator
    def calculate_sums_and_geometric_avg(self):
        """Обчислення сум рядків та середнього геометричного."""
        sums = self.rows_sums()
        print_table = [[value] for value in sums]
        self.print_table("Row Sums")
        print(f"Geometric average of row sums: {self.geometric_avg(sums)}")
        return sums

    def __add__(self, other):
        """Перевантаження оператора додавання для матриць."""
        if isinstance(other, Matrix):
            if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
                raise ValueError("Matrices must have the same dimensions for addition.")
            result = [
                [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
                for i in range(len(self.matrix))
            ]
            return Matrix(result)
        else:
            raise TypeError("Addition is only supported between two Matrix instances.")

    def __sub__(self, other):
        """Перевантаження оператора віднімання для матриць."""
        if isinstance(other, Matrix):
            if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
                raise ValueError("Matrices must have the same dimensions for addition.")
            result = [
                [self.matrix[i][j] - other.matrix[i][j] for j in range(len(self.matrix[0]))]
                for i in range(len(self.matrix))
            ]
            return Matrix(result)
        else:
            raise TypeError("Addition is only supported between two Matrix instances.")

    def __str__(self):
        """Перевантаження виводу матриці."""
        table = PrettyTable(header=False)
        for row in self.matrix:
            table.add_row(row)
        return str(table)



matrix_data = [
    [2, 0, 33, -1, -21],
    [78, 7, -4, -3, 11],
    [-2, -7, -1, -9, 0],
    [13, 61, 60, 42, -10],
    [1, 0, 4, 0, 16]
]

matrix = Matrix(matrix_data)
matrix.print_table("Original Matrix")


matrix.calculate_sums_and_geometric_avg()


matrix.sorting_enabled = False
matrix.calculate_sums_and_geometric_avg()


other_matrix_data = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

other_matrix = Matrix(other_matrix_data)
result_matrix = matrix + other_matrix
print("Result of matrix addition:")
print(result_matrix)
result_matrix_sub = matrix - other_matrix
print("Result of matrix addition:")
print(result_matrix)
print("Result of matrix substuction:")
print(result_matrix_sub)
