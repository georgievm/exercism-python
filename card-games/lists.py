""" it's the statistics module, man """
import statistics

def get_rounds(number):
    return [number, number+1, number+2]

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    return rounds.count(number)

def card_average(hand):
    return sum(hand)/len(hand)

def approx_average_is_average(hand):
    avg = card_average(hand)
    method_1 = card_average([hand[0], hand[-1]])
    method_2 = statistics.median(hand)
    return avg in (method_1, method_2)

def average_even_is_average_odd(hand):
    avg_even = card_average(hand[::2])
    avg_odd = card_average(hand[1::2])
    return avg_even == avg_odd

def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] *= 2
    return hand
