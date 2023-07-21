"""
Matrix Transpose:
Description: Write a program that calculates the transpose of a given matrix.
Example:
Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
"""
input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output_matrix = []

# Determine the dimensions of the input matrix
rows = len(input_matrix)
print(rows)
cols = len(input_matrix[0])
print(cols)

# Create an empty output matrix with swapped dimensions
for i in range(cols):
    output_matrix.append([0] * rows)

# Calculate the transpose by swapping the elements
for i in range(rows):
    for j in range(cols):
        output_matrix[j][i] = input_matrix[i][j]

print(output_matrix)
