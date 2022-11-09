name = input()
f = open(name, 'r')
lines = f.readlines()
oname = input()
cname = input()
for line in lines:
    oidx = 0
    idx = line.find('/', oidx)
    while (idx != -1):
        if (len(line[oidx:idx]) != len(oname)):
            print(line[oidx:idx]+'/', end='')
        else:
            change = True
            for i in range(len(line[oidx:idx])):
                if (oname[i] == '?'):
                    continue
                if (oname[i].lower() != line[oidx+i].lower()):
                    change = False
                    break
            if (change):
                print(cname+'/', end='')
            else:
                print(line[oidx:idx]+'/', end='')
        oidx = idx+1
        idx = line.find('/', oidx+1)
    if (oidx != len(line)-1):
        print(line[oidx:])
    else:
        print('')
