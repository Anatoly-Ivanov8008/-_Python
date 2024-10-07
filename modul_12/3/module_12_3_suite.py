""""
Модуль 12 задание 3
Домашнее задание по теме "Систематизация и пропуск тестов".
Задача "Заморозка кейсов"
"""""


import unittest
import test1_3
import test2_3

suite_tests = unittest.TestSuite()
suite_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(test1_3.RunnerTest))
suite_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(test2_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite_tests)

""""
В test1_3, test2_3 использованы декораторы для пропуска тестов:
 @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
"""""