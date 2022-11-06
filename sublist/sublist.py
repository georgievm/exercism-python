"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 'A is a sublist of B'
SUPERLIST = 'A is a superist of B'
EQUAL = 'A and B are equal'
UNEQUAL = 'A and B are unequal'


def sublist(list_one, list_two):
    separ = '-'
    str_1 = list_2 = ''
    if ''.join(map(str, list_one)) != '':
        str_1 = separ + separ.join(map(str, list_one)) + separ
    if ''.join(map(str, list_two)) != '':
        list_2 = separ + separ.join(map(str, list_two)) + separ

    if str_1 == list_2:
        return EQUAL
    if str_1 in list_2:
        return SUBLIST
    if list_2 in str_1:
        return SUPERLIST
    return UNEQUAL
