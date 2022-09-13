s = input().strip().lower()
d = {}
lst = []

for e in s:
    if(not e.isalpha()):
        continue
    if(e in d):
        d[e] -= 1
    else:
        d[e] = -1

for e in d:
    lst.append([d[e], e])

lst = sorted(lst)

for e in lst:
    print(e[1], -1*int(e[0]), sep=' -> ')
