def is_prime(n):
 # ทดสอบว่า n เป็นจ านวนเฉพาะหรือไม่
    if n <= 1:
        return False
    for k in range(2, int(n**0.5)+1):
        if n % k == 0:
            return False
    return True


def next_prime(N):
    N += 1
    while True:
        if is_prime(N):
            return N
        N += 1


def next_twin_prime(N):
    while True:
        nxt = next_prime(N)
        if(is_prime(nxt+2)):
            return (nxt, nxt+2)
        N = nxt


exec(input().strip())  # ตอ้ งมคี าสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
