def abbreviate(words):
    words = words.replace('-', ' ')
    non_alphas = [sym for sym in words if not sym.isalpha() and sym != ' ']
    for sym in non_alphas:
        words = words.replace(sym, '')
    abbr = list(map(lambda x: x[0:1].upper(), words.split(' ')))
    return ''.join(abbr)
