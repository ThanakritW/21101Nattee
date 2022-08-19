x = input()
n = [int(i) for i in x]
check = 11
sum = 0
for i in range(12):
    sum += n[i]*(13-i)
sum %= 11
check -= sum
print(x[0], str(x[1:5:1]), x[5:10:1], x[10:12:1], check % 10)
