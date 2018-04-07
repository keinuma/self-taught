import re
import this


def challenge1():
    string = this.s
    m = re.findall('Dutch', string, re.IGNORECASE)
    print(m)


def challenge2():
    s = 'Arizona 479, 501, 870. California 209, 213, 653'
    m = re.findall('\d', s)
    print(m)


def challenge3():
    s = 'The ghost that says boo haunts the loo'
    m = re.findall('.oo', s)
    print(m)


if __name__ == '__main__':
    challenge1()
    challenge2()
    challenge3()
