def is_mobile_number(number):
 # number เป็นสตริงเก็บหมายเลข (ภายในสตริงมีแต่ตัวเลขแน่ ๆ)
 # คืน True ถ้า number เป็นหมายเลขโทรศัพท์ถา้ไม่เป็น คืน False
    if(len(number) != 10):
        return False
    digit = number[0:2]
    if(digit != '06' and digit != '08' and digit != '09'):
        return False
    return True


x = input()
if(is_mobile_number(x)):
    print('Mobile number')
else:
    print('Not a mobile number')
