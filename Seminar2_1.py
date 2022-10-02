

#     Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#     Пример:
# - 6782 -> 23
# - 0,56 -> 11

print("Введите число:")
a = input()
b = a.replace(".", "", 1)
num = [b]
sum_all=0
n=len(b)
for i in range(n):
    sum_all=int(sum_all)+int(b[i])
print(f'{a} -> {sum_all}')



