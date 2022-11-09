log = list()
while(True):
    cmd = input().split()
    if(cmd[0] in "123"):
        break
    log.append(cmd)
if(cmd[0]=='1'):
    total = dict()
    for cmd in log:
        ota,bnk,cnt = cmd
        cnt = int(cnt)
        if(bnk in total):
            total[bnk] += cnt
        else:
            total[bnk] = cnt
    ans = sorted(((total[e],e) for e in total) ,reverse=True)

if(cmd[0]=='2'):
    total = dict()
    for cmd in log:
        ota,bnk,cnt = cmd
        if(bnk in total):
            total[bnk].add(ota)
        else:
            total[bnk] = set([ota])
    ans = sorted(((len(total[e]),e) for e in total) ,reverse=True)

if(cmd[0]=='3'):
    total = dict()
    otas = dict()
    for cmd in log:
        ota,bnk,cnt = cmd
        if(not bnk in total):
            total[bnk]=0
        if(not ota in otas):
            otas[ota] = dict()
        cnt = int(cnt)
        if(bnk in otas[ota]):
            otas[ota][bnk] += cnt
        else:
            otas[ota][bnk] = cnt
    for ota in otas:
        mx = 0
        name = ''
        bnks = sorted(otas[ota])
        for bnk in bnks:
            if(otas[ota][bnk] > mx):
                mx = otas[ota][bnk]
                name = bnk
        total[name]+=1
    ans = sorted(((total[e],e) for e in total) ,reverse=True)

for i in range(3):
    if(i):
        print(', ',end='')
    print(ans[i][1],end='')