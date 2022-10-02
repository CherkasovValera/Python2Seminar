
#     Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#     Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
number_str = int (input('Введите целое положительное число не равное нулю:  '))
number_pr=1
print('[',end=" ")
for i in range(number_str):
    number_pr=number_pr*(i+1)
    print(f'{number_pr},', end=" ")
print("]",end=" (")
list, number_f=[], number_str
for k in range(number_f):
    count=0
    n=len(list)+1
    for x in range(n):
        if number_f==1:
           print(f'{number_f})', end="")
           break
        while count<x+1:
            list.append(x+1)
            count+=1
            # if len(list)==number_str:
            #     break
        
print(*list)





