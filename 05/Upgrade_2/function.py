score = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']


def index_of(grades, ID):
    for i in range(len(grades)):
        if ID == grades[i][0]:
            return i
    return -1


def upgrade(grades, IDs):
    for e in IDs:
        idx = index_of(grades, e)
        if idx == -1:
            continue
        if grades[idx][1] == 'A':
            continue
        else:
            grades[idx][1] = score[score.index(grades[idx][1])-1]
    grades.sort()


# DON'T remove the following three lines
exec(input())
exec(input())
exec(input())
