a = float(input())
l = 0
u = a
x = l + (u - l) / 2
while (abs(a-10**x) > max(a, 10**x)/(10**10)):
    if 10**x > a:
        u = x
    else:
        l = x
    x = l + (u - l) / 2
print(round(x, 6))
