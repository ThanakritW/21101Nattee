def RLE(t):
    s = t
    if(len(s) == 0):
        return []
    last = s[0]
    n = 0
    lst = []
    for i in s:
        if i == last:
            n += 1
        else:
            lst.append([last, n])
            last = i
            n = 1
    lst.append([last, n])
    return lst


def str(x):
    output_string = ''
    for i in range(int(len(x)//2)):
        output_string += (x[2*i]*int(x[2*i+1]))
    return output_string


cmd = input()
if cmd == 'str2RLE':
    prnt = RLE(input())
    for e in prnt:
        print(e[0], e[1], end=' ')
elif cmd == 'RLE2str':
    print(str(input().split()))
else:
    print('Error')
