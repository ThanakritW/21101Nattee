cnt = 0
student = []
id = []
score = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
while True:
    n = input()
    if(n == 'q'):
        break
    student.append(n.split())
    id.append(n.split()[0])
n = input().split()
for e in n:
    idx = id.index(e)
    if(student[idx][1] == 'A'):
        continue
    student[idx][1] = score[score.index(student[idx][1])-1]
student.sort()
for e in student:
    print(e[0], e[1])
