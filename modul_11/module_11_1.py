""""
Модуль 11 задание 1
Домашнее задание по теме "Обзор сторонних библиотек Python"
Задача: познакомиться с использованием сторонних библиотек в Python и применить их в различных задачах.
"""""

import matplotlib.pyplot as plt
import numpy as np

# Создание данных для демонстрации некоторых возможностей matplotlib
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = y1 + y2

# Фигура и несколько подграфиков (1-я функция/класс: Figure и его методы)
fig, ax = plt.subplots(2, 2, figsize=(10, 6))

# 1. Линейный график (2-я функция/метод: plot)
ax[0, 0].plot(x, y1, label="sin(x)", color='b')
ax[0, 0].set_title('Sine Wave')
ax[0, 0].legend()

# 2. График с добавлением точек (scatter)
ax[0, 1].scatter(x, y2, color='r', label='cos(x)', alpha=0.6)
ax[0, 1].set_title('Cosine Points')
ax[0, 1].legend()

# 3. Гистограмма (hist)
ax[1, 0].hist(y3, bins=15, color='g', alpha=0.7)
ax[1, 0].set_title('Histogram of sin(x) + cos(x)')

# 4. Стиль сетки (3-я функция: grid)
ax[1, 1].plot(x, y3, label="sin(x) + cos(x)", color='purple', linestyle='--')
ax[1, 1].set_title('Sine + Cosine')
ax[1, 1].grid(True)
ax[1, 1].legend()

# Подписи осей и настройка
for i in range(2):
    for j in range(2):
        ax[i, j].set_xlabel('x-axis')
        ax[i, j].set_ylabel('y-axis')

plt.tight_layout()
plt.show()
