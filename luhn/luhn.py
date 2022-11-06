class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        # strip the spaces
        self.card_num = self.card_num.replace(' ', '')

        # validate the number
        if len(self.card_num) < 2 or not self.card_num.isdigit():
            return False

        rev_list = list(map(int, list(self.card_num)))[::-1]
        for i in range(1, len(rev_list), 2):
            product = rev_list[i]*2
            rev_list[i] = product - 9 if product > 9 else product

        return sum(rev_list) % 10 == 0
        