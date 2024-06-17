# Модуль 3 задача 3
print('Задача "Рекурсивное умножение цифр":\n')


def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) <= 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))


numbers = input('Введите целое число:\n')
print('Произведение цифр числа', str(numbers), 'равно: \n', get_multiplied_digits(numbers))
