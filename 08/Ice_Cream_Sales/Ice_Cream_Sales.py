n = int(input())
d = {}
sale = {}
total = 0
for i in range(n):
    name, price = input().split()
    d[name] = float(price)
    sale[name] = 0.0
q = int(input())
for i in range(q):
    name, cnt = input().split()
    if(name in d):
        sale[name] += d[name]*int(cnt)
        total += d[name]*int(cnt)
lst = []
for e in d:
    lst.append([-1*sale[e], e])
lst = sorted(lst)
if(lst[0][0] == 0):
    print('No ice cream sales')
    exit(0)
print("Total ice cream sales:", total)
print("Top sales:", lst[0][1], end='')
for i in range(1, len(lst)):
    e = lst[i]
    if e[0] != lst[0][0]:
        break
    print(", %s" % e[1], end='')
