"""
Модуль 5 задача 4
Домашняя работа по уроку "Различие атрибутов класса и экземпляра."
Задача "История строительства"
"""
class House:
    houses_history = []

    def __new__(cls, name, number_of_floors):
        cls.houses_history.append(name)
        return name

    def __del__(self):
        print(f'{str(self)} снесён, но он останется в истории')
        # House.houses_history.remove(self)   если необходимо будет удалить запись об объекте

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

    def __eq__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(self.number_of_floors, int):
            a = self.number_of_floors + value
            return House(self.name, a)

    def __radd__(self, value):
        if isinstance(value, int):
            a = value + self.number_of_floors
            return House(self.name, a)

    def __iadd__(self, value):
        if isinstance(self.number_of_floors, int):
            self.number_of_floors += value
            return House(self.name, self.number_of_floors)


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
House.__del__(h2)
House.__del__(h3)
print(House.houses_history)
