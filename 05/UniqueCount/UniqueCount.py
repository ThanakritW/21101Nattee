n = input().split()
n = [int(e) for e in n]
s = set({})
for e in n:
    s.add(e)
s = sorted(s)
print(len(s))
s = s[0:10]
print(s)
