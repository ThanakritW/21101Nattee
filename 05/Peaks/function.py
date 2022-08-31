
def peaks(x):
 # x: list of floats (or ints)
 # returns: list of indexes of peaks
    n = list(x)
    n = [float(e) for e in n]
    peak = []
    for i in range(1, len(n)-1):
        if(n[i-1] < n[i] > n[i+1]):
            peak.append(i)
    return peak


exec(input())  # DON'T remove this line
