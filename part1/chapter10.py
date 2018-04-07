"""
hangman game
>> from chapter10 import hangman
>> hangman()
"""

from random import choice


def hangman():
    word_list = [
        'king',
        'animal',
        'baseball',
        'basketball',
        'yang'
    ]
    word = choice(word_list)
    wrong = 0
    stages = [
        '',
        '----------          ',
        '|                   ',
        '|        |          ',
        '|        o          ',
        '|       /|\\         ',
        '|       / \\         ',
        '|                   '
    ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('ハングマンへようこそ！')

    while wrong < len(stages) - 1:
        print('\n')
        char = input('一文字を予想してね')
        if len(char) > 1:
            print('一文字だけだぞ')
            continue
        if char in rletters:
            index = rletters.index(char)
            board[index] = char
            rletters[index] = '?'
        else:
            wrong += 1
        print(''.join(board))
        print('\n'.join(stages[:wrong+1]))
        if '_' not in board:
            print('あなたの勝ち！')
            print(word)
            win = True
            break
    if not win:
        print('\n'.join(stages[:wrong+1]))
        print('あなたの負け。正解は{}。'.format(word))
