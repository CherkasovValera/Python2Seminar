#     Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите 
# на экран их сумму.
#     Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
posled_str = int (input('Введите целое положительное число не равное нулю:  '))
import math
posled_sum=0
print('[',end=" ")
for i in range(posled_str):
    number_pr=round((1+(1/(i+1)))**(i+1))
    n=math.trunc(number_pr)
    posled_sum=posled_sum+n
    print(f'{(n)},', end=" ")
print(f'] (',(posled_sum), end=" )")
# list, number_f=[], number_str
# for k in range(number_f):
#     count=0
#     n=len(list)+1
#     for x in range(n):
#         if number_f==1:
#            print(f'{number_f})', end="")
#            break
#         while count<x+1:
#             list.append(x+1)
#             count+=1







# 1    Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt 
# в одной строке одно число.
# 2   Реализуйте алгоритм перемешивания списка.
