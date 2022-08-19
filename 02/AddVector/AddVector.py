x = input()
y = input()
x=x[1:len(x)-1:1] #ตัด [ ] ออกจาก string
y=y[1:len(y)-1:1]
l1=x.split(", ") 
l2=y.split(", ")
l1=[float(e) for e in l1]
l2=[float(e) for e in l2]
l3=[]
for e in range(3):
    l3.append(l1[e]+l2[e])
print(l1,'+',l2,'=',l3)