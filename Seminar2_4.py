
# 1    Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt 
# в одной строке одно число.

a = int(input('Введите число не менее 3:  '))
list=[]
for r in range(-a, a+1):
    list.append(r)
p1=list[0]*list[2]*list[4]
print(list, end ='\n ')
print(list[0],'*',list[2],'*',list[4], '=', p1)

with open('file.txt','r') as data:
    data.write('0')
