x = input()
y = x.split()
a, b, c, d = [float(i) for i in y]
mx = d
if(a >= b and a >= c and a >= d):
    mx = a
elif (b >= a and b >= c and b >= d):
    mx = b
elif(c >= a and c >= b and c >= d):
    mx = c
mn = d
if(a <= b and a <= c and a <= d):
    mn = a
elif(b <= a and b <= c and b <= d):
    mn = b
elif(c <= a and c <= b and c <= d):
    mn = c
print(round((a+b+c+d-mn-mx)/2, 2))
