def factor(N):  # N เป็ นจ ำนวนเต็มบวกมำกกว่ำ 1
    i = 2
    lst = []
    while(N > 1):
        if(N % i != 0):
            i += 1
            continue
        cnt = 0
        while(N % i == 0):
            N /= i
            cnt += 1
        lst.append([i, cnt])
        N = int(N)
        i += 1
    return lst


exec(input().strip())
