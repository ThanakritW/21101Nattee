s = input()
last = s[0]
n = 0
for i in s:
    if i == last:
        n += 1
    else:
        print(last, n, end=' ')
        last = i
        n = 1
print(last, n)
