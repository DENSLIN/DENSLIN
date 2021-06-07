import numpy as np

matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

matrix1_arr = np.array(matrix1)
matrix2_arr = np.array(matrix2)
n = 1
i = 0
j = 0
sum1 = 0
sum_matrix = []
while n != (matrix1_arr.size + 1):
    sum1 = (matrix1_arr[j, i]) + (matrix2_arr[j, i])
    sum_matrix.append(sum1)
    i += 1
    if i == 3:
        j += 1
        i = 0
    n += 1
sum_matrix_arr = np.array(sum_matrix).reshape(3, 3)
print(sum_matrix_arr)
matrix1_and_matrix1 = matrix1 + matrix2
matrix1_and_matrix1_arr = np.array(matrix1_and_matrix1)
matrix1_and_matrix1_arr_reshape = matrix1_and_matrix1_arr.reshape(2, 9)
print(matrix1_and_matrix1_arr_reshape[0, :]*3)
# print(matrix1_and_matrix1_arr_reshape[:, 0])
matrix1_matrix2_arr = np.concatenate((matrix1_arr.reshape(1, 9), matrix2_arr.reshape(1, 9)), axis=0)
print(matrix1_matrix2_arr)