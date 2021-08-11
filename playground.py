import os
from copy import copy

import classes
import utils
from header import header


os.system('cls')

game = classes.Board()
hand = game.hand[:]
dummy = ['X']*6
empty = ' '
show_card, show_card_c1, show_card_c2 = ' ', ' ', ' '
trump = game.trump
tabs = '\t'

for _ in range(3):
# TABLE LAYOUT

    header()
    print('|--------------------------------------------|')
    print(f'|\t\t d|s |{dummy[3]}|{dummy[4]}|{dummy[5]}|\t\t     |')
    print('|                                            |')
    print(f'|\t\t     |{show_card_c2}|\t\t     |')
    print('|                                            |')
    print(f'| |{dummy[0]}|                                        |')
    print(f'| |{dummy[1]}|   |{show_card_c1}|\t\t\t     |{trump}|    |')
    print(f'| |{dummy[2]}|                                        |')
    print('|  d|s                                       |')
    print(f'|\t\t     |{show_card}|\t\t     |')
    print('|                                            |')
    print(f'|\t\t  {utils.print_hand(hand)} d|s\t{tabs if len(hand) < 3 else empty}     |')
    print(' -------------------------------------------- ')


    card_played = int(input(f'Make your choice: {utils.show_cards(hand)}: '))
    show_card = hand.pop(card_played-1)






    os.system('cls')



