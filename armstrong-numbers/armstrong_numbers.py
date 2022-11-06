def is_armstrong_number(number):
    result = 0
    for i in str(number):
     result += int(i)**len(str(number))
    return number == result
