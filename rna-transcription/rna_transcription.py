def to_rna(dna_strand):
    rna = ''
    transcription = {'G': 'C',
                    'C': 'G',
                    'T': 'A',
                    'A': 'U'}
    for letter in dna_strand:
        rna += transcription[letter]
    return rna
        
