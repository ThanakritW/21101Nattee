sol = input()
ans = input()
if(len(sol) != len(ans)):
    print("Incomplete answer")
    exit()
pt = 0
for i in range(len(sol)):
    if sol[i] == ans[i]:
        pt += 1
print(pt)
