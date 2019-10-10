def parser(phr, znak='', num1=0, num2=0, res=0):
    for i in phr:
        if znak == '':
            if i == '1':
                num1 *= 10
                num1 += 1
            elif i == '2':
                num1 *= 10
                num1 += 2
            elif i == '3':
                num1 *= 10
                num1 += 3
            elif i == '4':
                num1 *= 10
                num1 += 4
            elif i == '5':
                num1 *= 10
                num1 += 5
            elif i == '6':
                num1 *= 10
                num1 += 6
            elif i == '7':
                num1 *= 10
                num1 += 7
            elif i == '8':
                num1 *= 10
                num1 += 8
            elif i == '9':
                num1 *= 10
                num1 += 9
            elif i == '0':
                num1 *= 10
                num1 += 0
        if i == '+':
            znak = '+'
        elif i == '-':
            znak = '-'
        elif i == '*':
            znak = '*'
        elif i == '/':
            znak = '/'
        if znak != '':
            if i == '1':
                num2 *= 10
                num2 += 1
            elif i == '2':
                num2 *= 10
                num2 += 2
            elif i == '3':
                num2 *= 10
                num2 += 3
            elif i == '4':
                num2 *= 10
                num2 += 4
            elif i == '5':
                num2 *= 10
                num2 += 5
            elif i == '6':
                num2 *= 10
                num2 += 6
            elif i == '7':
                num2 *= 10
                num2 += 7
            elif i == '8':
                num2 *= 10
                num2 += 8
            elif i == '9':
                num2 *= 10
                num2 += 9
            elif i == '0':
                num2 *= 10
                num2 += 0
        if znak == '+':
            res = num1 + num2
        if znak == '-':
            res = num1 - num2
        if znak == '*':
            res = num1 * num2
        if znak == '/':
            res = num1 / num2

    return res


print(parser(input()))
