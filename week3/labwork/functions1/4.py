def filter_prime(num, n=2):
  if n >= num: 
      return True
  if num % n == 0:
      return False
  return filter_prime(num, n+1)


list=[]
a=int(input())
for x in range(a):
    c=int(input())
    list.append(c)
for b in list:
    if b!=0 and b!=1 and filter_prime(b)==True:
        print(b)