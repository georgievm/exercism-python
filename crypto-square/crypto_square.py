def cipher_text(plain_text):
    if not plain_text:
        return ''
    # text normalization
    lst = [i.lower() for i in plain_text if i.isalnum()]

    # fill the rectangle
    r, c = get_rows_columns(len(lst))
    rectangle = [list(f"{''.join(lst[i*c:i*c+c]):<{c}}") for i in range(0, r)]

    # encoded message (unseparated)
    encoded = [''.join(i) for i in zip(*rectangle)]

    return ' '.join(encoded)

def get_rows_columns(length):
    for col in range(1, length+1):
        for row in range(1, col+1):
            if col - row <= 1 and col*row >= length:
                return row, col
