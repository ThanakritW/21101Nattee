s = input()
first = True
for i in range(10):
    if(str(i) in s):
        continue
    if(first):
        first = False
    else:
        print(',', end='')
    print(i, end='')
if(first):
    print('None')
