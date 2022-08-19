def check_digit(n):
 # คืนเลขตรวจสอบของเลข 12 หลักแรกของเลขบัตรประจ ำตัวประชำชน
 # n: สตรงิเก็บเลขสบิ สองหลักแรกของเลขบัตรประจ ำตัวประชำชน
    n = [int(i) for i in n]
    check = 11
    sum = 0
    for i in range(12):
        sum += n[i]*(13-i)
    sum %= 11
    check -= sum
    return check % 10


exec(input())  # DON'T remove this line
