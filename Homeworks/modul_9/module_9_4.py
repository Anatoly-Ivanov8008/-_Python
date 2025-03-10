""""
Модуль 9 задание 4
Домашнее задание по теме "Создание функций на лету"
Задача "Функциональное разнообразие"
"""""
'''
Lambda-функция:
'''

first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y: x == y, first, second))
print(result)

'''
Замыкание:
'''


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for text in data_set:
                file.write(f'{text}\n')
        file.close()

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'], 'и объекты', 'можете', 'использовать свои')

'''
Метод __call__:
'''
from random import choice


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Передаваемые', 'данные в функции', 'и объекты', 'можете использовать свои')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())