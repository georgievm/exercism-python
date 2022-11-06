def is_isogram(string):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alpha:
        if string.lower().count(letter) > 1:
            return False
    return True
