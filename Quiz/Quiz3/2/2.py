n,m,k = [int(e) for e in input().split()]

grad = dict()
relate = dict()

for i in range(n):
    name,faculty = input().split()
    grad[name] = faculty
for i in range(m):
    cmd = input().split()
    name = cmd[0]
    relate[name] = set()
    for e in cmd[1:]:
        relate[name].add(grad[e])
for i in range(k):
    group = input().split()
    ans = relate[group[0]]
    for e in group[1:]:
        ans = ans.intersection(relate[e])
    if(len(ans)):
        for e in sorted(ans):
            print(e,end=' ')
        print('')
    else:
        print('None')

        