"""Основной файл для запуска приложения."""

from functions import calculate, matrix_from_file

if __name__ == '__main__':
    matrix = matrix_from_file('input_file.txt')
    print('Введена матрица')
    print(matrix)
    print('Количество кратеров : ' + str(calculate(matrix)))
