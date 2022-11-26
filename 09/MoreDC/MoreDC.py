n = input().strip()
animals = {}
animals_name = []
while(n!='q'):
    name,animal = n.split(', ')
    if(not animal in animals): 
        animals[animal]=[]
        animals_name.append(animal)
    animals[animal].append(name)
    n = input().strip()
for e in animals_name:
    print(e,': ',end='',sep='')
    for k in range(len(animals[e])):
        if(k): print(', ',end='')
        print(animals[e][k],end='')
    print()

# testcases
# Ted, bear
# Pongo, dog
# Fozzie, bear
# Winnie-the-Pooh, bear
# Nana, dog
# Hello Kitty, cat
# Scooby Doo, dog
# Yogi, bear
# Garfield, cat
# Tom, cat
# Sylvester, cat
# Pluto, dog
# Goofy, dog
# q