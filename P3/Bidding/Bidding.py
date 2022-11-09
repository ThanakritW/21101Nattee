q = int(input())

log = dict()
bidder = set()
ans = dict()
total = dict()

for i in range(q):
    cmd = input().split()
    if(not cmd[2] in log):
        log[cmd[2]] = list()
    if(cmd[0]=='B'):
        log[cmd[2]].append(tuple((cmd[0],cmd[1],cmd[3])))
        bidder.add(cmd[1])
    elif(cmd[0]=='W'):
        log[cmd[2]].append(tuple((cmd[0],cmd[1])))
        bidder.add(cmd[1])

bidder = sorted(bidder)
for e in bidder:
    ans[e] = list()
    total[e] = 0

for k in log:
    res = dict()
    time = dict()
    for i in bidder:
        res[i] = time[i] = 0
    for i in range(len(log[k])):
        cmd = log[k][i]
        if(cmd[0]=='B'):
            res[cmd[1]] = int(cmd[2])
            time[cmd[1]] = i
        else:
            res[cmd[1]] = 0
    mx = 0
    time_mx = -1
    winner = ''
    for e in res:
        if(mx == res[e] and time_mx > time[e]):
            winner = e
            timer_mx = time[e]
        elif(mx < res[e]):
            mx = res[e]
            winner = e
            time_mx = time[e]
    if(mx!=0):
        ans[winner].append(k)
        total[winner]+=mx
for e in bidder:
    print(e,': $',sep='',end='')
    if(total[e]==0):
        print(0)
    else:
        print(total[e],' -> ',sep='',end='')
        ans[e]=sorted(ans[e])
        for i in ans[e]:
            print(i,end=' ')
        print('')
