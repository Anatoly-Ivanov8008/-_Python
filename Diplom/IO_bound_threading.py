import threading  # Модуль для работы с потоками
import requests  # Синхронная библиотека для HTTP-запросов
import time  # Для измерения времени выполнения
import psutil  # Для мониторинга системных ресурсов

""""
Реализация IO-bound задачи.
Задача: 
Выполнение 500 HTTP-запросов к тестовому API (https://httpbin.org/delay/1),
возвращающему ответ с задержкой в 1 секунду.
Реализация представлена с использованием модуля threading.
"""

# Общий счетчик успешных запросов
success_counter = 0
lock = threading.Lock()  # Блокировка для синхронизации доступа к счетчику


# Функция для выполнения одного HTTP-запроса
def fetch(url):
    global success_counter  # Используем глобальный счетчик
    try:
        response = requests.get(url)  # Выполняем синхронный GET-запрос
        with lock:  # Гарантируем безопасный доступ к счетчику
            success_counter += 1  # Увеличиваем счетчик успешных запросов
    except Exception as e:
        print(f"Ошибка запроса: {e}")  # Логируем ошибку


# Основная функция для запуска задач в потоках
def main_io_bound():
    global success_counter  # Используем глобальный счетчик
    url = "https://httpbin.org/delay/1"  # Тестовый URL с задержкой 1 секунда
    num_requests = 500  # Количество запросов
    threads = []  # Список для хранения потоков

    # Замер времени выполнения
    start_time = time.time()  # Засекаем начальное время

    # Создаем и запускаем 100 потоков
    for _ in range(num_requests):
        thread = threading.Thread(target=fetch, args=(url,))  # Создаем поток
        threads.append(thread)  # Добавляем поток в список
        thread.start()  # Запускаем поток

    # Дожидаемся завершения всех потоков
    for thread in threads:
        thread.join()  # Блокируем основной поток до завершения текущего

    end_time = time.time()  # Засекаем конечное время выполнения

    # Вывод результатов
    print(f"Отправлено запросов: {num_requests}")
    print(f"Успешных ответов: {success_counter}")
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
