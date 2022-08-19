def choose(stu1, stu2):
    check1 = stu1[2] != 'A' or stu1[3] >= 'D' or stu1[4] >= 'D'
    check2 = stu2[2] != 'A' or stu2[3] >= 'D' or stu2[4] >= 'D'
    if(check1 and check2):
        return []
    if(check1):
        return [stu2[0]]
    if(check2):
        return [stu1[0]]
    if(stu1[1] != stu2[1]):
        if(stu1[1] > stu2[1]):
            return [stu1[0]]
        return [stu2[0]]
    if(stu1[3] != stu2[3]):
        if(stu1[3] < stu2[3]):
            return [stu1[0]]
        return [stu2[0]]
    if(stu1[4] != stu2[4]):
        if(stu1[4] < stu2[4]):
            return [stu1[0]]
        return [stu2[0]]
    return [stu1[0], stu2[0]]


x = input()
y = input()
x = x.split()
y = y.split()
ans = choose(x, y)
if(len(ans) == 0):
    print('None')
elif(len(ans) == 1):
    print(ans[0])
else:
    print('Both')
