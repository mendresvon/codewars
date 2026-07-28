def replace_exclamation(st):
    return ''.join(['!' if c in 'aeiouAEIOU' else c for c in st])