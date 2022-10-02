#     Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите 
# на экран их сумму.
#     Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
posled_str = int (input('Введите целое положительное число n не равное нулю:  '))
import math
posled_sum=0
print(f'[ n = {posled_str}:',end=" ")
for i in range(posled_str):
    number_pr=round((1+(1/(i+1)))**(i+1))
    n=math.trunc(number_pr)
    posled_sum=posled_sum+n
    print(i+1, ':', n,',', end=" ")
print(f'] (',(posled_sum), end=" )")







