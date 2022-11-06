def primes(limit):
    nums = set(range(2, limit+1))
    non_primes = {j for n in nums for j in range(n*2, limit+1, n)}
    primes = sorted(nums - non_primes)
    return primes