def saddle_points(matrix):
    result = []
    if not matrix:
        return result
    if len(set([len(row) for row in matrix])) != 1:
        raise ValueError("irregular matrix")

    transposed = list(zip(*matrix))
    for row_i, row in enumerate(matrix):
        for col_i, el in enumerate(row):
            if el == max(row) and el == min(transposed[col_i]):
                result.append({'row': row_i+1, 'column': col_i+1})
                
    return result
