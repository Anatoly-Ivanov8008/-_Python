""""
Модуль 10 задание 5
Домашнее задание по теме "Многопроцессное программирование"
Задача "Многопроцессное считывание"
"""""

import time
from multiprocessing import Pool


# Функция для чтения данных из файла
def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())


file_names = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']


# Линейное выполнение
def linear_execution():
    start_time = time.time()
    for file in file_names:
        read_info(file)
    end_time = time.time()
    print(f"Линейное выполнение заняло: {end_time - start_time} секунд")


# Многопроцессное выполнение
def parallel_execution():
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, file_names)
    end_time = time.time()
    print(f"Многопроцессное выполнение заняло: {end_time - start_time} секунд")


if __name__ == '__main__':
    # Раскомментируйте нужный метод выполнения

    # Линейное выполнение
    # linear_execution()

    # Многопроцессное выполнение
    parallel_execution()
