""""
Модуль 7 задание 5
Домашнее задание по теме "Файлы в операционной системе".
"""""

import os
import time

directory = '.'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(directory, file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(os.path.abspath(file))
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')
