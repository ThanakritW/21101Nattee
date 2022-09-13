s1 = input()
s1 = s1.replace(' ', '').lower()
s2 = input()
s2 = s2.replace(' ', '').lower()
s1 = sorted(s1)
s2 = sorted(s2)
anagram = True
if(len(s1) != len(s2)):
    print('NO')
    exit(0)
for i in range(len(s1)):
    if(s1[i] != s2[i]):
        print('NO')
        exit(0)
print('YES')
