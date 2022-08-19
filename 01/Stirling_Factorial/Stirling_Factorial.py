import math
n = input()
n = int(n)
e = 2.718281828459045
pi = 3.141592653589793
print(pow((2*pi),1/2)*pow(n,n+1/2)*pow(e,-n+1/(12*n+1)))
print(pow((2*pi),1/2)*pow(n,n+1/2)*pow(e,-n+1/(12*n)))