# Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1
# # j = 0,1, n-1.
# Test Data : Rows = 3, Columns = 4
# Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

row_number=int(input("Enter the number of rows:"))
column_number=int(input("ENter the number of columns:"))
matrix=[[0 for j in range (column_number)]for i in range (row_number)]
for i in range(row_number):
    for j in range(column_number):
        matrix[i][j]=i*j
print(matrix)