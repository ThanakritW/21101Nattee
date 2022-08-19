import math
info = input()
sinfo = info.split()
bd, bm, by, td, tm, ty = [int(i) for i in sinfo]
by -= 543
ty -= 543
bcheck = False
tcheck = False
if(by % 4 == 0):
    if(by % 100 == 0):
        if(by % 400 == 0):
            bcheck = True
    else:
        bcheck = True
if(ty % 4 == 0):
    if(ty % 100 == 0):
        if(ty % 400 == 0):
            tcheck = True
    else:
        tcheck = True
dim = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ds = dim[bm-1]-bd
if(bm <= 2 and bcheck):
    ds += 1
while(bm < 12):
    ds += dim[bm]
    bm += 1
dt = td
if(tm >= 3 and tcheck):
    dt += 1
while(tm-2 >= 0):
    dt += dim[tm-2]
    tm -= 1
totalDay = ds+dt+max(0, (ty-by-1))*365
print(totalDay, "{:.2f}".format(round(math.sin(2*math.pi*totalDay/23), 2)), "{:.2f}".format(round(math.sin(2 *
      math.pi*totalDay/28), 2)), "{:.2f}".format(round(math.sin(2*math.pi*totalDay/33), 2)))
