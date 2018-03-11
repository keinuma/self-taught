def challenge1():
    string1 = 'モンキー'
    string2 = 'セクション２'
    string3 = 'ok'
    print(string1)
    print(string2)
    print(string3)


def challenge2():
    try:
        number = int(input('好きな数字を入力してね。: '))
    except ValueError:
        print('数字を入力しろよ')
        return None
    if number < 10:
        print('弱小かよ')
    else:
        print('まあまあだな')


def challenge3():
    try:
        number = int(input('好きな数字を入力しろよな。: '))
    except ValueError:
        print('数字を入れてくだせえ')
        return None
    if number <= 10:
        print('鍛え直し')
    elif 10 < number <= 25:
        print('もう一声')
    else:
        print('よくやった')


def challenge4(a=2, b=12):
    remainder = a % b
    print('余りは{}だった'.format(remainder))


def challenge5(a=4, b=19):
    quotient = a // b
    print('商は{}だった'.format(quotient))


def challenge6():
    age = input('君は何歳かな: ')
    try:
        age = int(age)
    except ValueError:
        print('歳を入れましょうね')
        return None
    if age <= 10:
        print('若いな…')
    elif 10 < age <= 30:
        print('青年よ')
    elif 30 < age <= 50:
        print('働きすぎるなよ')
    else:
        print('後何年')
