""""
Модуль 7 задание 4
Домашнее задание по теме "Форматирование строк".
"""""

team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

# использование %
print('В команде Мастера кода участников: %s' % team1_num)
print('Итого сегодня в командах участвуют: %s и %s' % (team1_num, team2_num))

# использование .format()
print('\nКоманда Волшебники данных решила задач: {}'.format(score2))
print('Волшебники данных решили задачи за {} c!'.format(team2_time))

# использование f''
print(f'\nКоманды решили {score1} и {score2} задач.')

if score1 > score2 or score1 == score2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

print(f'Результат битвы: {result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
