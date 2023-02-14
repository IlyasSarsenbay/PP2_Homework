def str(b, x, a): 
    if x==a: 
        print(''.join(b) )
    else: 
        for y in range(x,a): 
            b[x], b[y] = b[y], b[x] 
            str(b, x+1, a) 
            b[x], b[y] = b[y], b[x]
  

s = input()
a = len(s) 
b = list(s) 
str(b, 0, a)