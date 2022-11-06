def is_pangram(sentence):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alpha:
        if sentence.lower().count(letter) == 0:
            return False
    return True
