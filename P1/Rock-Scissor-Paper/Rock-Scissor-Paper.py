from re import L

n = int(input())
a = 0
b = 0
for i in range(3*n):
    pa, pb = [e for e in input().split()]
    if(pa != pb):
        if((pa == 'R' and pb == 'S') or (pa == 'S' and pb == 'P') or (pa == 'P' and pb == 'R')):
            a += 1
        else:
            b += 1
    if(a == n or b == n):
        break
print(a, b)
if(a == n):
    print('Player 1 wins')
elif(b == n):
    print('Player 2 wins')
else:
    print('Tie')
