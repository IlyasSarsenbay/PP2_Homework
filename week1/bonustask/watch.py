n =int(input())
if n>=1440*(n//1440):
    print((n-1440*(n//1440))//60)
    print(n%60)
else:
    print(n//60)
    print(n%60)