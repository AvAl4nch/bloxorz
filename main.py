import keyboard
from Player import Player
import os

canvas = [
    'VVVVVVVVVVVVVVVVVVVVVVVV',
    'VVVVVVVVVVVVVVVVVVVVVVVV',
    'VV████████████████████VV',
    'VV████████████████████VV',
    'VV████████████████████VV',
    'VV████████████████████VV',
    'VV████████████████████VV',
    'VV████████████████████VV',
    'VV████████████████████VV',
    'VV████████████████████VV',
    'VV████████████████████VV',
    'VV████████████████████VV',
    'VV████████████████████VV',
    'VV████████████████████VV',
    'VV████████████████████VV',
    'VVVVVVVVVVVVVVVVVVVVVVVV',
    'VVVVVVVVVVVVVVVVVVVVVVVV',
]


level = [
    '                        ',
    '                        ',
    '  ████████████████████  ',
    '  ████████████████████  ',
    '  ████████████████████  ',
    '  ████████████████████  ',
    '  ████████████████████  ',
    '  ███████████@████████  ',
    '  ████████████████████  ',
    '  ████████████████████  ',
    '  ████████████████████  ',
    '  ████████████████████  ',
    '  ████████████████████  ',
    '  ████████████████████  ',
    '  ████████████████████  ',
    '                        ',
    '                        ',
]

def render_level(level, player):
    temp_level = level.copy()


    x1, y1, x2, y2 = player.render()

    t1 = list(temp_level[x1])
    t1[y1] = '#'
    temp_level[x1] = ''.join(t1)

    t2 = list(temp_level[x2])
    t2[y2] = '#'
    temp_level[x2] = ''.join(t2)

    os.system('cls' if os.name == 'nt' else 'clear')

    for row in temp_level:
        for i in row:
            print(i, end=' ')
        print()


def check(player, level):
    x1, y1, x2, y2 = player.render()
    t1 = list(level[x1])[y1]
    t2 = list(level[x2])[y2]
    print(t1)
    print(t2)

    if t1 == ' ' or t2 == ' ':
        game_over()

    if t1 == t2 and t1 == '@':
        win()


def game_over():
    print('GAME OVER!')
    exit()

def win():
    print('WIN')
    exit()



def on_key_event(player, level, e):
    if e.event_type == keyboard.KEY_DOWN:
        match e.name:
            case 'w': player.move_up()
            case 's': player.move_down()
            case 'a': player.move_left()
            case 'd': player.move_right()

        check(player, level)
        render_level(level ,player)


if __name__ == '__main__':

    player = Player()

    render_level(level, player)

    keyboard.hook(lambda e: on_key_event(player, level, e))
    keyboard.wait('esc')

