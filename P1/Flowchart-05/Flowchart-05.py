c = input()
if(c == 'S'):
    m = int(input())
    q = 1
    r = 0
    t = 1
    k = 1
    n = 3
    x = 3
    i = 0
    p = ''
    while(i < m):
        if(4*q+r-t < n*t):
            p = p+str(n)
            i += 1
            a = 10*(r-n*t)
            n = (10*(3*q+r))//t-10*n
            q = 10*q
            r = a
        else:
            a = x*(2*q+r)
            b = (7*q*k+2+x*r)//(x*t)
            q = k*q
            t *= x
            x += 2
            k += 1
            n = b
            r = a
    p = p[0]+'.'+p[1:len(p)]
    print('pi =', p)
else:
    if(c == 'R'):
        n = int(input())
        total = 0
        for k in range(n+1):
            total += ((-3)**(-k))/(2*k+1)
        p = (12**0.5)*total
        p = round(p, 12)
        print('pi =', p)
    elif(c == 'P'):
        p = (7+(6+(5**0.5))**0.5)**0.5
        p = round(p, 6)
        print('pi =', p)
    else:
        print('Invalid')
