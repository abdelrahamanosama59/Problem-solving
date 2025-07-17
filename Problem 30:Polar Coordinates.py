import cmath

s = input()
s = complex(s)
seta = cmath.polar(s)

for i in seta:
    print(i)
