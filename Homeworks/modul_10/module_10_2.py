""""
Модуль 10 задание 2
Домашнее задание по теме "Потоки на классах"
Задача "За честь и отвагу!"
"""""

from threading import Thread
from time import sleep


class Knight(Thread):
    enemy = 100
    days = 0

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!"')
        while self.enemy != 0:
            self.days += 1
            self.enemy = self.enemy - self.power
            print(f'{self.name} сражается {self.days} дней(дня), осталось {self.enemy} воинов.\n')
            sleep(1)
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
