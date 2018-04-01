# 手続き型プログラミングの例

pop = []
jpop = []


def collect_songs():
    song = '曲名を入力してください'
    ask = 'pかjのどちらかを入力してください。qで終了します。'

    while True:
        genre = input(ask)
        if genre == 'q':
            break

        if genre == 'p':
            p = input(song)
            pop.append(p)

        elif genre == 'j':
            j = input(song)
            jpop.append(j)

        else:
            print('不正な値です。')

    print('pop songs: ', pop)
    print('jpop songs: ', jpop)


class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print('Created!')

    def rot(self, days, temp):
        self.mold = days * temp


class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l


if __name__ == '__main__':
    collect_songs()
    or1 = Orange(10, 'dark orange')
    print(or1.color)
    rectangle = Rectangle(10, 20)
    print(rectangle.area())
    rectangle.change_size(20, 40)
    print(rectangle.area())
