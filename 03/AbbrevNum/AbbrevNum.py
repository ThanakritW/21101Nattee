x = int(input())
dict={1e9:'B',1e6:'M',1e3:'K'}
for v,k in dict.items():
    if x/v >= 1:
        if x/v<10:
            print(round(x/v,1),k,sep='')
        else:
            print(int(round(x/v,0)),k,sep='')
        exit()
print(x)