import os

import classes
from header import header


os.system('cls')

hand = classes.Board()
dummy = ['X']*6
empty = ' '

for _ in range(3):
# TABLE LAYOUT
    header()
    print('|--------------------------------------------|')
    print(f'|\t\t    |{dummy[3]}|{dummy[4]}|{dummy[5]}|\t\t     |')
    print('|                                            |')
    print(f'|\t\t     |{hand.hand[3]}|\t\t     |')
    print('|                                            |')
    print(f'| |{dummy[2]}|                                        |')
    print(f'| |{dummy[1]}| |{hand.hand[4]}|\t\t\t\t|{hand.hand[5]}| |')
    print(f'| |{dummy[0]}|                                        |')
    print('|                                            |')
    print(f'|\t\t     |{hand.hand[2]}|\t\t     |')
    print('|                                            |')
    print(f'|\t\t  |{hand.hand[0]}|{hand.hand[1]}|{hand.hand[2]}|\t\t     |')
    print(' -------------------------------------------- ')

    inp = input('Press enter to continue: ')
    if inp == 'y':
        dummy[3] = ' '
        dummy[1] = ' '

    os.system('cls')



