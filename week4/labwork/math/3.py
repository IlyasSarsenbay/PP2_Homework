from math import tan, pi
a = int(input())
b = float(input())
c = a * (b** 2) / (4 * tan(pi / a))
print(int(c))