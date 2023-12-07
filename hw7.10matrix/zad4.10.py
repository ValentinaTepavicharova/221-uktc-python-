row_col = int(input())
matrix = []

for _ in range(row_col):
    element_matrix = [int(x) for x in input("Enter number split', ':").split(", ")]
    matrix.append(element_matrix)

diagonal_sum = sum(matrix[i][i] for i in range(row_col))
print(diagonal_sum)

