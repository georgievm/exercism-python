def sum_of_multiples(limit, multiples):
    candidates = []
    for m in multiples:
        if m != 0:
            counter = 1
            while (counter * m) < limit:
                candidates += [counter * m]
                counter += 1
    
    return sum(set(candidates))