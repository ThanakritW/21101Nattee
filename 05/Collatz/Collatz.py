n = input()
seq = []
while n != 1:
    n = int(n)
    seq.append(n)
    if(n % 2 == 0):
        n /= 2
    else:
        n = 3*n+1
seq.append(1)
if(len(seq) > 15):
    seq = seq[len(seq)-15:len(seq)]
first = True
for e in seq:
    if(first):
        first = False
    else:
        print('->', end='')
    print(e, end='')
