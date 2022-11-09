name = input()
f = open(name, 'r')
lines = f.readlines()
oname = input()
cname = input()
for line in lines:
    tmp = ""
    oidx = 0
    idx = line.find('/', oidx)
    while (idx != -1):
        print(line[oidx:idx])
        oidx = idx
        idx = line.find('/', oidx)
