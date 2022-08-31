n = int(input())
lst = []
for i in range(n):
    x, y = input().split()
    total = (float(x)**2+float(y)**2)**0.5
    lst.append([total, i+1, x, y])
lst.sort()
ans = lst[2]
print('#', ans[1], ': (', ans[2], ', ', ans[3], ')', sep='')
