totalp = 0
totals = 0
totalh = 0
for i in range(9):
    p, s, c = [int(e) for e in input().split()]
    totalp += p
    totals += s
    if(c == 1):
        totalh += min(s, p+2)
print(totals)
handicap = 0.8 * (1.5*totalh-totalp)
if(handicap < 0):
    handicap -= 1
handicap = int(handicap)
print(handicap)
print(totals-handicap)
