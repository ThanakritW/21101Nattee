dna = input().strip().upper()
cmd = input()
for e in dna:
    if(e != 'A' and e != 'T' and e != 'C' and e != 'G'):
        print('Invalid DNA')
        exit(0)
if(cmd == 'R'):
    x = ''
    for e in dna:
        if(e == 'A'):
            x += 'T'
        elif (e == 'T'):
            x += 'A'
        elif (e == 'C'):
            x += 'G'
        elif (e == 'G'):
            x += 'C'
    print(x[::-1])
elif(cmd == 'F'):
    cntA = 0
    cntT = 0
    cntC = 0
    cntG = 0
    for e in dna:
        if(e == 'A'):
            cntA += 1
        elif (e == 'T'):
            cntT += 1
        elif (e == 'C'):
            cntC += 1
        elif (e == 'G'):
            cntG += 1
    print('A=%s, T=%s, G=%s, C=%s' % (cntA, cntT, cntG, cntC))
else:
    substr = input()
    idx = dna.find(substr, 0)
    cnt = 0
    while(idx != -1):
        cnt += 1
        idx = dna.find(substr, idx+1)
    print(cnt)
