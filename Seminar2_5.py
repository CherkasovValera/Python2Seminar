# 2   Реализуйте алгоритм перемешивания списка.

a = [18,86,'wef','git','fet','ddr','sssr','data',65,'<->','wilo',101,'rem',73]
b = []
i=0
print(*a)
while i<10:
    d=a[i]
    a[i]=a[i+4]
    a[i+4]=d
    b.append(a[i])
    i+=1
print(*a,end='\n')