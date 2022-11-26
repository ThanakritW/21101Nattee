class roman:
    def __init__(self, r):
        self.r = r

    def __lt__(self, rhs):
        return int(self) < int(rhs)

    def __str__(self):
        return self.r

    def __int__(self):
        total = 0
        trans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = []
        for i in range(len(self.r)):
            num.append(trans[self.r[i]])
        i = 0
        while (i < len(num)):
            if (i == len(num)-1):
                total += num[i]
                break
            if (num[i] >= num[i+1]):
                total += num[i]
            else:
                total -= num[i]
            i += 1
        return total

    def __add__(self, rhs):
        trans = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        r = ''
        key = sorted(trans.keys(), reverse=True)
        total = int(self)+int(rhs)
        for e in key:
            if (total >= e):
                n = total//e
                r += trans[e]*n
                total -= n*e
        self.r = r
        return self


t, r1, r2 = input().split()
a = roman(r1)
b = roman(r2)
if t == '1':
    print(a < b)
elif t == '2':
    print(int(a), int(b))
elif t == '3':
    print(str(a), str(b))
elif t == '4':
    print(int(a + b))
else:
    print(str(a + b))
