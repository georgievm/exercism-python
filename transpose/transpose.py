def transpose(lines):
    lines = lines.split('\n')
    line_lengths = [len(line) for line in lines]
    transposed = ['' for i in range(0, max(line_lengths))]

    # add spaces where needed
    lines_copy = lines.copy()
    for line_ind in range(0, len(lines)):
        if len(lines[line_ind]) < max(line_lengths[line_ind:]):
            lines_copy[line_ind] += ' '*(max(line_lengths[line_ind:])-len(lines[line_ind]))

    for line in lines_copy:
        for i in range(0, len(line)):
            transposed[i] += line[i]

    return '\n'.join(transposed)