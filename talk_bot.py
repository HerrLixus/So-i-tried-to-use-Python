def godb():
    print('Ну ладно, пока.')

def wud():
    print("Чем занимаешься?")
    phr2 = input()
    print('Круто. как продвигается работа?')
    phr3 = input()
    if phr3 == "хорошо":
        print("Найс. Удачи.")
    elif phr3 == "Хорошо":
        print("Найс. Удачи.")
    elif phr3 == "нормально":
        print("Найс. Удачи.")
    elif phr3 == "Нормально":
        print("Найс. Удачи.")
    elif phr3 == "плохо":
        print("Может, тебе стоит отдохнуть?")
    elif phr3 == "Плохо":
        print("Может, тебе стоит отдохнуть?")
    else:
        print('Я тебя не понял.')

def hau():
    print('Как дела?')
    phr1 = input()
    if phr1 == "хорошо":
        print("Это хорошо.")
        wud()
    elif phr1 == "Хорошо":
        print("Это хорошо.")
        wud()
    elif phr1 == "нормально":
        print("Это хорошо.")
        wud()
    elif phr1 == "Нормально":
        print("Это хорошо.")
        wud()
    elif phr1 == "плохо":
        print("Очень жаль.")
        wud()
    elif phr1 == "Плохо":
        print("Очень жаль.")
        wud()
    elif phr1 == "Норм":
        print("Это хорошо.")
        wud()
    elif phr1 == "норм":
        print("Это хорошо.")
        wud()
    else:
        print('Я тебя не понял.')


def hello():
    print('Привет!')
    phr = input()
    if phr == 'привет':
        hau()
    elif phr == 'Привет':
        hau()
    elif phr == 'пока':
        godb()
    elif phr == 'Пока':
        godb()
    else:
        print('Я тебя не понял.')
hello()