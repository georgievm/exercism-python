def flatten(iterable):
    string = str(iterable)
    for item in ['[', ']', ', None', 'None, ', 'None']:
        string = string.replace(item, '')

    if string == '':
        return []
    return ([int(x) for x in string.split(', ')])
