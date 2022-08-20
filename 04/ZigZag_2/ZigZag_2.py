n = 0
zigmn = 1e19
zigmx = -1e19
zagmn = 1e19
zagmx = -1e19
while True:
    x = input()
    n += 1
    if(x[0] == 'Z'):
        break
    l, r = [int(e) for e in x.split()]
    if n % 2 == 1:
        zigmn = min(zigmn, l)
        zigmx = max(zigmx, l)
        zagmn = min(zagmn, r)
        zagmx = max(zagmx, r)
    else:
        zigmn = min(zigmn, r)
        zigmx = max(zigmx, r)
        zagmn = min(zagmn, l)
        zagmx = max(zagmx, l)

if(x == 'Zig-Zag'):
    print(zigmn, zagmx)
else:
    print(zagmn, zigmx)
