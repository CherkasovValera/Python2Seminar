
# 1    Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt 
# в одной строке одно число.
numbers = [0,2,4]
data = open('file.txt','w')
data.write('0\n')
data.write('2\n')
data.write('4')
data.close()
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
a = int(input('Введите число не менее 3:  '))
list=[]
for r in range(-a, a+1):
    list.append(r)
p1=list[0]*list[2]*list[4]
print(list, end ='\n ')
print(list[0],'*',list[2],'*',list[4], '=', p1)

