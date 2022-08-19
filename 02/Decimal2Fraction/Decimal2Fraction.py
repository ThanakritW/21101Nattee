import math
s = input()
a, b, c = s.split(',')
d = int(a+b+c)-int(a+b)
e = int((len(c)*'9') + (len(b)*'0'))
g = math.gcd(d, e)
d //= g
e //= g
print(d, '/', e)
