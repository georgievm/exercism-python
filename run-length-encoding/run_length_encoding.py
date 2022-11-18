def decode(string):
    if not string:
        return ''
    lst = [i+',' if i.isalpha() or i == ' ' else i for i in list(string[:-1])]
    splitted = ''.join(lst + [string[-1:]]).split(',')
    decoded = ''
    for i in splitted:
        decoded += i if len(i) == 1 else int(i[:-1])*i[-1:]
    return decoded

def encode(string):
    lst = [sym if sym == string[i] else f',{sym}' for i, sym in enumerate(string[1:])]
    splitted = (string[:1] + ''.join(lst)).split(',')
    encoded = ''.join(f'{len(s) if len(s) > 1 else ""}{s[:1]}' for s in splitted)
    return encoded
