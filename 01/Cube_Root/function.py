def sqrt_n_times(x, n):
    cal = x
    for e in range(n):
        cal = cal**(1/2)
    return cal
def cube_root(y):
    cal=sqrt_n_times(y,2)
    cal=cal*sqrt_n_times(cal,2)
    cal=cal*sqrt_n_times(cal,4)
    cal=cal*sqrt_n_times(cal,8)
    cal=cal*sqrt_n_times(cal,16)
    cal=cal*sqrt_n_times(cal,32)
    return round(cal,15)
def main():
 q = float(input())
 print(cube_root(q))
exec(input()) # DON'T remove this line