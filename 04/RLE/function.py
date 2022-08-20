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


exec(input())  # DON'T remove this line
