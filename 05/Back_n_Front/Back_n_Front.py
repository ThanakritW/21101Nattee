lst = []


def linsert(x):
    if(len(lst) % 2 == 0):
        lst.append(x)
    else:
        lst.insert(0, x)


n = int(input())
for i in range(n):
    t = int(input())
    linsert(t)
t = input().split()
x = [int(e) for e in t]
for e in x:
    linsert(e)
while True:
    t = int(input())
    if t == -1:
        break
    linsert(t)
print(lst)
