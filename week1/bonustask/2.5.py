a=int(input())
b=int(input())
c=int(input())
if a>b:
    if a>c and b>c:
        print(c)
    if a>c and c>b:
        print(b)
    if a<c:
        print(b)
    if b==c:
        print(b)
    if a==c:
        print(a)
elif b>a:
    if b>c and a>c:
        print(c)
    if b>c and c>a:
        print(a)
    if b<c:
        print(a)
    if a==c:
        print(a)
    if b==c:
        print(a)
elif a==b and b==c and a==c:
    print(a)
elif a==b and a<c:
    print(a)