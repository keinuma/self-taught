def challenge1():
    string = 'カミュ'
    for i in string:
        print(i)


def challenge2():
    string1 = input('一つ目の文字列を入力してね')
    string2 = input('二つ目の文字列を入力してね')
    formater = '私は昨日{}を書いて、{}に送った'
    print(formater.format(string1, string2))


def challenge3():
    string = 'aldous Huxley was born in 1894.'
    string = string[0].upper() + string[1:]
    print(string)


def challenge4():
    string = 'どこで？ だれが？ いつ？'
    print(string.split(' '))


def challenge5():
    target = [
        'The',
        'fox',
        'jumped',
        'over',
        'the',
        'fence',
        '.'
    ]
    string = ' '.join(target)
    print(string.replace(' .', '.'))


def challenge6():
    string = 'A screaming comes across the sky.'
    print(string.replace('s', '$'))


def challenge7():
    string = 'Hemingway'
    print(string.index('m'))


def challenge8():
    string = 'お前はすでに\'死んでいる\''
    print(string)


def challenge9():
    string = 'three '
    hey = string * 3
    print(hey.rstrip())


def challenge10():
    string = '四月の晴れた寒い日で、時計がどれも十三時を打っていた。'
    inner_string = string.split('、')[0]
    print(inner_string)
