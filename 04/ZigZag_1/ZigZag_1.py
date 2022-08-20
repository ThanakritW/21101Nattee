x = int(input())
red = []
blue = []
for i in range(x):
    a, b = [int(e) for e in input().split()]
    if(i % 2 == 0):
        red.append(a)
        blue.append(b)
    else:
        red.append(b)
        blue.append(a)
y = input()
if y == 'Zig-Zag':
    mn = 1e19
    mx = -1e19
    for i in red:
        if i < mn:
            mn = i
    for i in blue:
        if i > mx:
            mx = i
else:
    mn = 1e19
    mx = -1e19
    for i in blue:
        if i < mn:
            mn = i
    for i in red:
        if i > mx:
            mx = i
print(mn, mx)
