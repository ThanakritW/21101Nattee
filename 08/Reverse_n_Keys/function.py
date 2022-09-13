def reverse(d):
    # d เป็น dict ที่มี value ไม่ซ ้ำกนั
    # คืน dict ใหม่ที่เก็บ key,value ที่ค่ำเป็น value,key ของ d ที่ได ้รับ
    rd = {}
    for e in d:
        rd[d[e]] = e
    return rd


def keys(d, v):
    # คืนลิสต์ที่เก็บค่ำของ keys ใน d (เรียงยังไงก็ได ้) ที่มีค่ำ value เท่ำกับ v
    lst = []
    for e in d:
        if(v == d[e]):
            lst.append(e)
    return lst


exec(input().strip())  # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
