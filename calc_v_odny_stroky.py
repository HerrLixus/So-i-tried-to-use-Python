nm = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']  # создаем список цифр
mrk = ['+', '-', '*', '/']
curmr = ''
nm1 = 0
nm2 = 0
res = 0
inp = input()  # просим пользователя ввести пример
for i in inp:
    for j in nm:
        if i == j and curmr == '':
            nm1 *= 10
            nm1 += int(i)
        elif i == j and curmr != '':
            nm2 *= 10
            nm2 += int(i)
    for h in mrk:
      if i == h:
          curmr = i
if curmr == '+':
    res = nm1 + nm2
elif curmr == '-':
    res = nm1 - nm2
elif curmr == '*':
    res = nm1 * nm2
elif curmr == '/':
    res = nm1 / nm2
print(res)