import sys

total = int(input('Введите значение выручки фирмы: '))
costs = int(input('Введите издержки фирмы: '))

if total <= costs:
    print('Ваша фирма работает в убыток')
    sys.exit()

print('Ваша фирма работает с прибылью')
profit = total - costs
print('Ваша фирма работает с рентабельностью:', profit / total * 100)

persons = int(input('Введите количество сотрудников '))
print('Значение прибыли в расчете на одного сотрудника:', profit / persons)
