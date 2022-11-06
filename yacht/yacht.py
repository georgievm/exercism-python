# Score categories.
# Change the values as you see fit.
YACHT = "yacht"
ONES = "1s"
TWOS = "2s"
THREES = "3s"
FOURS = "4s"
FIVES = "5s"
SIXES = "6s"
FULL_HOUSE = "full"
FOUR_OF_A_KIND = "4of_kind"
LITTLE_STRAIGHT = "little"
BIG_STRAIGHT = "big"
CHOICE = "choice"


def score(dice, category):
    if category == 'yacht':
        return 50*int(dice[0] == dice[1] == dice[2] == dice[3] == dice[4])
    if category == '1s':
        return 1*dice.count(1)
    if category == '2s':
        return 2*dice.count(2)
    if category == '3s':
        return 3*dice.count(3)
    if category == '4s':
        return 4*dice.count(4)
    if category == '5s':
        return 5*dice.count(5)
    if category == '6s':
        return 6*dice.count(6)
    if category == 'full':
        dice.sort()
        return sum(dice) * int(dice[0] == dice [1] and dice[3] == dice[4] and not dice[2] == dice[0] == dice[4])
    if category == '4of_kind':
        dice.sort()
        return int((dice.count(dice[0]) == 4 and dice.count(dice[4]) == 1) or (dice.count(dice[0]) == 1 and dice.count(dice[4]) == 4) or (dice[0] == dice[1] == dice[2] == dice[3] == dice[4])) * 4*dice[1]
    if category == 'little':
        dice.sort()
        return 30*int(dice == [1, 2, 3, 4, 5])
    if category == 'big':
        dice.sort()
        return 30*int(dice == [2, 3, 4, 5, 6])
    if category == 'choice':
        return sum(dice)
        
