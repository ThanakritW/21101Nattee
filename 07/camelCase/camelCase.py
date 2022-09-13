from pickle import FALSE


s = input()
first = False
ffirst = False
for x in s:
    if((x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z') or (x >= '0' and x <= '9')):
        if(first and ffirst):
            print(x.upper(), end='')
            first = False
        else:
            print(x.lower(), end='')
            ffirst = True
            first = False
    else:
        first = True
