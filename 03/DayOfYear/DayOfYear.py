d = int(input())
m = int(input())
y = int(input())
y -= 543
check = False
if(y % 4 == 0):
    if(y % 100 == 0):
        if(y % 400 == 0):
            check = True
    else:
        check = True
dim = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
diy = d
for i in range(m-1):
    diy += dim[i]
if(check and m > 2):
    diy += 1
print(diy)
