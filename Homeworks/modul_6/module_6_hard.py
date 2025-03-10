""""
Модуль 6 Дополнительное практическое задание
Дополнительное практическое задание по модулю: "Наследование классов."
Задание "Они все так похожи"
"""
from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, __color, *__sides):
        if self.__is_valid_color(*__color):
            self.set_color(*__color)
        else:
            self.set_color(0, 0, 0)
        if self.__is_valid_sides(*__sides):
            self.set_sides(*__sides)
        else:
            self.set_sides(__sides * self.sides_count)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        for i in (r, g, b):
            if isinstance(i, int) and 0 <= i <= 255:
                new_color = True
            else:
                new_color = False
                break
        return new_color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *__sides):
        for i in __sides:
            if isinstance(i, int) and i > 0 and len(__sides) == self.sides_count:
                new_sides = True
            else:
                new_sides = False
                break
        return new_sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *__sides):
        super().__init__(__color, *__sides)
        self.__radius = self.__calculate_radius()

    def __calculate_radius(self):
        return self.get_sides()[0] / (2 * pi)

    def get_square(self):
        area_circle = pi * self.__radius ** 2
        return area_circle


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = self.__calculate_height()

    def __calculate_height(self):
        s = len(self) / 2
        return (s * (s - self.get_sides()[0]) * (s - self.get_sides()[1]) * (s - self.get_sides()[2])) ** 0.5

    def get_square(self):
        s = len(self) / 2
        return (s * (s - self.get_sides()[0]) * (s - self.get_sides()[1]) * (s - self.get_sides()[2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        sides = [sides[0]] * 12 if len(sides) == 1 else [1] * 12
        super().__init__(color, *sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


""""
Код для проверки
"""

circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
