def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10 or (not isbn[-1].isdigit() and isbn[-1] != 'X'):
        return False
    sum = 0
    for i in range(0, 10):
        if i != 9 and not isbn[i].isdigit():
            return False
        if isbn[i] == 'X':
            sum += 10 * (10-i)
        else:
            sum += int(isbn[i]) * (10-i)
    return sum % 11 == 0
