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


if __name__ == '__main__':
    collect_songs()