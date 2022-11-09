def ema(t,p):
    if(t==p):
        total = 0
        for i in range(1,p+1):
            total += price[i]
        return total/p
    a = 2/(p+1)
    return a*price[t]+ema(t-1,p)*(1-a)

n = int(input())
cnt = 1
price = [float(0)]
out = []
for i in range(n):
    price += [float(e) for e in input().split(',')]
nowState = 0
oldState = 0
for i in range(14,n*7+1):
    fastEMA = ema(i,7)
    slowEMA = ema(i,14)
    if fastEMA==slowEMA:
        continue
    if(fastEMA<slowEMA):
        nowState = 1
    else:
        nowState = 2
    if(nowState!=oldState and oldState!=0):
        if(nowState == 1):
            out.append("SELL at "+str(price[i]))
        else:
            out.append("BUY at "+str(price[i]))
    oldState = nowState
if(len(out)):
    for e in out:
        print(e)
else:
    print("No results")

