def annotate(minefield):
    if minefield == []:
        return []
    
    minefield = [[j for j in i] for i in minefield]
    
    # check for malformed input
    row_lengths = [len(row) for row in minefield]
    splitted = [j for i in minefield for j in i]
    other_chars_count = sum(i not in [' ', '*'] for i in splitted)
    
    if (len(set(row_lengths)) != 1 or other_chars_count > 0):
        raise ValueError("The board is invalid with current input.")

    # replace with the count of adjacent mines
    new_minefield = []
    last_col_ind = row_lengths[0] - 1
    last_row_ind = len(minefield) - 1
    
    for i in range(len(minefield)):
        new_minefield.append('')
        for j in range(len(minefield[0])):
            if minefield[i][j] == '*':
                new_minefield[i] += '*'
            else:
                adj_to_current = []
                
                if i != 0 and j != 0: # up-left
                    adj_to_current.append(minefield[i-1][j-1])
                if i != 0: # up
                    adj_to_current.append(minefield[i-1][j])
                if i != 0 and j != last_col_ind: # up-right
                    adj_to_current.append(minefield[i-1][j+1])
                if j != 0: # left
                    adj_to_current.append(minefield[i][j-1])
                if j != last_col_ind: # right
                    adj_to_current.append(minefield[i][j+1])
                if i != last_row_ind and j != 0: # bottom-left
                    adj_to_current.append(minefield[i+1][j-1])
                if i != last_row_ind: # bottom
                    adj_to_current.append(minefield[i+1][j])
                if i != last_row_ind and j != last_col_ind: # bottom-right
                    adj_to_current.append(minefield[i+1][j+1])

                adj_mine_count = adj_to_current.count('*')
                if (adj_mine_count > 0):
                    new_minefield[i] += str(adj_mine_count)
                else:
                    new_minefield[i] += ' '
    
    return new_minefield