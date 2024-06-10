def get_matrix(n, m, value):
    matrix1 = []
    for i in range(n):
        matrix2 = []   # Создаем буферный список
        for j in range(m):
            matrix2.insert(j, value)
        matrix1.append(matrix2)
    return matrix1

n = int(input('Введите количество строк: '))
m = int(input('Введите колчество столбцов: '))
value = int(input('Введите значение: '))
print(get_matrix(n, m, value))