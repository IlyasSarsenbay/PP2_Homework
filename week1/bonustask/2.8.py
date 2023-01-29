x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
a=x2-x1
b=y2-y1
if abs(a)<=1 and abs(b)<=1:
    print('YES')
else:
    print('NO')