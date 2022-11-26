word = []
ask = ''
n = m = lenAsk = 0

def recur(x,y,cnt,path):
    if(word[x][y]!=ask[cnt]):
        return
    if(cnt == lenAsk-1):
        print(path)
        exit(0)
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if(-1 < nx < n and -1 < ny < m):
            recur(nx,ny,cnt+1,path+[(nx,ny)])

n,m = [int(e) for e in input().split()]
for i in range(n):
    s = input().strip()
    word.append(s)
ask = input()
lenAsk = len(ask)
for i in range(n):
    for j in range(m):
        if(word[i][j]==ask[0]):
            recur(i,j,0,[(i,j)])



