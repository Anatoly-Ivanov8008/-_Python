""""
Модуль 12 задание 1
Домашнее задание по теме "Простые Юнит-Тесты"
Задача "Проверка на выносливость"
"""""


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

