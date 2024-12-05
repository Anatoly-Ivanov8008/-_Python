import multiprocessing  # Модуль для работы с процессами
import requests  # Синхронная библиотека для HTTP-запросов
import time  # Для измерения времени выполнения
import psutil  # Для мониторинга системных ресурсов

""""
Реализация IO-bound задачи.
Задача: 
Выполнение 500 HTTP-запросов к тестовому API (https://httpbin.org/delay/1),
возвращающему ответ с задержкой в 1 секунду.
Реализация представлена с использованием модуля multiprocessing.
"""

# Функция для выполнения одного HTTP-запроса
def fetch(url, success_counter):
    try:
        response = requests.get(url)  # Выполняем синхронный GET-запрос
        success_counter["success"] += 1  # Увеличиваем счетчик успешных запросов
    except Exception as e:
        print(f"Ошибка запроса: {e}")  # Логируем ошибку


# Основная функция для запуска задач в процессах
def main_io_bound():
    url = "https://httpbin.org/delay/1"  # Тестовый URL с задержкой 1 секунда
    num_requests = 500  # Количество запросов
    processes = []  # Список для хранения процессов
    success_counter = multiprocessing.Manager().dict()  # Общий словарь для подсчета успешных запросов
    success_counter["success"] = 0  # Инициализируем счетчик успешных запросов

    # Замер времени выполнения
    start_time = time.time()  # Засекаем начальное время

    # Создаем и запускаем 100 процессов
    for _ in range(num_requests):
        process = multiprocessing.Process(target=fetch, args=(url, success_counter))  # Создаем процесс
        processes.append(process)  # Добавляем процесс в список
        process.start()  # Запускаем процесс

    # Дожидаемся завершения всех процессов
    for process in processes:
        process.join()  # Блокируем основной процесс до завершения текущего

    end_time = time.time()  # Засекаем конечное время выполнения

    # Вывод результатов
    print(f"Отправлено запросов: {num_requests}")
    print(f"Успешных ответов: {success_counter['success']}")
    print(f"Время выполнения: {end_time - start_time:.2f} секунд")

    # Получение загрузки CPU
    cpu_usage = psutil.cpu_percent(interval=1)  # Измеряем загрузку CPU за 1 секунду
    print(f"Загрузка CPU: {cpu_usage}%")

    # Получение информации о памяти
    memory_info = psutil.virtual_memory()
    print(f"Использовано памяти: {memory_info.used / (1024 ** 2):.2f} МБ")
    print(f"Свободно памяти: {memory_info.available / (1024 ** 2):.2f} МБ")


if __name__ == "__main__":
    main_io_bound()  # Запускаем основную функцию
