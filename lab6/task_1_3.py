from prettytable import PrettyTable

def print_table(matrix, title="Matrix"):
  print(f"{title}:")
  result_table = PrettyTable(header=False)
  for row in matrix:
     result_table.add_row(row)
  print(result_table)
  print("\n")

# fi(aij)- сума елементів у кожному рядку матриці;
def rows_sums(matrix):
    return [sum(row) for row in matrix]

# F(fi(aij))- середнє геометричне значення fi(aij)
def geometric_avg(values):
    values_count = len(values)
    values_product = 1
    for value in values:
      values_product *= value
    return values_product**(1/values_count)

def selection_sort_columns(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for col in range(cols):
        for row in range(rows - 1):
            min_index = row
            for j in range(row + 1, rows):
                if matrix[j][col] < matrix[min_index][col]:
                    min_index = j
            matrix[row][col], matrix[min_index][col] = matrix[min_index][col], matrix[row][col]
    return matrix

matrix = [
    [2, 0, 33, -1, -21],
    [78, 7, -4, -3, 11],
    [-2, -7, -1, -9, 0],
    [13, 61, 60, 42, -10],
    [1, 0, 4, 0, 16]
]
start_matrix = [elem.copy() for elem in matrix]
sorted_matrix = selection_sort_columns(matrix)
rows_sums_table = [[value] for value in rows_sums(sorted_matrix)]

print_table(start_matrix, title="Matrix")
print_table(sorted_matrix, title="Sorted Matrix")
print_table(rows_sums_table, title="Row Sums")
print(f"Geometric average of row sums: {geometric_avg(rows_sums(sorted_matrix))}")
