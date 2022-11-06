def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
        
    is_prime = lambda n: all(n%i != 0 for i in range(2, int(n**.5)+1))
    prime_n = 1
    current_num = 2
    while True:
        prime = is_prime(current_num)
        if prime and prime_n == number:
            return current_num
        if prime:
            prime_n += 1
        current_num += 1
    