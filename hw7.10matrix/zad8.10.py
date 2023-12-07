row_col = int(input())
matrix = [input("Enter symbol split'':") for _ in range(row_col)]
search_symbol = input("Enter the symbol you want to find:")

found = False
for row in range(row_col):
    for col in range(row_col):
        if matrix[row][col] == search_symbol:
            print(f"({row},{col})")
            found = True
            break
    if found:
        break
if not found:
    print(f"{search_symbol} does not exist in matrix!")
