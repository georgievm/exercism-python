def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    if sum == number:
        return 'perfect'
    if sum > number:
        return 'abundant'
    return 'deficient'
