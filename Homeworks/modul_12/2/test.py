""""
Модуль 12 задание 2
Домашнее задание по теме "Методы Юнит-тестирования"
Задача
"""""

import module_12_2
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = module_12_2.Runner('Усэйн', 10)
        self.runner2 = module_12_2.Runner('Андрей', 9)
        self.runner3 = module_12_2.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        result = {}
        for j in cls.all_results:
            for i in cls.all_results[j]:
                result[i] = cls.all_results[j][i].name
            print(f'{j} {result}')

    def test_tournament1(self):
        self.distants1 = module_12_2.Tournament(90, self.runner1, self.runner3)
        self.all_results['1 тест'] = self.distants1.start()
        self.assertTrue(self.all_results['1 тест'][2].name == 'Ник')

    def test_tournament2(self):
        self.distants2 = module_12_2.Tournament(90, self.runner2, self.runner3)
        self.all_results['2 тест'] = self.distants2.start()
        self.assertTrue(self.all_results['2 тест'][2].name == 'Ник')

    def test_tournament3(self):
        self.distants3 = module_12_2.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results['3 тест'] = self.distants3.start()
        self.assertTrue(self.all_results['3 тест'][3].name == 'Ник')
