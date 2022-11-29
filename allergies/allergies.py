ALLERGENS = ['cats', 'pollen', 'chocolate', 'tomatoes', 'strawberries', 'shellfish', 'peanuts', 'eggs']

class Allergies:

    def __init__(self, score):
        self.score = score % 256
    
    def allergic_to(self, item):
        return item in self.lst

    @property # getter here
    def lst(self):
        lst = []
        score = self.score
        for i, allergen in enumerate(ALLERGENS):
            if (value := 2**(7-i)) <= score:
                lst.append(allergen)
                score -= value
        return lst
