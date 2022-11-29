def spiral_matrix(size):
    if size == 0: return []

    # generate empty matrix
    placeholder = '#'
    matrix = [size*[placeholder] for _ in range(size)]

    pre_try, pre_row, pre_col = 'right', 0, 0

    # functions for the [right, down, left, up] directions
    def try_right(num):
        nonlocal pre_col, pre_try
        if pre_col == size-1 or matrix[pre_row][pre_col+1] != placeholder:
            try_down(num)
        else:
            pre_col += 1
            matrix[pre_row][pre_col] = num
            pre_try = 'right'

    def try_down(num):
        nonlocal pre_row, pre_try
        if pre_row == size-1 or matrix[pre_row+1][pre_col] != placeholder:
            try_left(num)
        else:
            pre_row += 1
            matrix[pre_row][pre_col] = num
            pre_try = 'down'

    def try_left(num):
        nonlocal pre_col, pre_try
        if pre_col == 0 or matrix[pre_row][pre_col-1] != placeholder:
            try_up(num)
        else:
            pre_col -= 1
            matrix[pre_row][pre_col] = num
            pre_try = 'left'

    def try_up(num):
        nonlocal pre_row, pre_try
        if pre_row == 0 or matrix[pre_row-1][pre_col] != placeholder:
            try_right(num)
        else:
            pre_row -= 1
            matrix[pre_row][pre_col] = num
            pre_try = 'up'
    
    matrix[0][0] = 1
    for num in range(2, size**2+1):
        eval('try_' + pre_try + '(num)')

    return matrix