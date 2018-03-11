import os
import time


def challenge1(number):
    """
    引数の二乗を返すぜ
    :param int number:
    :return:
    """
    if not isinstance(number, int):
        raise ValueError('数値型を入力してくだせえ')
    return number * number


def challenge2(string):
    """
    文字列を出力するよ
    :param string:
    :return:
    """
    if not isinstance(string, str):
        raise ValueError('文字列型を入力してくだせえ')
    print(string)


def challenge3(name, ext, path, isDirectory=False, wait=3):
    """
    引数いっぱいあるよ
    :param name:
    :param ext:
    :param path:
    :param isDirectory:
    :param wait:
    :return:
    """
    file_path = path + '/' + name + ext
    if isDirectory:
        os.mkdir(path)
        return None
    time.sleep(wait)
    with open(file_path, 'w') as f:
        f.write(' ')


def challenge4(num):
    def div2(number):
        """
        2で割るよ
        :param number:
        :return:
        """
        return number // 2

    def times4(number):
        """
        4をかけるよ
        :param number:
        :return:
        """
        return number * 4

    first = div2(num)
    print(times4(first))


def challenge5(string):
    """
    floatに変換するよ
    :param string:
    :return:
    """
    try:
        floated = float(string)
    except ValueError:
        print('数字を入力してくれ')
        return None
    print('浮動小数点型への変換に成功した！')
    return floated
