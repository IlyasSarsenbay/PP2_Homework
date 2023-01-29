a=int(input())
b=int(input())
c=int(input())
if a==b and a!=c:
    print(2)
if b==c and a!=c:
    print(2)
if a==b and b==c:
    print(3)
if a!=b and b!=c and a!=c:
    print(0)
if a==c and b!=c:
    print(2)