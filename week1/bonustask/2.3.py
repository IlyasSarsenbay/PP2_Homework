a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a%2!=0 and c%2!=0:
    if (b%2!=0 and d%2!=0) or (b%2==0 and d%2==0):
        print("YES")
    if (b%2!=0 and d%2==0) or (b%2==0 and d%2!=0):
        print("NO")
if a%2==0 and c%2==0:
    if (b%2!=0 and d%2!=0) or (b%2==0 and d%2==0):
        print("YES")
    if (b%2!=0 and d%2==0) or (b%2==0 and d%2!=0):
        print("NO")
if a%2!=0 and c%2==0:
      if (b%2!=0 and d%2!=0) or (b%2==0 and d%2==0):
        print("NO")
      if (b%2!=0 and d%2==0) or (b%2==0 and d%2!=0):
        print("YES")
if a%2==0 and c%2!=0:
      if (b%2!=0 and d%2!=0) or (b%2==0 and d%2==0):
        print("NO")
      if (b%2!=0 and d%2==0) or (b%2==0 and d%2!=0):
        print("YES")