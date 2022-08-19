def choose(stu1, stu2):
 # stu1 และ stu2 เป็นลิสต์[ ID, GPAX, compprog, cal1, cal2 ]
 # ID เป็นสตริงเก็บเลขประจ ำตัว
 # GPAX เป็น float
 # comprog, cal1, cal2 เป็นสตริงเก็บเกรดของสำมวิชำ (เกรดเป็นแบบไม่มีประจุ A,B,C,D,F)
 # ฟังกช์ ันนี้คนื
 # - ถ้ำไม่ผ่ำนเกณฑ์ข้อ 1 ทั้งคู่ คืนลิสต์ว่ำง
 # - ถ้ำผ่ำนเกณฑ์ข้อ 1 คนเดียว คืนลิสต์ที่เก็บเลขประจ ำตัวของคนที่ผ่ำนเกณฑ์ข้อ 1
 # - ถ้ำผ่ำนเกณฑ์ข้อ 1 ทั้งคู่ คืนลิสต์ที่เก็บเลขประจ ำตัวของนิสติ ที่มีข้อ 2 ที่ดีกว่ำ
 # - ถ้ำผ่ำนเกณฑ์ข้อ 1 ทั้งคู่ และมีข้อ 2 เท่ำกัน คืนลิสต์ที่เก็บเลขประจ ำตัวของนิสติ คนแรก ตำมด้วยของคนที่สอง
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


exec(input())  # DON'T remove this line
