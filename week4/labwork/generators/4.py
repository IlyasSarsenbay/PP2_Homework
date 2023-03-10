from math import sqrt, ceil
def sq(start, stop):
    for i in range(start, stop+1):
        sqrti = sqrt(i)
        if sqrti == ceil(sqrti):
            yield i

a=int(input())
b=int(input())
for i in sq(a,b):
    print(i)