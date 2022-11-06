def encode(numbers):
    encoded_values = []
    for num in numbers:
        bin_n = f'{num:b}'
        
        # complement with zeros
        while len(bin_n) % 7 != 0: bin_n = '0' + bin_n
        
        # form 8-bit octets
        end = len(bin_n) // 7
        octets = [str(1*(i != end-1)) + bin_n[i*7:i*7+7] for i in range(end)]
        
        encoded_values.extend([int(oct, 2) for oct in octets])
    return encoded_values

def decode(bytes_):
    # check input data
    if bin(bytes_[-1])[2:][-8:-7] == '1':
        raise ValueError("incomplete sequence")

    sequences, seq_ind = [[]], 0
    for byte_ind, byte in enumerate(bytes_):
        bin_n = bin(byte)[2:]
        # complement with zeros to full octet
        while len(bin_n) % 8 != 0:
            bin_n = '0' + bin_n

        # check if MSB is 0 (end of sequence) + add to the sequences list
        sequences[seq_ind].append(bin_n[1:])
        if bin_n[-8:-7] == '0' and byte_ind != len(bytes_) - 1:
            seq_ind += 1
            sequences.append([])

    decoded = [int(''.join(seq), 2) for seq in sequences]
    return decoded
