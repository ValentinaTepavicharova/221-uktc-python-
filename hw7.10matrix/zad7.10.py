row_col = int(input())
matrix = []

for _ in range(row_col):
    element_matrix = [int(x) for x in input("Enter number split', ':").split(", ")]
    matrix.append(element_matrix)

diagonal_sum = sum(matrix[i][row_col-1-j] for i in range(row_col) for j in range(i+1))

print(diagonal_sum)
