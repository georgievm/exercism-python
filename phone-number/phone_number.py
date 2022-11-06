class PhoneNumber:
    def __init__(self, number):
        num = number

        # check for letters & punctuations
        letters = [i for i in num if i.isalpha()]
        punctuations = [i for i in num if not i.isalnum() and i not in '+-(). ']
        if letters:
            raise ValueError("letters not permitted")
        if punctuations:
            raise ValueError("punctuations not permitted")

        # remove non-digits
        num = ''.join([i for i in num if i.isdigit()])
        
        # check length
        if len(num) < 10:
            raise ValueError("incorrect number of digits")
        if len(num) > 11:
            raise ValueError("more than 11 digits")
        if len(num) == 11:
            if not num.startswith('1'):
                raise ValueError("11 digits must start with 1")
            num = num[1:]

        # check area & exchange codes
        for n, word in ('0', 'zero'), ('1', 'one'):
            if num[0] == n:
                raise ValueError(f"area code cannot start with {word}")
            if num[3] == n:
                raise ValueError(f"exchange code cannot start with {word}")
                
        self.number = num
        self.area_code, self.exchange_code, self.subscr_code = num[:3], num[3:6], num[6:]
        
    def pretty(self):
        return f'({self.area_code})-{self.exchange_code}-{self.subscr_code}'