a = 0
b = 0
c = 0
phr = input()
n = 'привет'

for i in phr:
    a += 1
    b = 0
    for j in n:
        b += 1
        if a == b and i == j:
            c += 1

if c == 0:
    print("эталону не соответствует")
elif len(n) / c > 0.7:
    print("эталону соответствует")
else:
    print("эталону не соответствует")