import asyncio  # Библиотека для асинхронного программирования
import math  # Для вычисления факториала
import psutil  # Для мониторинга системных ресурсов
import time  # Для измерения времени выполнения

""""
Реализация CPU-bound задачи.
Задача: 
Выполнение 1000 вычислений факториала числа 200000, требующих интенсивного использования процессора.
Реализация представлена с использованием модуля asyncio.
"""

# Функция для вычисления факториала числа
def calculate_factorial(n):
    return math.factorial(n)  # Используем встроенную функцию для вычисления факториала


# Асинхронная обертка для вычисления факториала
async def async_factorial(n):
    return calculate_factorial(n)  # Синхронное вычисление в асинхронной обертке


# Основная корутина для выполнения всех задач
async def main_cpu_bound():
    n = 200000  # Число, для которого будет вычисляться факториал
    tasks = [async_factorial(n) for _ in range(1000)]  # Создаем 1000 задач для вычисления факториала

    # Замер времени выполнения
    start_time = time.time()  # Засекаем начальное время выполнения
    results = await asyncio.gather(*tasks)  # Асинхронно выполняем все задачи
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
    asyncio.run(main_cpu_bound())  # Запуск событийного цикла

