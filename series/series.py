def slices(series, length):
    CHECKS = {'length == 0': 'slice length cannot be zero',
             'length < 0': 'slice length cannot be negative',
             'not series': 'series cannot be empty',
             'length > len(series)': 'slice length cannot be greater than series length'}
    for expr, message in CHECKS.items():
        if eval(expr):
            raise ValueError(message)

    slices = []
    for i in range(0, len(series)):
        slice = series[i:i+length]
        if len(slice) < length:
            break
        slices.append(slice)
    return slices
