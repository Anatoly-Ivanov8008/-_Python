"""
Модуль 7 задание 3
Домашнее задание по теме "Оператор "with".
Задача "Найдёт везде"
"""


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                text = file.read()
                text = text.replace("\n", " ")
                exception = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for j in exception:
                    text = text.replace(j, "")
                text = text.lower()
                words = text.split()
            all_words[i] = words
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        results = {}
        for keys, words in all_words.items():
            position = words.index(word)
            results[keys] = position + 1
        return results

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        results = {}
        for keys, words in all_words.items():
            results[keys] = words.count(word)
        return results


finder1 = WordsFinder('test_file.txt')
print(finder1.get_all_words()) # Все слова
print(finder1.find('TEXT'))
print(finder1.count('teXT'))
'''
Поиск во всех стихотворениях
'''
finder2 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder2.get_all_words())
print(finder2.find('the'))
print(finder2.count('the'))