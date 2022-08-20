def grade_mcq(sol, ans):
    if(len(sol) != len(ans)):
        return -1
    pt = 0
    for i in range(len(sol)):
        if sol[i] == ans[i]:
            pt += 1
    return pt


exec(input())  # DON'T remove this line
