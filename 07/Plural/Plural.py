x = input()
vowels = ['a', 'e', 'i', 'o', 'u']

if(x[-1] == 's' or x[-1] == 'x' or x[-1:-3:-1] == 'hc'):
    x += 'es'
elif (x[-1] == 'y' and not(x[-2] in vowels)):
    x = x[:-1]
    x += 'ies'
else:
    x += 's'
print(x)
