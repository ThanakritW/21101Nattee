def spiral_square(n): # n is a positive odd number
    pattern = [[0]*n for e in range(n)]
    x = y = n-1
    cnt = n**2
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    dir = 0
    while(cnt):
        pattern[x][y]=cnt
        cnt-=1
        if(not ((0 <= x+dx[dir] < n) and (0 <= y+dy[dir] < n))):
            dir = (dir+1)%4
        elif(pattern[x+dx[dir]][y+dy[dir]]!=0):
            dir = (dir+1)%4
        x += dx[dir]
        y += dy[dir]
    return pattern
        
def print_square(S):
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))

exec(input().strip())