n = int(input())
for i in range(n):
    s = input()
    cnt = 0
    if(len(s) == 0):
        print('')
        continue
    while(s[cnt] == '.'):
        cnt += 1
    print(s[int(cnt/2):len(s)])
