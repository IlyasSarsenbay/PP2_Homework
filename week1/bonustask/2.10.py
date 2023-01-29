x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1!=x2 and y1!=y2) and abs(x1 - x2) != abs(y1 - y2):
    print('NO')
else:
    print('YES')