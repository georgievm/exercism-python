def score(word):
    values = [('AEIOULNRST', 1), ('DG', 2), ('BCMP', 3), ('FHVWY', 4), ('K', 5), ('JX', 8), ('QZ', 10)]
    dict = {i:v for k, v in values for i in k}
    score = 0
    for letter in word:
        score += dict[letter.upper()]
    return score
