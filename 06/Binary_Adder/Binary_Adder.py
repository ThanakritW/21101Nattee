a, b = input().split()
a = int(a, 2)
b = int(b, 2)
total = a+b
total = bin(total)
print(total[2:len(total)])
