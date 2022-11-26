n = int(input())
places = dict()
ans = []
for i in range(n):
    s = input().strip()
    id,place = s.split(': ')
    place = place.split(', ')
    for j in place:
        if(not j in places):
            places[j]=set()
        places[j].add(id)
query = input().strip()
for e in places:
    if(query in places[e]):
        for j in places[e]:
            if(j != query and (not j in ans)):
                ans.append(j)
for e in ans:
    print(e)

# testcases
# 6
# 5123461: A, B, D, E, F
# 427613829: B, D, G, H, I
# 38216542: Z, B, D, J
# 423212822: AA, B1, C3, D
# 4126548: J, Z3
# 98871973331: Q, M, N
# 42321822

