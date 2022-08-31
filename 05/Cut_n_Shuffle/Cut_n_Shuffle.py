deck = input().split()
cmd = input()
half = int(len(deck)//2)
for e in cmd:
    if e == 'C':
        under = deck[0:half]
        top = deck[half:len(deck)]
        for j in under:
            top.append(j)
        deck = top
    elif e == 'S':
        under = deck[0:half+1]
        top = deck[half:len(deck)]
        result = []
        for i in range(half):
            result.append(under[i])
            result.append(top[i])
        deck = result
for e in deck:
    print(e, end=' ')
