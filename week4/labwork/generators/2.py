def even(n):
    a=1
    while a<n:
        yield a+1 
        a+=2

n=int(input())
for i in even(n):
    print(i,end=", ")