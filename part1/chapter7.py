def challenge1():
    target = [
        'ウォーキング・デッド',
        'アントラージュ',
        'ザ・ソプラノズ',
        'ヴァンパイア・ダイアリーズ',
    ]
    for i in target:
        print(i)


def challenge2():
    for num in range(25, 51):
        print(num)


def challenge3():
    target = [
        'ウォーキング・デッド',
        'アントラージュ',
        'ザ・ソプラノズ',
        'ヴァンパイア・ダイアリーズ',
    ]
    for i, string in enumerate(target):
        print(i, string)


def challenge4():
    numbers = [1, 4, 5, 7, 10]
    while True:
        num = input('数字を入力してね: ')
        if num == 'q':
            break
        try:
            num = int(num)
        except ValueError:
            print('数字を入力するか、qで終了します')
            continue
        if num in numbers:
            print('正解')
            break
        else:
            print('不正解')


def challenge5():
    a = [8, 19, 148, 4]
    b = [9, 1, 33, 83]
    result = []
    for i, j in zip(a, b):
        result.append(i * j)
    print(result)
    return result
