# def find_crater(array: np.ndarray, i: int, j: int) -> bool:
#     if i < 0 or i >= len(array):
#         return False
#     if j < 0 or j >= len(array):
#         return False
#     crater = array[i][j] == "1"
#     array[i][j] = "0"
#     if crater:
#         find_crater(array, i, j + 1)
#         find_crater(array, i, j - 1)
#         find_crater(array, i + 1, j)
#         find_crater(array, i - 1, j)
#     return crater
#
#
# def calculate(array: np.ndarray):
#     craters = 0
#     for i in range(len(array)):
#         for j in range(len(array[i])):
#             if find_crater(array, i, j):
#                 craters += 1
#     return craters

import numpy as np

basi_matrix =[
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

print(basi_matrix)
basic_matrix2 = [
    [1, 0],
    [1, 1]
]
matrix = basi_matrix

def unit_finder (matrix: list , x , y) -> True:
    if x < 0 or y < 0:
        return False
    a = matrix[x][y]
    if matrix[x][y] == 1:
        matrix[x][y] = 0
        try:

            unit_finder(matrix, x + 1, y) #down
            unit_finder(matrix, x - 1, y) #up
            unit_finder(matrix, x, y + 1) #right
            unit_finder(matrix, x, y - 1) #left
        except IndexError:
            pass

        return True


# def unit_finder (matrix: list , x , y) -> True:
#     if x < 0 or y < 0:
#         return False
#     a = matrix[x][y] == 1
#     matrix[x][y] = 0
#     if a:
#
#         try:
#
#             unit_finder(matrix, x + 1, y) #down
#             unit_finder(matrix, x - 1, y) #up
#             unit_finder(matrix, x, y + 1) #right
#             unit_finder(matrix, x, y - 1) #left
#         except IndexError:
#             return False
#
#     return True
#





def calculate(matrix: list ) -> int:
    counter = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            # unit_finder(matrix, x, y)
            if unit_finder(matrix, x, y):
                counter += 1
    return counter

print(calculate(basi_matrix))


