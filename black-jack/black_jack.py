"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    if card in ['J', 'Q', 'K']:
        return 10
    if card == 'A':
        return 1
    return int(card)

def higher_card(card_one, card_two):
    val_one = value_of_card(card_one)
    val_two = value_of_card(card_two)
    if val_one == val_two:
        return card_one, card_two
    if val_one > val_two:
        return card_one
    return card_two

def value_of_ace(card_one, card_two):
    if 'A' in [card_one, card_two]:
        if value_of_card(card_one) + value_of_card(card_two) + 10 + 11 <= 21:
            return 11
        else:
            return 1
    if value_of_card(card_one) + value_of_card(card_two) + 11 <= 21:
        return 11
    return 1

def is_blackjack(card_one, card_two):
    top = ['A', '10', 'J', 'Q', 'K']
    hand = [card_one, card_two]
    return card_one in top and card_two in top and hand.count('A') == 1

def can_split_pairs(card_one, card_two):
    hand = [card_one, card_two]
    return card_one == card_two or (hand.count('Q') == hand.count('K') == 1)

def can_double_down(card_one, card_two):
    return value_of_card(card_one)+value_of_card(card_two) in [9, 10, 11]
