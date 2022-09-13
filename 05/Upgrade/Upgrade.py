cnt = 0
code = []
grade = []
score = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
while True:
    n = input()
    if(n == 'q'):
        break
    c, g = n.split()
    code.append(c)
    grade.append(g)
n = input().split()
for e in n:
    idx = code.index(e)
    if(grade[idx] == 'A'):
        continue
    grade[idx] = score[score.index(grade[idx])-1]
for i in range(len(code)):
    print(code[i], grade[i])
