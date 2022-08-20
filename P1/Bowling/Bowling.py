x = input()
i = 0
total = 0
round = 0
score = []


def strike(idx):
    buffer = 0
    if(x[idx+2] == '/'):
        return 10
    if(x[idx+1] == 'X'):
        buffer += 10
    else:
        buffer += int(x[idx+1])
    if(x[idx+2] == 'X'):
        buffer += 10
    else:
        buffer += int(x[idx+2])
    return buffer


def spare(idx):
    if(x[idx+2] == 'X'):
        return 10
    else:
        return int(x[idx+2])


while round < 9:
    if x[i] == 'X':
        temp = 10+strike(i)
        score.append(temp)
        i += 1
        total += temp
    else:
        if(x[i+1] == '/'):
            temp = 10 + spare(i)
            score.append(temp)
            total += temp
        else:
            score.append(int(x[i])+int(x[i+1]))
            total += int(x[i])+int(x[i+1])
        i += 2
    round += 1

last = x[i:len(x)]
lastsc = 0
if(last[1] == '/'):
    if last[2] == 'X':
        lastsc = 20
    else:
        lastsc = 10+int(last[2])
elif(last[0] == 'X' and last[2] == '/'):
    lastsc = 20
else:
    for i in last:
        if(i == 'X'):
            lastsc += 10
        else:
            lastsc += int(i)
score.append(lastsc)
total += lastsc
n = int(input())
if(n in range(1, 11)):
    print(score[n-1])
else:
    print(total)
