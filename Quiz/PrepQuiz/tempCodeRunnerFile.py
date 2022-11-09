def rating(lv,score):
    return int(25*(lv+1)*(score/1e7))

n = int(input())

history = dict()
rates = dict()

for k in range(n):
    cmd = input()
    if(cmd == 'Rating'):
        ratings = sorted([rates[e] for e in rates],reverse=True)
        total = 0
        for i in range(min(5,len(ratings))):
            total += ratings[i]
        print(total)
        continue
    cmd = cmd.split(' | ')
    if(cmd[0]=='Play'):
        name,lv,score = cmd[1:]
        lv = int(lv)
        score = int(score)
        rate = rating(lv,score)
        if(not name in history):
            history[name] = (rate,lv,score)
            rates[name]=rate
        else:
            if rate > history[name][0]:
                history[name] = (rate,lv,score)
                rates[name]=rate
            if rate == history[name][0]:
                if lv > history[name][1]:
                    history[name] = (rate,lv,score)
                    rates[name]=rate
                if(lv == history[name][1] and score > history[name][2]):
                    history[name] = (rate,lv,score)
                    rates[name]=rate
    elif(cmd[0]=='Rating'):
        print(rates[cmd[1]])
    elif(cmd[0]=='Detail'):
        if(cmd[1] in history):
            print(cmd[1],history[cmd[1]][1],history[cmd[1]][2],history[cmd[1]][0],sep=' | ')
        else:
            print(cmd[1],": No play history",sep='')