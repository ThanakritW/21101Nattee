from cmath import sqrt
import math
a = float(input())
b = float(input())
c = float(input())
x = 0 - b
y = ((b**2)-(4*a*c))**0.5
z = 2*a
# print(x, y, z)
print(round((x-y)/z, 3), end=' ')
print(round((x+y)/z, 3))
