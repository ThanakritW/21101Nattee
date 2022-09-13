n = int(input())
df = {}
ds = {}
for i in range(n):
    f, s = input().strip().split()
    df[f] = s
    ds[s] = f
n = int(input())
for i in range(n):
    q = input().strip()
    if(q in df):
        print(df[q])
    elif(q in ds):
        print(ds[q])
    else:
        print('Not found')
