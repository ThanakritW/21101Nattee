def missing_digits(t):
    s = t
    first = True
    lst = []
    for i in range(10):
        if(str(i) in s):
            continue
        lst.append(i)
    return lst


exec(input())  # DON'T remove this line
