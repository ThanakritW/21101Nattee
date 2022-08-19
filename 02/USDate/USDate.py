x = input()
d, m, y = x.split('/')
m = int(m)-1
month = ['January', 'February', 'March', 'April', 'May', 'June',
         'July', 'August', 'September', 'October', 'November', 'December']
print(month[m], d+',', y)
