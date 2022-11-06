def commands(binary_str):
    handshake = ['wink', 'double blink', 'close your eyes', 'jump']
    bin = int(binary_str)
    while (bin >= 10000):
        bin -= 10000

    if bin == 0:
        return []
    elif bin == 1:
        return rev_return(int(binary_str), [handshake[0]])
    elif bin == 10:
        return rev_return(int(binary_str), [handshake[1]])
    elif bin == 11:
        return rev_return(int(binary_str), [handshake[0], handshake[1]])
    elif bin == 100:
        return rev_return(int(binary_str), [handshake[2]])
    elif bin == 1000:
        return rev_return(int(binary_str), [handshake[3]])
    elif bin == 1111:
        return rev_return(int(binary_str), handshake)

def rev_return(bin, result):
    if bin > 10000:
        result.reverse()
        return result
    return result