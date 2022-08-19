a = int(input())
b = 12
c = 100
d = 50
e = 1000
if a > 10:
    a -= 10
    b = b+a
    if a > 10:
        b = b+a
elif a == 10:
    print(10)
else:
    print("a is not big enough")

print(a)
