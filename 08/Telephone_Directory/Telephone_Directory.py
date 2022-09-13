n = int(input())
dn = {}
dt = {}
for i in range(n):
    f, s, t = input().split()
    f += ' '+s
    dn[f] = t
    dt[t] = f
q = int(input())
for i in range(q):
    x = input()
    print(x+' --> ', end='')
    if(x in dn):
        print(dn[x])
    elif(x in dt):
        print(dt[x])
    else:
        print('Not found')
