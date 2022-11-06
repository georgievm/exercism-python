def factors(value):
    factors, f = [], 2
    while value != 1:
        if value % f == 0:
            factors.append(f)
            value /= f
        else:
            f += 1
            
    return factors