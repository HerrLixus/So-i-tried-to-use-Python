def godb():
    print('Пока.')

def wud():
    print("Чем занимаешься?")
    phr2 = input()
    print('Круто. как продвигается работа?')
    phr3 = input()
    if phr3 == "хорошо" or phr3 == "Хорошо" or phr3 == "нормально" or phr3 == "Нормально" or phr3 == "норм" or phr3 == "Норм":
        print("Найс. Удачи.")
        godb()
    elif phr3 == "плохо" or phr3 == "Плохо":
        print("Может, тебе стоит отдохнуть?")
        godb()
    else:
        print('Я тебя не понял.')

def hau():
    print('Как дела?')
    phr1 = input()
    if phr1 == "хорошо" or phr1 == "Хорошо" or phr1 == "нормально" or phr1 == "Нормально" or phr1 == "Норм" or phr1 == "норм":
        print("Это хорошо.")
        wud()
    elif phr1 == "плохо" or phr1 == "Плохо":
        print("Очень жаль.")
        wud()
    else:
        print('Я тебя не понял.')

def hello():
    print('Привет!')
    phr = input()
    if phr == 'привет' or phr == 'Привет':
        hau()
    elif phr == 'пока' or phr == 'Пока':
        godb()
    else:
        print('Я тебя не понял.')

hello()
