bd = int(input())
bm = int(input())
by = int(input())-543
td = int(input())
tm = int(input())
ty = int(input())-543
bcheck = False
tcheck = False
if(by % 4 == 0):
    if(by % 100 == 0):
        if(by % 400 == 0):
            check = True
    else:
        check = True
if(ty % 4 == 0):
    if(ty % 100 == 0):
        if(ty % 400 == 0):
            check = True
    else:
        check = True
dim = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ds = dim[bm-1]-bd
if(bm >= 2 and bcheck):
    ds += 1
while(bm < 12):
    ds += dim[bm]
    bm += 1
dt = td
if(tm >= 3 and tcheck):
    dt += 1
while(tm-1 >= 0):
    dt += dim[tm-1]
    tm -= 1
