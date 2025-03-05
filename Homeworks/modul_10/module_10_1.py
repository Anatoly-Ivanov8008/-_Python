""""
Модуль 10 задание 1
Домашнее задание по теме "Создание потоков".
Задача "Потоковая запись в файлы"
"""""

from datetime import datetime
from threading import Thread
from time import sleep


def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл  {file_name}')


time_start_func = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
time_end_func = datetime.now()
time_res_func = time_end_func - time_start_func
print(f'Функции отработали за {time_res_func}')

thread_1 = Thread(target=wite_words, args=(10, 'example5.txt'))
thread_2 = Thread(target=wite_words, args=(30, 'example6.txt'))
thread_3 = Thread(target=wite_words, args=(200, 'example7.txt'))
thread_4 = Thread(target=wite_words, args=(100, 'example8.txt'))

time_start_thread = datetime.now()
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

time_end_thread = datetime.now()
time_res_thread = time_end_thread - time_start_thread
print(f'Потоки завершили работу за {time_res_thread}')