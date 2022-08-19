def number_name(n):
    # คืนค ำอ่ำนของตัวเลข (หลักเดียว) ตำมตำรำงข้ำงบนนี้
    # n: เป็นสตริงเก็บเลขหลักเดียว '0', '1', ..., '9'
    # หรือ เป็นจ ำนวนเต็มหรือจ ำนวนจริงมีค่ำ 0,1,2,...,9
    n = int(float(n))
    arab = ['zero', 'one', 'two', 'three', 'four',
            'five', 'six', 'seven', 'eight', 'nine']
    return arab[n]


exec(input())  # DON'T remove this line
