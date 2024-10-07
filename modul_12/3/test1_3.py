import module_12_1_3
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test1 = module_12_1_3.Runner('test1')
        for i in range(1, 11):
            test1.walk()
        self.assertEqual(test1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test2 = module_12_1_3.Runner('test2')
        for i in range(1, 11):
            test2.run()
        self.assertEqual(test2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test3 = module_12_1_3.Runner('test3')
        test4 = module_12_1_3.Runner('test4')
        for i in range(1, 11):
            test3.run()
            test4.walk()
        self.assertNotEqual(test4.distance, test3.distance)
