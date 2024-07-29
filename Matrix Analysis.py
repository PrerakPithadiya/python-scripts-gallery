import random

# Step 1: Generate a 4x4 2-dimensional list filled with random 0s and 1s
matrix = [[random.randint(0, 1) for _ in range(4)] for _ in range(4)]

# Step 2: Print the generated list
print("Generated 4x4 matrix:")
for row in matrix:
    print(row)

# Step 3: Calculate the number of 1s in each row and each column
row_counts = [sum(row) for row in matrix]
col_counts = [sum(matrix[row][col] for row in range(4)) for col in range(4)]

# Step 4: Identify the rows and columns with the most number of 1s
max_row_1s = max(row_counts)
max_col_1s = max(col_counts)

rows_with_max_1s = [
    index for index, count in enumerate(row_counts) if count == max_row_1s
]
cols_with_max_1s = [
    index for index, count in enumerate(col_counts) if count == max_col_1s
]

print("\nRows with the most number of 1s:")
for row in rows_with_max_1s:
    print(f"Row {row} with {max_row_1s} 1s")

print("\nColumns with the most number of 1s:")
for col in cols_with_max_1s:
    print(f"Column {col} with {max_col_1s} 1s")
