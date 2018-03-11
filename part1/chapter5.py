
FAVORITE_ARTIST = [
    '山下達郎',
    'Greeen',
    '宇多田ヒカル',
    'ゲスの極み乙女',
    'Ed Sheeran',
]

LOCATION_VISITED = [
    (39.72, 140.10),
    (39.69, 140.12),
    (42.98, 144.38),
    (43.19, 140.99),
    (38.26, 140.86),
    (35.86, 139.60),
]


MY_INFO = {
    'height': 180,
    'weight': 55,
    'favorite': 'python',
    'music': 'やまたつ',
    'actor': '松田龍平',
}


def search_dict(key):
    try:
        data = MY_INFO[key]
    except KeyError:
        print('キーなし')
        return None
    print('マッチした値は{}。'.format(data))
    return data


FAVORITE_ARTIST_MUSIC = [
    '蒼氓',
    'Story',
    'あなた',
    '両成敗',
    'Perfect'
]

FAVORITE_ARTIST_INFO = {}
for artist, music in zip(FAVORITE_ARTIST, FAVORITE_ARTIST_MUSIC):
    FAVORITE_ARTIST_INFO[artist] = music
print(FAVORITE_ARTIST_INFO)


def setter():
    even = {2, 4, 6, 8, 10}
    minimum = {1, 2, 3}
    print('和集合: ', even | minimum)
    print('差集合: ', even - minimum)
    print('積集合: ', even & minimum)
    print('対称差: ', even ^ minimum)
