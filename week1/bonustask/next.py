x=int(input())
txt="The next number for the number {} is {}."
tx1="The previous number for the number {} is {}."
print(txt.format(x,x+1))
print(tx1.format(x,x-1))