from functools import reduce

def largest_product(series, size):
    if size == 0:
        return 1
    slices = get_slices(series, size)
    products = [reduce(lambda a, b: int(a)*int(b), list(s)) for s in slices]
    return max(products)

def get_slices(series, length):
    CHECKS = {'length > len(series)': 'span must be smaller than string length',
              'length < 0': 'span must not be negative',
             'not series.isnumeric()': 'digits input must only contain digits'}
    
    for expr, message in CHECKS.items():
        if eval(expr): raise ValueError(message)

    slices = []
    for i in range(0, len(series)):
        if len(slice:=series[i:i+length]) < length: break
        slices.append(slice)
    return slices