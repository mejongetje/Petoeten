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