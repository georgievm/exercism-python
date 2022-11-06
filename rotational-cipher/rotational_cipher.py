def rotate(text, key):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    rotated = ''
    for symbol in text:
        if symbol.isalpha():
            if symbol != symbol.lower():
                rotated += alpha[(alpha.index(symbol.lower())+key)%26].upper()
            else:
                rotated += alpha[(alpha.index(symbol.lower())+key)%26]
        else:
            rotated += symbol
    return rotated
