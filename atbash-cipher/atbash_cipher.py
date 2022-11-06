def encode(plain_text):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    plain_text = plain_text.lower()
    for symbol in plain_text:
        if symbol in [' ', '.', ',']:
            plain_text = plain_text.replace(symbol, '')
    encoded = ''
    counter = 0
    for symbol in plain_text:
        if symbol.isalpha():
            encoded += alpha[-alpha.index(symbol)-1]
        else:
            encoded += symbol
        counter += 1
        if counter % 5 == 0 and plain_text.index(symbol) != len(plain_text)-1:
            encoded += ' '
    return encoded

def decode(ciphered_text):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    ciphered_text = ciphered_text.replace(' ', '')
    decoded = ''
    for symbol in ciphered_text:
        if symbol.isalpha():
            decoded += alpha[-alpha.index(symbol)-1]
        else:
            decoded += symbol
    return decoded
