def DNA_strand(dna):
    pairs = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    
    return ''.join(pairs[char] for char in dna)