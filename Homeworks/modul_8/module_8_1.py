""""
Модуль 8 задание 1
Домашнее задание по теме "Try и Except".
Задание "Программистам всё можно"
"""""


def add_everything_up(a, b):
    try:
        c = a + b
        return c
    except TypeError:
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
