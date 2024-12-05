import threading  # Модуль для работы с потоками
import math  # Для вычисления факториала
import psutil  # Для мониторинга системных ресурсов
import time  # Для измерения времени выполнения

""""
Реализация CPU-bound задачи.
Задача: 
Выполнение 1000 вычислений факториала числа 200000, требующих интенсивного использования процессора.
Реализация представлена с использованием модуля threading.
"""

# Функция для вычисления факториала числа
def calculate_factorial(n):
    return math.factorial(n)  # Вычисляем факториал числа n


# Задача для выполнения в потоке
def thread_task(n):
    result = calculate_factorial(n)  # Вычисляем факториал


# Основная функция для запуска потоков
def main_cpu_bound():
    n = 200000  # Число, для которого будет вычисляться факториал
    threads = []  # Список для хранения потоков

    # Замер времени выполнения
    start_time = time.time()  # Засекаем начальное время

    # Создаем и запускаем 1000 потоков
    for _ in range(1000):
        thread = threading.Thread(target=thread_task, args=(n,))  # Создаем поток для задачи
        threads.append(thread)  # Добавляем поток в список
        thread.start()  # Запускаем поток

    # Дожидаемся завершения всех потоков
    for thread in threads:
        thread.join()  # Ожидаем завершения потока

    end_time = time.time()  # Засекаем конечное время выполнения

    # Вывод времени выполнения
    print(f"Время выполнения: {end_time - start_time:.2f} секунд")

    # Получение загрузки CPU
    cpu_usage = psutil.cpu_percent(interval=1)  # Измеряем загрузку CPU за 1 секунду
    print(f"Загрузка CPU: {cpu_usage}%")

    # Получение информации о памяти
    memory_info = psutil.virtual_memory()
    print(f"Использовано памяти: {memory_info.used / (1024 ** 2):.2f} МБ")
    print(f"Свободно памяти: {memory_info.available / (1024 ** 2):.2f} МБ")


if __name__ == "__main__":
    main_cpu_bound()  # Запуск основной функции
