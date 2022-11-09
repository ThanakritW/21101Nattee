def format(num):
    if(num%1 == 0):
        return int(num)
    return num

n = int(input())
user = {}
Bid = set()
for i in range(n):
    name,id,money = input().split()
    if(not name in user):
        user[name]={id:float(money)}
    else:
        user[name][id] = float(money)
    Bid.add(id)
while(True):
    cmd = input()   
    if(cmd == 'exit'):
        break
    cmd = cmd.split()
    if(cmd[2] == 'deposit'):
        if(not cmd[0] in user):
            if(cmd[1] in Bid):
                print("Transaction Failed")
                continue
            user[cmd[0]]={cmd[1]:float(cmd[3])}
        elif(not cmd[1] in user[cmd[0]]):
            if(cmd[1] in Bid):
                print("Transaction Failed")
                continue
            user[cmd[0]][cmd[1]]=float(cmd[3])
        else:
            user[cmd[0]][cmd[1]]+=float(cmd[3])
        print(cmd[0]," (",cmd[1],") ",format(user[cmd[0]][cmd[1]]),sep='')
    if(cmd[2] == 'withdraw'):
        if(not cmd[0] in user):
            print("Transaction Failed")
            continue
        if(not cmd[1] in user[cmd[0]]):
            print("Transaction Failed")
            continue
        else:
            if(user[cmd[0]][cmd[1]]<float(cmd[3])):
                print("Transaction Failed")
                continue
            else:
                user[cmd[0]][cmd[1]]-=float(cmd[3])
                print(cmd[0]," (",cmd[1],") ",format(user[cmd[0]][cmd[1]]),sep='')
    if(cmd[2]=='transfer'):
        target = ''
        for e in user:
            if(cmd[3] in user[e]):
                target = e
        if(target == ''):
            print("Transaction Failed")
            continue
        if(not cmd[0] in user):
            print("Transaction Failed")
            continue
        if(not cmd[1] in user[cmd[0]]):
            print("Transaction Failed")
            continue
        else:
            if(user[cmd[0]][cmd[1]]<float(cmd[4])):
                print("Transaction Failed")
                continue
            else:
                user[cmd[0]][cmd[1]]-=float(cmd[4])
                user[target][cmd[3]]+=float(cmd[4])
                print(cmd[0]," (",cmd[1],") ",format(user[cmd[0]][cmd[1]]),sep='')
                print(target," (",cmd[3],") ",format(user[target][cmd[3]]),sep='')