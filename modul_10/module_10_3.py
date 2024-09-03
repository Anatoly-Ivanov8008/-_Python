""""
Модуль 10 задание 3
Домашнее задание по теме "Блокировки и обработка ошибок"
Задача "Банковские операции"
"""""

from random import randint
from time import sleep
import threading

lock = threading.Lock()
balanc = 0


class Bank():

    def deposit(self):
        global lock
        global balanc
        for i in range(100):
            rand = randint(50, 500)
            balanc = balanc + rand
            if balanc > 500 and lock.acquire():
                lock.release()
            print(f'\nПополнение: {rand}. Баланс: {balanc}')
            sleep(0.09)

    def take(self):
        global lock
        global balanc
        for i in range(100):
            rand = randint(50, 500)
            print(f'Запрос на выдачу средств {rand}')
            if rand <= balanc:
                balanc = balanc - rand
                sleep(0.09)
                print(f'\nСнятие: {rand}. Баланс: {balanc}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                lock.acquire()


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {balanc}')
