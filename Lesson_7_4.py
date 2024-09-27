team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

#Использование %:
print("В команде Мастера кода участников: %s " % team1_num)
print( "Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))

#Использование format():
print("Команда Волшебники данных решила задач: {}".format(score_2))
print("Волшебники данных решили задачи за {time}".format(time=team2_time))

#Использование f-строк:
print(f"Команды решили {score_1} и {score_2} задачи.")
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено {score_1+score_2} задач, в среднем по {(team1_time+team2_time)/tasks_total} секунды на задачу!.")

