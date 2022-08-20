rotate = input()
n = int(input())
a = ['']*n
for i in range(n):
    a[i] = input()
for i in range(n-1):
    if(len(a[i]) != len(a[i+1])):
        print('Invalid size')
        exit()
if(rotate == '90'):
    for i in range(len(a[0])):
        for j in range(n):
            print(a[n-1-j][i], end='')
        print('')
elif(rotate == 'flip'):
    for i in range(n):
        print(a[i][::-1])
if(rotate == '180'):
    for j in range(n):
        print(a[n-j-1][::-1])
