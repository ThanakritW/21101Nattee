s = input()
x = int(s[3] + s[10] + s[17] + s[24] + s[31])
y = int(s[7] + s[12] + s[17] + s[22] + s[27])
z=x+y+10000
z//=10
z%=1000
letter = z%10
letter += (z//10)%10
letter += (z//100)%10
letter = (letter%10)+1
print(str(z)+chr(ord('A')+letter-1)) 