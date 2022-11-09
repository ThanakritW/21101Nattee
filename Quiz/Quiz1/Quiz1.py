x = input().split()
x = [int(e) for e in x]
k = int(input())
cur = -1
cnt = 0
total = 0
for e in x:
    if(e == cur):
        cnt += 1
    else:
        if(cnt < k):
            total += cnt*cur
        cur = e
        cnt = 1
if(cnt < k):
    total += cnt*cur
print(total)
