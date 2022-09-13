f1, f2 = input().strip().split()
f1 = open(f1, 'r').readlines()
f2 = open(f2, 'r').readlines()
f1 = [e.replace('\n', '') for e in f1]
f2 = [e.replace('\n', '') for e in f2]
f1 += f2
reg = []
for e in f1:
    id, grade = e.split()
    reg.append([id[len(id)-2:], id, grade])
reg = sorted(reg)
for e in reg:
    print(e[1], e[2])
