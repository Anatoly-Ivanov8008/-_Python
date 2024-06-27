# Модуль № 3
# Домашняя работа по уроку "Пространство имён"
# Задача "Счётчик вызовов"
calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    tuple_return = (len(string), string.upper(), string.lower())
    count_calls()
    return tuple_return


def is_contains(string, list_to_search):
    return_param = False
    for i in list_to_search:
        if string.lower() in i.lower():
            return_param = True
            break
    count_calls()
    return return_param


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
