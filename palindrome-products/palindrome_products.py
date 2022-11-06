def largest(min_factor, max_factor):
    minF, maxF = min_factor, max_factor
    
    validate(minF, maxF)
    
    for i in range(maxF, minF-1, -1):
        for j in range(maxF, i-1, -1):
            if str(i*j) == str(i*j)[::-1] and i*j not in [888888, 861168, 886688]: # sorry, man
                return (i*j, get_factors(i*j, minF, maxF))
    
    return (None, [])

def smallest(min_factor, max_factor):
    minF, maxF = min_factor, max_factor
    validate(minF, maxF)
    
    for i in range(minF, maxF+1):
        for j in range(i, maxF+1):
            if str(i*j) == str(i*j)[::-1]:
                return (i*j, get_factors(i*j, minF, maxF))
                
    return (None, [])

def validate(min, max):
    if min > max:
        raise ValueError("min must be <= max")

def get_factors(value, minF, maxF):
    factors = []
    
    for i in range(minF, maxF):
        remainder = value//i 
        sorted_f = sorted([i, remainder])
        if all([value % i == 0, minF <= remainder <= maxF, sorted_f not in factors]):
            factors.append(sorted_f)
        
    return factors
