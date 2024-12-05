
# Дипломная работа




## тема: Сравнение различных подходов к реализации асинхронного программирования: asyncio, threading и multiprocessing.

## задача: Реализовать асинхронные задачи с использованием asyncio, threading и multiprocessing, сравнить их производительность и уместность для различных типов задач.
### Автор: Иванов Анатолий Леонидович

## Описание проекта:

### Этот проект посвящен сравнению производительности и применимости трёх подходов к реализации асинхронного программирования в Python:

* asyncio
* threading
* multiprocessing.
  
## Рассматриваются два типа задач:

* IO-bound — задачи, связанные с вводом-выводом, например, выполнение HTTP-запросов.

* CPU-bound — вычислительно интенсивные задачи, такие как вычисление факториалов.

## Проект включает:

* Исследование теоретических аспектов каждого подхода.

* Реализацию задач с использованием модулей asyncio, threading и multiprocessing.

* Сравнение их производительности на основе времени выполнения, загрузки CPU и использования памяти.

## Структура проекта:
```python
├── Diplom_project.docx           # Дипломная работа
├── README.md                     # Описание проекта
├── requirements.txt              # Список зависимостей
├── CPU_bound_asyncio.py          # CPU-bound задача с использованием asyncio
├── CPU_bound_threading.py        # CPU-bound задача с использованием threading
├── CPU_bound_multiprocessing.py  # CPU-bound задача с использованием multiprocessing
├── IO_bound_asyncio.py           # IO-bound задача с использованием asyncio
├── IO_bound_threading.py         # IO-bound задача с использованием threading
├── IO_bound_multiprocessing.py   # IO-bound задача с использованием multiprocessing
```

## Требования:
Для запуска кода вам потребуется Python версии 3.9+ и следующие библиотеки:

* aiohttp
* requests
* psutil
  
#### Установить зависимости можно с помощью команды:
```python
pip install -r requirements.txt
```
## Как запустить примеры:
### IO-bound задача (HTTP-запросы)
#### Asyncio
Файл: io_bound_asyncio.py
```python
python IO_bound_asyncio.py
```

