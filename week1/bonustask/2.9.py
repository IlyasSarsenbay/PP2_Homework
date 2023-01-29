x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
a=x2-x1
b=y2-y1
if x1==x2 or y1==y2 or abs(a)!=abs(b):
    print('NO')
else:
    print('YES')