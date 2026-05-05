def count_smileys(arr):
    smiley_count = 0
    
    for face in arr:
        if len(face) == 2 and face[0] in [':', ';'] and face[1] in [')', 'D']:
            smiley_count += 1
        elif len(face) == 3 and face[0] in [':', ';'] and face[1] in ['-', '~'] and face[2] in [')', 'D']:
            smiley_count += 1
    
    return smiley_count