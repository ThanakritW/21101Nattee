def row_number(t, e):  # return row number of t containing e (top row is row #0)
    for i in range(len(t)):
        if(e in t[i]):
            return i


def flatten(t):  # return a list of ints converted from list of lists of ints t
    lst = []
    for e in t:
        for j in e:
            if(j != 0):
                lst.append(j)
    return lst


def inversions(x):  # return the number of inversions of list x
    cnt = 0
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if(x[i] > x[j]):
                cnt += 1
    return cnt


def solvable(t):  # return True if tiling t (list of lists of ints) is solvable
    # otherwise return False
    isZeroEven = row_number(t, 0) % 2 == 0
    isRowEven = len(t) % 2 == 0
    isInvEven = inversions(flatten(t)) % 2 == 0
    if(not isRowEven):
        if(isInvEven):
            return True
    else:
        if(isInvEven and (not isZeroEven)):
            return True
        if((not isInvEven) and isZeroEven):
            return True
    return False


exec(input().strip())  # do not remove this line
