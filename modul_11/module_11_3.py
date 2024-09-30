""""
Модуль 11 задание 3
Домашнее задание по теме "Интроспекция"
Задача
"""""
from pprint import pprint

def introspection_info(obj):
    _type = type(obj)
    _dir = dir(obj)
    _id = id(obj)
    result = {'type' : _type,
              'attributes and methods' : _dir,
              'id in memory' : _id}
    return result

number_info = introspection_info(42)
pprint(number_info)

