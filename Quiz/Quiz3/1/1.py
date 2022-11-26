n = int(input())
teams = dict()
for i in range(n):
    n,c = input().split()
    teams[n] = c
lst = input()
while(lst != 'q'):
    team = lst.split()
    group = set()
    valid = True
    for e in team:
        if(not e in teams):
            valid = False
            print("Not OK")
            break
        if(teams[e] in group):
            valid = False
            print("Not OK")
            break
        group.add(teams[e])
    if(valid):
        print('OK')
    lst = input()