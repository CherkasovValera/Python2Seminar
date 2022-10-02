

#     Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#     Пример:
# - 6782 -> 23
# - 0,56 -> 11

print("Введите число:")
a = input()
b = a.replace(".", "", 1)
num = [b]
sum_all=0
for i in range(len(b)):
    sum_all=int(sum_all)+int(b[i])
print(f'{a} -> {sum_all}')



