def is_paired(input_string):
    inp = ''
    for symbol in input_string:
        if symbol in ['(', ')', '{', '}', '[', ']']:
            inp += symbol
    brackets = ['[]', '{}', '()']
    while any(pair in inp for pair in brackets):
        for pair in brackets:
            inp = inp.replace(pair, '')

    return not bool(inp)