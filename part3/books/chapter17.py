import re

zen = """Although never is
often better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be a good
idea. Namespaces
are one honking
great idea -- let's
do more of those!
"""

text = """キリンは大昔から __複数名詞__ の興味の対象でした。
キリンは __複数名詞__ のなかで一番背が高いですが、科学者たちは
そのような長い __体の一部__ をどうやって獲得したのか説明できません。
キリンの身長は __数値__ __単位__ 近くあり、その高さはほとんどは
脚と __体の一部__ によるものです。
"""


def simple_match():
    l = 'Beautiful is better than ugly'
    matches = re.findall('beautiful', l, re.IGNORECASE)
    print(matches)


def caret_match():
    m = re.findall('^If', zen, re.MULTILINE)
    print(m)


def strings_match():
    string = "Two too."
    m = re.findall('t[wo]o', string, re.IGNORECASE)
    print(m)


def number_match():
    line = '123 hi 34 hello.'
    m = re.findall('\d', line, re.IGNORECASE)
    print(m)


def not_greedy_match():
    t = '__one__ __two__ __three__'
    found = re.findall('__.*?__', t)
    for match in found:
        print(match)


def mad_libs(mls):
    """
    :param mls: 文字列でユーザに入力してもらいたい単語（=ヒント）
    の部分は後を2つのアンダースコアで挟んでください。ヒントの単語
    にはアンダースコアを含めないでください。 __hint__hint__ は
    ダメです。 __hint__ はOKです、
    """
    hints = re.findall(("__.*?__"), mls)
    if hints is not None:
        for word in hints:
            q = "{} を入力:".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print(mls)
    else:
        print("引数mlsが無効です")


def escape():
    line = 'I love $'
    m = re.findall('\\$', line, re.IGNORECASE)
    print(m)


if __name__ == '__main__':
    simple_match()
    caret_match()
    strings_match()
    number_match()
    not_greedy_match()
    mad_libs(text)
    escape()
