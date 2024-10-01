""""
Модуль 11 задание 3
Домашнее задание по теме "Интроспекция"
Задача
"""""
from pprint import pprint


class May:
    def __init__(self):
        self.a = 5
        self.b = 10
        self.c = 4


def introspection_info(obj):
    _type = type(obj)
    _modul = type(obj).__module__
    _attr = []
    _method = []
    _id = id(obj)
    for i in dir(obj):
        if callable(getattr(obj, i)):
            _method.append(i)
        else:
            _attr.append(i)
    result = {'module': _modul,
              'type': _type,
              'attributes': _attr,
              'methods': _method,
              'id in memory': _id}
    return result


number_info = introspection_info(43)
trum = May()
class_info = introspection_info(trum)
pprint(number_info)
pprint(class_info)