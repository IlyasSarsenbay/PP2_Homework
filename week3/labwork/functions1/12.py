def h(num ):
    for x in num:
        o = ''
        t = x
        while( t > 0 ):
          o += '*'
          t= t - 1
        print(o)
list=[]
a=int(input())
for x in range(a):
    b=int(input())
    list.append(b)
h(list)