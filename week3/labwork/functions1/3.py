def solve(numheads, numlegs):
    for x in range(numheads + 1):
        y = numheads - x
        if 2 * x + 4 * y == numlegs:
            return x,y
a = int(input())
b = int(input())
print(solve(a,b))