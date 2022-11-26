cmd = input()
cnt = 0
ally = dict()
enemy = dict()
while(cmd != 'End'):
    cmd = cmd.split()
    if(cmd[0] == 'Ally'):
        group = cmd[1:]
        for i in range(len(group)):
            if(not group[i] in ally): ally[group[i]] = set()
            ally[group[i]].update(group[0:i])
            ally[group[i]].update(group[i+1:])
    elif(cmd[0] == 'Enemy'):
        c1,c2 = cmd[1:]
        if(not c1 in ally):
            ally[c1] = set()
        if(not c2 in ally):
            ally[c2] = set()
        u = ally[c1]
        u.add(c1)
        for e1 in u:
            if(not e1 in enemy): enemy[e1] = set()
            enemy[e1].add(c2)
            for e2 in ally[c2]:
                enemy[e1].add(e2)
        u = ally[c2]
        u.add(c2)
        for e1 in u:
            if(not e1 in enemy): enemy[e1] = set()
            enemy[e1].add(c1)
            # print(e1,enemy[e1])
            for e2 in ally[c1]:
                enemy[e1].add(e2)
    elif(cmd[0] == "Table"):
        # print(enemy) 
        lst = cmd[1:]
        valid = True
        for i in range(len(lst)):
            if(not lst[i] in enemy):
                continue
            if(lst[i-1] in enemy[lst[i]]):
                valid = False
                break
        if(valid):
            print('Okay')
        else:
            print('No')
    
    cmd = input()
