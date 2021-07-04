input_time_in_sec = int(input('Введите время в секундах: '))
seconds = input_time_in_sec % 60
hours = input_time_in_sec // 3600
minutes = input_time_in_sec // 60 - hours * 60


print('{0:02}:{1:02}:{2:02}'.format(hours, minutes, seconds))


