a = input()
for i in range(len(a)):
    if a[i] == '(':
        print('[', end='')
    elif a[i] == '[':
        print('(', end='')
    elif a[i] == ')':
        print(']', end='')
    elif a[i] == ']':
        print(')', end='')
    else:
        print(a[i], end='')
