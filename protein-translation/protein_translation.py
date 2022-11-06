def proteins(strand):
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]

    dict = {'AUG': 'Methionine', 'UUU UUC': 'Phenylalanine',
            'UUA UUG': 'Leucine', 'UCU UCC UCA UCG': 'Serine',
            'UAU UAC': 'Tyrosine', 'UGU UGC': 'Cysteine', 'UGG': 'Tryptophan'}

    proteins = []
    for codon in codons:
        if codon in 'UAA, UAG, UGA':
            return proteins
        for codon_gr in list(dict.keys()):
            if codon in codon_gr:
                proteins.append(dict[codon_gr])
    return proteins
