def uni(num):
    list = []
    for i in num :
        if i not in list:
            list.append(i)
    return list
list=[]
a=int(input())
for x in range(a):
    b=int(input())
    list.append(b)

print(uni(list))