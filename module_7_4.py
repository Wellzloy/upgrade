team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

print('В команде Мастера кода участников: %s !' % team1_num)
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))
print('Команда Волшебники данных решила задач: {0} !'.format(score_2))
print('Команда Волшебники данных решила задач за: {0} с!'.format(team1_time))
print(f'Команды решили: {score_1} и {score_2}')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
challenge_result = result
print(f'Результат битвы: {challenge_result}')
tasks_total = score_1 + score_2
time_avg = team1_time + team2_time
print(f'Сегодня было решено {tasks_total} задач, '
      f'в среднем по {format(time_avg / score_1 + score_2, '.2f')} секунды на задачу!')
