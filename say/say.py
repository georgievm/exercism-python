def say(number):
    # input data validation
    if not 0 <= number <= 999999999999:
        raise ValueError('input out of range')

    # split num into chunks of 3-digit strings
    chunks_of_3 = f"{number:,}".split(',')

    # add chunk num in words + corresponding scale word to list
    text, scale_words = [], ['', ' thousand', ' million', ' billion']
    for i, chunk in enumerate(chunks_of_3):
        if chunk != '000':
            scale_word = scale_words[len(chunks_of_3)-i-1]
            text += [chunk_to_text(chunk) + scale_word]

    return ' '.join(text)

def chunk_to_text(chunk):
    to_twenty = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
        'seventeen', 'eighteen', 'nineteen']
    by_tens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
        7: 'seventy', 8: 'eighty', 9: 'ninety'}
    text = []
    dig_1, dig_2, dig_3 = chunk[-3:-2], chunk[-2:-1], chunk[-1:]
    
    if dig_1 and dig_1 != '0':
            text += [f'{to_twenty[int(dig_1)]} hundred']
    if dig_2 + dig_3 != '00':
        if 0 <= int(dig_2 + dig_3) <= 19:
            text += [to_twenty[int(dig_2 + dig_3)]]
        else:
            ones = f'-{to_twenty[int(dig_3)]}' if dig_3 != '0' else ''
            text += [by_tens[int(dig_2)] + ones]

    return ' '.join(text)
