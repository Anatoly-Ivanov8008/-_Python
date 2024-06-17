# Задача "Распаковка":
print('1. Функция с параметрами по умолчанию: \n')
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(6)
print_params(8, 10)
print_params(7, 9 ,3)
print_params(b=25)
print_params(c=[1, 2, 3])

print('\n2. Распаковка параметров: \n')
values_list = [76, 'string', False]
values_dict = {'a': 43, 'b': 'string', 'c': False}
print_params(*values_list)
print_params(**values_dict)

print('\n3.Распаковка + отдельные параметры: \n')
values_list_2 = [54.32, 'string']
print_params(*values_list_2, 42)
