""""
Модуль 12 задание 4
Домашнее задание по теме "Логирование"
Задача "Логирование бегунов"
"""""

import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            logging.info('"test_walk" выполнен успешно')
            test1 = Runner('Вося', -8)
            for i in range(1, 11):
                test1.walk()
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            logging.info('"test_run" выполнен успешно')
            test2 = Runner(34, 5)
            for i in range(1, 11):
                test2.run()
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


    def test_challenge(self):
        test3 = Runner('test3')
        test4 = Runner('test4')
        for i in range(1, 11):
            test3.run()
            test4.walk()
        self.assertNotEqual(test4.distance, test3.distance)

