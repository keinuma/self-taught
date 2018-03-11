import csv


def challenge1():
    with open('./data/2005_data.csv', 'r') as f:
        data = f.read()
    print(data)


def challenge2():
    with open('./data/answer.txt', 'w', encoding='utf-8') as f:
        qa = input('好きな食べ物は？')
        f.write(qa)


def challenge3():
    data = [
        ['Top Gun', 'Risky Business', 'Minority Report'],
        ['Titanic', 'The Revenant', 'Inception'],
        ['Training Day', 'Man on Fire', 'Flight']
    ]
    with open('./data/movies.csv', 'w') as f:
        writer = csv.writer(f, delimiter=',')
        for row in data:
            writer.writerow(row)


def challenge4():
    data = [
        ['トップガン', '卒業白書', 'マイノリティ・レポート'],
        ['タイタニック', 'レヴィナント', 'インセプション'],
        ['トレーニングデイ', 'マイ・ボディガード', 'フライト']
    ]
    with open('./data/movies_ja.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        for row in data:
            writer.writerow(row)

