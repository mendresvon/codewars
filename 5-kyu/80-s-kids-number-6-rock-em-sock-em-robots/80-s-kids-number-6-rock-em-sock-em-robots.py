def fight(r1, r2, tactics):
    r1["tactics"].reverse()
    r2["tactics"].reverse()
    attacker, defender = (r1, r2) if r1["speed"] >= r2["speed"] else (r2, r1)
    
    while attacker["health"] > 0:
        if not attacker["tactics"] and not defender["tactics"]:
            break
        if attacker["tactics"]:
            defender["health"] -= tactics[attacker["tactics"].pop()]
        attacker, defender = defender, attacker
    
    if attacker["health"] == defender["health"]:
        return "The fight was a draw."
    elif attacker["health"] > defender["health"]:
        return f"{attacker['name']} has won the fight."
    else:
        return f"{defender['name']} has won the fight."