def fight(r1, r2, tactics):
    r1['tactics'].reverse()
    r2['tactics'].reverse()
    att, deff = (r1,r2) if r1['speed'] >= r2['speed'] else [r2, r1]
    
    while att['health'] > 0:
        if not (att['tactics'] or deff['tactics']):
            break
        if att['tactics']:
            deff['health'] -= tactics[att['tactics'].pop()]
        att, deff = deff, att
    
    if att['health'] > deff['health']:
        return f"{att['name']} has won the fight."
    elif deff['health'] > att['health']:
        return f"{deff['name']} has won the fight."
    else:
        return "The fight was a draw."