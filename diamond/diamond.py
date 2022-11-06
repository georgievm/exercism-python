import string

def rows(letter):
    alphabet = string.ascii_uppercase
    diamond, pos = [], alphabet.index(letter)

    for i in range(pos + 1):
        outer_sp = ' ' * (pos - i)
        inner_sp = ' ' * (i*2 - 1 if i != 0 else 0)
        letter_2 = alphabet[i] if i != 0 else ''

        diamond += [outer_sp + alphabet[i] + inner_sp + letter_2 + outer_sp]

    return diamond + diamond[-2::-1]
