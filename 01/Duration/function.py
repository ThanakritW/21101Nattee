from posixpath import split


def str2hms(hms_str):
    # คนื จ ำนวนชั่วโมง นำทีและวนิ ำที ที่ดึงมำจำกสตริง hms
    # เชน่ str2hms("10:03:29") ได้ 10,3,29
    t = hms_str.split(':')
    return int(t[0]), int(t[1]), int(t[2])


def hms2str(h, m, s):
    # คืนสตริงในรูปแบบ HH:MM:SS ที่น ำจ ำนวนชั่วโมง นำที และวินำทีมำจำก h,m และ s
    # เชน่ hms2str(10,3,29) ได้ "10:03:29"
    return ('0'+str(h))[-2:] + ':' + \
        ('0'+str(m))[-2:] + ':' + \
        ('0'+str(s))[-2:]


def to_sec(h, m, s):
    # คืนจ ำนวนวินำทีทั้งหมดนับจำกเที่ยงคืนจำกถึงเวลำ h:m:s
    # เชน่ to_sec(10,3,29) ได้ 36209
    return (h*3600+m*60+s)


def to_hms(s):
    # คืนจ ำนวนชั่วโมง นำที และวินำที ที่หำมำจำกจ ำนวนวินำที่ s ทั้งหมดนับจำกเที่ยงคืน
    # เชน่ to_hms(36209) ได้ 10,3,29
    ha = s//3600
    s = s % 3600
    ma = s//60
    s = s % 60
    sa = s
    return ha, ma, sa


def diff(h1, m1, s1, h2, m2, s2):
    # คืนจ ำนวนชั่วโมง นำทีและวนิ ำที่ จะเป็นชว่ งเวลำตัง้แต่เวลำ h1,m1,s1 จนถึง h2,m2,s2
    # เชน่ diff(10,57,57, 12,0,0) ได้ 1,2,3
    # หมำยเหตุ เวลำ h1,m1,s1 ที่ได้รับ ไม่มำกกว่ำ h2,m2,s2 แน่ ๆ
    # (เชน่ ไม่มีกรณีให้หำชว่ งเวลำตั้งแต่ 23,50,50 ถึง 2,1,1 แน่ ๆ)
    ts = to_sec(h1, m1, s1)
    tt = to_sec(h2, m2, s2)
    if(tt < ts):
        tt += 1440*60
    tt -= ts
    ha, ma, sa = to_hms(tt)
    return ha, ma, sa


def main():
    # ฟังกช์ ันนี้รับเวลำเริ่มต้น และเวลำสนิ้ สุด ในรูปแบบ HH:MM:SS
    # เพื่อแสดงชว่ งเวลำตั้งแต่เริ่มจนถึงสนิ้ สุด ในรูปแบบ HH:MM:SS
    # ดูตัวอย่ำงในตำรำงข้ำงล่ำง
    hms_start = input()
    hms_end = input()
    h1, m1, s1 = [int(x) for x in hms_start.split(':')]
    h2, m2, s2 = [int(x) for x in hms_end.split(':')]
    ha, ma, sa = diff(h1, m1, s1, h2, m2, s2)
    print(hms2str(ha, ma, sa))


exec(input())  # DON'T remove this line
