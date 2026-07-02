def DNA_strand(dna):
    dna = list(dna)
    
    for i in range(len(dna)):
        if dna[i] == 'A':
            dna[i] = 'T'
        elif dna[i] == 'T':
            dna[i] = 'A'
        elif dna[i] == 'C':
            dna[i] = 'G'
        elif dna[i] == 'G':
            dna[i] = 'C'
    
    return ''.join(dna)