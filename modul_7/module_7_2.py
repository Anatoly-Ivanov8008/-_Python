"""
Модуль 7 задание 2
Домашнее задание по теме "Позиционирование в файле".
Задача "Записать и запомнить"
"""

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    namber_str = 1
    strings_positions = {}
    for j in strings:
        begin_line = file.tell()
        key = (namber_str, begin_line)
        file.write(f'{j}\n')
        namber_str = namber_str + 1
        strings_positions[key] = j
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)