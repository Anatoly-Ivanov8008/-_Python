""""
Модуль 12 задание 1
Домашнее задание по теме "Простые Юнит-Тесты"
Задача "Проверка на выносливость"
"""""


import module_12_1
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test1 = module_12_1.Runner('test1')
        for i in range(1, 11):
            test1.walk()
        self.assertEqual(test1.distance, 50)

    def test_run(self):
        test2 = module_12_1.Runner('test2')
        for i in range(1, 11):
            test2.run()
        self.assertEqual(test2.distance, 100)

    def test_challenge(self):
        test3 = module_12_1.Runner('test3')
        test4 = module_12_1.Runner('test4')
        for i in range(1, 11):
            test3.run()
            test4.walk()
        self.assertNotEqual(test4.distance, test3.distance)
