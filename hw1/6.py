a = int(input("Введите a: "))
b = int(input("Введите b: "))

day_num = 1
while a < b:
    a = a * 1.1
    day_num += 1
#    print(f"{day_num}-й день: {a:.2f}")
print(f"на {day_num} день спортсмен достиг результата - не менее {b} км")
