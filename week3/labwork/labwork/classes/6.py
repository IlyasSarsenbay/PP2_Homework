
lis=[]
a=int(input())
for x in range(a):
    c=int(input())
    lis.append(c)
for i in lis:
   pr = list(filter(lambda x: x == 2 or x % i==0, lis))

print(pr)
