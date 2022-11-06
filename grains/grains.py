def square(number):
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)

def total():
    total = 1
    for i in range(1, 64):
        total += 2**i
    return total
