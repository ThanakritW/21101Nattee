mname = ["Jan", "Feb", "Mar", "Apr",
         "May", "Jun", "Jul", "Aug",
         "Sep", "Oct", "Nov", "Dec"]
dim = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def read_date():  # อ่านวันเดือนปีคั่นด้วยช่องว่าง เดือนเป็นชื่อเดือน คืนลิสต์ เลขวัน เดือน ปี
    s = input().split()
    return [int(s[0]), mname.index(s[1])+1, int(s[2])]


def zodiac(d, m):  # คืนชื่อราศีของวัน d เดือน m
    if d >= 22 and m == 3 or d <= 21 and m == 4:
        return "Aries"
    if d >= 22 and m == 4 or d <= 21 and m == 5:
        return "Taurus"
    if d >= 22 and m == 5 or d <= 21 and m == 6:
        return "Gemini"
    if d >= 22 and m == 6 or d <= 21 and m == 7:
        return "Cancer"
    if d >= 22 and m == 8 or d <= 21 and m == 9:
        return "Virgo"
    if d >= 22 and m == 7 or d <= 21 and m == 8:
        return "Leo"
    if d >= 22 and m == 9 or d <= 21 and m == 10:
        return "Libra"
    if d >= 22 and m == 10 or d <= 21 and m == 11:
        return "Scorpio"
    if d >= 22 and m == 11 or d <= 21 and m == 12:
        return "Sagittarius"
    if d >= 22 and m == 12 or d <= 20 and m == 1:
        return "Capricorn"
    if d >= 21 and m == 1 or d <= 20 and m == 2:
        return "Aquarius"
    if d >= 21 and m == 2 or d <= 21 and m == 3:
        return "Pisces"


def days_in_feb(y):  # คืนจ านวนวันของเดือนกุมภาพันธ์ในปี y
    if (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)):
        return 29
    return 28


def days_in_month(m, y):  # คืนจ านวนวันของเดือน m ในปี y
    if(m == 2):
        return days_in_feb(y)
    else:
        return dim[m-1]


def days_in_between(d1, m1, y1, d2, m2, y2):
 # คืนจ านวนวันตั้งแต่วันเดือนปีd1,m1,y1 ถึง d2,m2,y2
    total = days_in_month(m1, y1)-d1
    for i in range(m1+1, 13):
        total += days_in_month(i, y1)
    for i in range(y1+1, y2):
        total += 365
        if(days_in_feb(i) == 29):
            total += 1
    for i in range(1, m2):
        total += days_in_month(i, y2)
    total += d2
    return total-1


def main():
    d1, m1, y1 = read_date()
    d2, m2, y2 = read_date()
    print(zodiac(d1, m1), zodiac(d2, m2))
    print(days_in_between(d1, m1, y1, d2, m2, y2))


    # แสดง ราศีของ d1,m1,y1 กับ ของ d2,m2,y2 บรรทัดเดียกัน คั่นด้วยช่องว่าง
    # แสดงจ านวนวันตั้งแต่ d1,m1,y1 ถึง d2,m2,y2
exec(input().strip())  # ต้องมีบรรทัดนี้เมื่อส่งไป grader
