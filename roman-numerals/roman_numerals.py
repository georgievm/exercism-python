def roman(number):
    roman_nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_symb = 'M CM D CD C XC L XL X IX V IV I'
    remainder, result = number, ''

    while remainder != 0:
        for i, base_value in enumerate(roman_nums):
            if remainder >= base_value:
                quotient = remainder // base_value
                remainder = remainder % base_value

                result += roman_symb.split(' ')[i] * quotient

    return result
