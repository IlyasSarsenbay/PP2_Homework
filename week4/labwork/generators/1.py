def squares(n):
    a=1
    while a<=n:
        yield a*a
        a+=1
 
n=int(input())
for i in squares(n):
    print(i)

