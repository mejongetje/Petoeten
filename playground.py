import os
from copy import copy

import classes
import utils
from header import header


os.system('cls')

header()
inp0 = input('Press enter to play. ')
os.system('cls')

game = classes.Board()
p3 = classes.Player('mejongetje', 'human')
classes.p1.hand, classes.p2.hand, p3.hand = game.hand[0], game.hand[1], game.hand[2]

empty = ' '
loc_d1, loc_d2, loc_d3 = ' ', ' ', ' '
loc_s1, loc_s2, loc_s3 = ' ', ' ', ' '
trump = game.trump
tabs = '\t'
pos = 0
round = 1
trick_cards = []
hand = True

while hand:
    # TABLE LAYOUT
    header()
    print('|--------------------------------------------|')
    print('|                UNCLE DANNY                 |')
    print('|--------------------------------------------|')
    print(f'| A |\t\t {loc_d2}:{loc_s2} |{classes.p2.dummycards[0]}|{classes.p2.dummycards[1]}|{classes.p2.dummycards[2]}|\t\t     |')
    print('| U |                                        |')
    print(f'| N |\t\t     |{classes.p2.showcard}|\t\t     |')
    print('| T |                                        |')
    print(f'|   |  |{classes.p1.dummycards[0]}|                          TRUMP:   |')
    print(f'| S |  |{classes.p1.dummycards[1]}|   |{classes.p1.showcard}|\t\t     |{trump[0]}|    |')
    print(f'| H |  |{classes.p1.dummycards[2]}|                                   |')
    print(f'| E |    {loc_d1}:{loc_s1}                                 |')
    print(f'| I |\t\t     |{p3.showcard}|\t\t     |')
    print('| L |                                        |')
    print(f'| A |\t\t {utils.print_hand(p3.hand)}| {loc_d3}:{loc_s3}\t{tabs if len(p3.hand) < 3 else empty}     |')
    print('|--------------------------------------------|')
    print('|                 MEJONGETJE                 |')
    print(' -------------------------------------------- ')

    if pos % 3 == 0 and pos != 0:
        round += 1
        trick_winner = utils.trick_win(classes.Player.players, trick_cards, trump[0])
        utils.add_trickpoints(trick_winner, trick_cards)
        print(f'Winner of the trick is {trick_winner}.')
        trick_cards = []
        classes.p1.showcard, classes.p2.showcard, p3.showcard = ' ', ' ', ' '
        utils.position_update(classes.Player.players, trick_winner)
        if round == 4:
            hand_winner = utils.hand_win(classes.Player.players)
            print(f'Winner of the hand is {hand_winner}')
            hand = False
            break

    player = utils.whos_turn(classes.Player.players, pos)

    if player.type == 'human':
        len_hand = len(player.hand)
        while True:
            try:
                card_inp = int(input(f'Make your choice: {utils.show_cards(p3.hand)}'))
                if card_inp <= len_hand and type(card_inp) == int:
                    break
            except:
                pass
        player.showcard = utils.human_play(player, card_inp)
        trick_cards.append(player.showcard)
        pos += 1
        inp5 = input('Click enter to continue')
        os.system('cls')
    else:
        player.showcard = utils.computer_play(player, round, trick_cards)
        trick_cards.append(player.showcard)
        pos += 1
        inp5 = input("Click enter to continue")
        os.system('cls')
    



