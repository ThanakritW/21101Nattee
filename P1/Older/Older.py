a = input().split()
b = input().split()
months = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12}
a[2] = a[2][0:len(a[2])-1]
b[2] = b[2][0:len(b[2])-1]
am = months[a[1]]
bm = months[b[1]]
ad = int(a[2])
bd = int(b[2])
ay = int(a[3])
by = int(b[3])

if(ay != by):
    if(ay < by):
        print(a[0])
    else:
        print(b[0])
elif(am != bm):
    if(am < bm):
        print(a[0])
    else:
        print(b[0])
elif(ad != bd):
    if(ad < bd):
        print(a[0])
    else:
        print(b[0])
else:
    print(a[0], b[0])
