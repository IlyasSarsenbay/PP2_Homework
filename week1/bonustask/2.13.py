n=int(input())
m=int(input())
x=int(input())
y=int(input())
if n>m:
    x1=m-x
    y1=n-y
    print(min(x,y,x1,y1))
elif m>n:
    x1=n-x
    y1=m-y
    print(min(x,y,x1,y1))