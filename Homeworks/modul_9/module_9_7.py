""""
Модуль 9 задание 7
Домашнее задание по теме "Декораторы"
Задание: Декораторы в Python
"""""


def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for i in range(2, int(result ** 0.5) + 1):
            if result % i == 0:
                print('Состовное')
                return result
        print('Простое')
        return result
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
