input_num = int(input('Введите целое положительное число:'))

max_num = 0
while input_num > 0:
    curr_num = input_num % 10
    input_num = input_num // 10
    if curr_num == 9:
        max_num = 9
        break
    elif max_num < curr_num:
        max_num = curr_num

print('Наибольшая цифра:', max_num)
