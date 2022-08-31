real = ['Robert', 'William', 'James', 'John', 'Margaret',
        'Edward', 'Sarah', 'Andrew', 'Anthony', 'Deborah']
nick = ['Dick', 'Bill', 'Jim', 'Jack', 'Peggy',
        'Ed', 'Sally', 'Andy', 'Tony', 'Debbie']
n = int(input())
for i in range(n):
    s = input()
    found = False
    for j in range(10):
        if s == real[j]:
            print(nick[j])
            found = True
            break
        elif s == nick[j]:
            print(real[j])
            found = True
            break
    if(not found):
        print('Not found')
