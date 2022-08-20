def a_to_z(x):
    if((x >= 'A' and x <= 'Z') or (x >= 'a' and x <= 'z')):
        return True
    return False


a = input()
b = input()
n = 0
i = 0
while i < len(b):
    if(b[i:i+len(a)] == a):
        check = True
        if i > 0 and a_to_z(b[i-1]):
            check = False
        if i < len(b)-len(a)-1 and a_to_z(b[i+len(a)]):
            check = False
        if(check):
            n += 1
    i += 1
print(n)
