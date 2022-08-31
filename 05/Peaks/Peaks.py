n = input().split()
n = [int(e) for e in n]
cnt = 0
for i in range(1, len(n)-1):
    if(n[i-1] < n[i] > n[i+1]):
        cnt += 1
print(cnt)
