def make_int_list(x):
 # รับสตริง x มำแยกและแปลงเป็น int เก็บใน list แล้วคืนเป็นผลลัพธ์
 # เช่น x = '12 34 5' ได้ผลเป็น [12 34 5]
    return [int(e) for e in x.split()]


def is_odd(e):
 # คืนค่ำจริงเมื่อ e เป็นจ ำนวนคี่ ถ้ำไม่ใช่ คืนค่ำเท็จ
    if(e % 2 == 0):
        return False
    return True


def odd_list(alist):
 # คืน list ที่มีค่ำเหมือน alist แต่มีเฉพำะตัวที่เป็นจ ำนวนคี่
 # เช่น alis = [10, 11, 13, 24, 25] จะได้ [11, 13, 25]
    lst = []
    for e in alist:
        if is_odd(e):
            lst.append(e)
    return lst


def sum_square(alist):

 # คืนผลรวมของก ำลังสองของแต่ละค่ำใน alist
 # เช่น alist = [1,3,4] ได้ผลเป็น (1*1 + 3*3 + 4*4) = 26
    total = 0
    for e in alist:
        total += e**2
    return total


exec(input().strip())  # ต้องมีบรรทัดนี้เมื่อส่งไป grader
