import itertools

def show_cards(hand):
    i = 1
    strng = ' '
    for card in hand:
        strng += '['+str(i)+']' + ' ' + card.name + ' '
        i += 1
    return strng

def print_hand(hand):
    strng = ' '
    for card in hand:
        strng += '|' + card.name
    return strng


def whos_turn(players, pos):
    for player in players:
        if player.hand_position == pos % 3:
            return player


def human_play(player, card_ind):
    player.showcard = None
    player.showcard = player.hand[card_ind-1]
    player.hand.remove(player.showcard)
    return player.showcard
    

def computer_play(player, round, trickcards):
    if player.hand_position != 0:
        suit = trickcards[0].suit
        playersuit = [card for card in player.hand if card.suit == suit]
        if playersuit:
            player.showcard = next(card for card in player.hand if card.suit == suit)
        else:
            player.showcard = player.hand[0]
    else:
        player.showcard = player.hand[0]
    player.hand.remove(player.showcard)
    player.dummycards[round-1] = ' '
    return player.showcard


def trick_win(players, cards, trump):
    suits = [card.suit for card in cards]
    if trump.suit in suits:
        rank = max([card for card in cards if card.suit == trump.suit], key=lambda card: card.rank)
        candidate_players = [player for player in players if player.showcard.suit == trump.suit]
        winner = [player for player in players if player.showcard == rank]
        return winner[0]
    else:
        key_suit = cards[0].suit 
        candidate_cards = [card for card in cards if card.suit == key_suit]
        candidate_players = [player for player in players if player.showcard.suit == key_suit]
        highest_rank = max(candidate_cards, key=lambda x: x.rank)
        winner = [player for player in candidate_players if player.showcard == highest_rank]
        return winner[0]

def add_trickpoints(winner, cards):
    points = sum([card.rank for card in cards])
    winner.trickpoints += points


def hand_win(players):
    winner = max([player for player in players], key=lambda player: player.trickpoints)
    return winner


def position_update(players, winner):
    winner.hand_position = 0
    if winner == players[0]:
        players[1].hand_position = 1
        players[2].hand_position = 2
    elif winner == players[1]:
        players[2].hand_position = 1
        players[0].hand_position = 2
    elif winner == players[2]:
        players[0].hand_position = 1
        players[1].hand_position = 2


    
