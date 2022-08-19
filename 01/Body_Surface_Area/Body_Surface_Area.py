import math
w = float(input())
h = float(input())
print(pow(w*h, 1/2)/60)
print(0.024265*pow(w, 0.5378)*pow(h, 0.3964))
print(0.0333*pow(w, 0.6157-0.0188*math.log10(w))*pow(h, 0.3))
