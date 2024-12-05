import asyncio  # Модуль для асинхронного программирования
import aiohttp  # Библиотека для асинхронных HTTP-запросов
import psutil  # Для мониторинга системных ресурсов
import time  # Для измерения времени выполнения

""""
Реализация IO-bound задачи.
Задача: 
Выполнение 500 HTTP-запросов к тестовому API (https://httpbin.org/delay/1),
возвращающему ответ с задержкой в 1 секунду.
Реализация представлена с использованием модуля asyncio.
"""

# Асинхронная функция для выполнения одного HTTP-запроса
async def fetch(url, success_counter):
    async with aiohttp.ClientSession() as session:  # Создаем асинхронную HTTP-сессию
        try:
            async with session.get(url) as response:  # Выполняем GET-запрос
                await response.text()  # Асинхронно считываем ответ (для проверки успешного получения)
                success_counter["success"] += 1  # Увеличиваем счетчик успешных запросов
        except Exception as e:
            print(f"Ошибка запроса: {e}")  # Логируем ошибки


# Основная корутина для выполнения всех запросов
async def main_io_bound():
    url = "https://httpbin.org/delay/1"  # Тестовый URL с задержкой в 1 секунду
    num_requests = 500  # Количество запросов
    success_counter = {"success": 0}  # Счетчик успешных запросов

    # Замер времени выполнения
    start_time = time.time()  # Засекаем начальное время

    # Создаем список задач
    tasks = [fetch(url, success_counter) for _ in range(num_requests)]

    # Асинхронно выполняем все задачи
    await asyncio.gather(*tasks)

    # Засекаем конечное время выполнения
    end_time = time.time()

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


# Запускаем основную корутину
if __name__ == "__main__":
    asyncio.run(main_io_bound())  # Запуск событийного цикла
