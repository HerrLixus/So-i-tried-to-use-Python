nm1 = int(input())
mark = input()
nm2 = int(input())
while True:
    if mark == '+':
        nm1 = nm1 + nm2
        print(nm1)
        mark = input()
        nm2 = int(input())
    elif mark == '-':
        nm1 = nm1 - nm2
        print(nm1)
        mark = input()
        nm2 = int(input())
    elif mark == '*':
        nm1 = nm1 * nm2
        print(nm1)
        mark = input()
        nm2 = int(input())
    elif mark == '/':
        nm1 = nm1 / nm2
        print(nm1)
        mark = input()
        nm2 = int(input())
    elif mark == '//':
        nm1 = nm1 // nm2
        print(nm1)
        mark = input()
        nm2 = int(input())
    elif mark == '^':
        nm1 = nm1 ** nm2
        print(nm1)
        mark = input()
        nm2 = int(input())