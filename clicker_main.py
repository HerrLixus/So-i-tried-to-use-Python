from random import randint
import io
z = ['Меч 1 уровня', 'Меч 2 уровня', 'Меч 3 уровня', 'ЫЫЫЫ АДМИН АРУЖИЕ']
x = 0
i = 100
money = 0
if x == 0:
    ur = 1
if x == 1:
    ur = 2
if x == 2:
    ur = 3
if x == 3:
    ur = 100
while i >= 0:
    c = randint(0, 100)
    a = input()
    if c <= 25:
        i -= ur * 2
        print("Вы нанесли критический удар!")
    else:
        i -= ur
    print(i, "хп у монстра")
else:
    vi = input("1 - Магазин")
# if vi == 1:
