row_col = int(input())
matrix = []

for row in range(row_col):
    matrix.append([])
    for col in range(row_col):
        matrix[row].append(col + 1 + row * row_col)

row_sums = [sum(row) for row in matrix]

for row_sum in row_sums:
    print(row_sum)

