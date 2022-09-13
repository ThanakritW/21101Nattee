fname, year = input().split()
year = year[-2:]
f = open(fname, 'r').readlines()
mn = 1e6
mx = -1e6
total = 0
cnt = 0
for line in f:
    line = line.replace('\n', '').split()
    id, score = line[0], float(line[1])
    if(id[:2] == str(year)):
        mn = min(mn, score)
        mx = max(mx, score)
        total += score
        cnt += 1
if(cnt == 0):
    print('No data')
else:
    print(mn, mx, total/cnt)
