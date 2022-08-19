x = input()
x = x.split()
a, b, c, d = [int(i) for i in x]
if a > b:
    temp = a
    a = b
    b = temp
    if(d >= a):
        if(c > d):
            c = c-a
    else:
        c = c+a
    b = a+c+d
else:
    if(c > a and a >= b):
        d = d + a
    if(d > c):
        b += 2
    else:
        b *= 2
print(a, b, c, d)
