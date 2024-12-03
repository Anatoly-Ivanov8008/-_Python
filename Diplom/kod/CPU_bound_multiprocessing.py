import multiprocessing  # Модуль для работы с процессами
import math  # Для вычисления факториала
import psutil  # Для мониторинга системных ресурсов
import time  # Для измерения времени выполнения


# Функция для вычисления факториала числа
def calculate_factorial(n):
    return math.factorial(n)  # Вычисляем факториал числа n


# Задача для выполнения в процессе
def process_task(n):
    result = calculate_factorial(n)  # Вычисляем факториал
    # print(result)  # Выводим результат


# Основная функция для запуска процессов
def main_cpu_bound():
    n = 200  # Число, для которого будет вычисляться факториал
    processes = []  # Список для хранения процессов

    # Замер времени выполнения
    start_time = time.time()  # Засекаем начальное время

    # Создаем и запускаем 1000 процессов
    for _ in range(1000):
        process = multiprocessing.Process(target=process_task, args=(n,))  # Создаем процесс для задачи
        processes.append(process)  # Добавляем процесс в список
        process.start()  # Запускаем процесс

    # Дожидаемся завершения всех процессов
    for process in processes:
        process.join()  # Ожидаем завершения процесса

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
