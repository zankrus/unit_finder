"""Файл с функциями для работы приложения."""


def matrix_from_file(file_path: str) -> list:
    """Функция для получения матрицы из файла."""
    array = []
    with open(file_path, 'r') as input_file:
        for line in input_file:
            array.append([int(x) for x in line.split()])
    return array


def unit_finder(matrix: list, x: int, y: int) -> True:
    """Функция через рекурсию ищет острова с единицами в матрице."""
    if x < 0 or y < 0:
        return False
    if matrix[x][y] == 1:
        matrix[x][y] = 0
        try:

            unit_finder(matrix, x + 1, y)  # down
            unit_finder(matrix, x - 1, y)  # up
            unit_finder(matrix, x, y + 1)  # right
            unit_finder(matrix, x, y - 1)  # left
        except IndexError:
            pass

        return True


def calculate(matrix: list) -> int:
    """Функция считает кол-во островов в матрице."""
    counter = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            # unit_finder(matrix, x, y)
            if unit_finder(matrix, x, y):
                counter += 1
    return counter
