def encode(message, rails):
    enc_rows = ['' for i in range(rails)]
    # generate a list with zig-zag row positions
    row_pos = generate_row_positions(message, rails)
        
    # put each letter in the appropriate row
    for index, letter in enumerate(message):
        enc_rows[row_pos[index]] += letter
    
    return ''.join(enc_rows)

def decode(message, rails):
    # generate a list with zig-zag row positions
    row_pos = generate_row_positions(message, rails)

    # create a matrix with symbols to replace afterwards
    matrix = []
    for letter_ind in range(len(message)):
        to_append = []
        for i in range(rails):
            if i == row_pos[letter_ind]:
                to_append.append('#')
            else:
                to_append.append('')
        matrix.append(to_append)

    # reverse the matrix
    rev_matrix = []
    for i in range(rails):
        to_append = []
        for j in range(len(message)):
            to_append.append(matrix[j][i])
        rev_matrix.append(to_append)

    # unpack the rev_metrix
    matrix = [j for i in rev_matrix for j in i]

    # replace # in matrix with the appropriate letter
    message_lst = [item for item in message]
    for item_ind, item in enumerate(matrix):
        if item == '#':
            matrix[item_ind] = message_lst.pop(0)

    # assemble the decoded text
    decoded = ''
    for i in range(len(message)):
        row_str = ''
        for rail_ind in range(rails):
            row_str += matrix[(rail_ind * len(message)) + i]
        decoded += row_str
    
    return decoded

def generate_row_positions(message, r):
    row_pos = [0]
    while len(row_pos) < len(message):
        row_pos.extend(list(range(1, r))) if row_pos[-1] == 0 else row_pos.extend(list(range(r-2, -1, -1)))
    return row_pos
