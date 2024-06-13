numbers = input('Введите число от 3 до 20: ')
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_2 = []
list_3 = []
for i in range(1, len(list_1)):
    for j in range(1, int(numbers)):
        if int(numbers) % (i + j) == 0:
            if f'{j} + {i}' in list_3 or i == j:
                continue
            else:
                list_3.append(f'{i} + {j}')
                list_2.extend([i, j])
print('Ваш пароль: \n', *list_2, sep='')
