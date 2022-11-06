import math

def score(x, y):
    x = abs(x)
    y = abs(y)

    line = math.sqrt(x*x + y*y)
    if line > 10:
        return 0
    elif 5 < line <= 10:
        return 1
    elif 1 < line <= 5:
        return 5
    return 10
