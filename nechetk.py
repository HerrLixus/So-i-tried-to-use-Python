a = 0
b = 0
c = 0
et = False
phr = input()
etal = ['привет', 'хай ', 'йоу', 'че как']

for h in etal:
    a = 0
    c = 0
    for i in phr:
        a += 1
        b = 0
        for j in h:
            b += 1
            if a == b and i == j:
                c += 1
            if not et and c / len(h) > 0.7:
                et = True


if et:
    print("эталону соответствует")
else:
    print("эталону не соответствует")