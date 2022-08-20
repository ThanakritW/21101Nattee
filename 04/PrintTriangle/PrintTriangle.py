n = int(input())
print(' '*(n-2), '*')
for i in range(2, n):
    print(' '*(n-i), end='')
    print('*', end='')
    print(' '*(2*i-3), end='')
    print('*')
print('*'*(2*n-1))
