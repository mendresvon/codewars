def declare_winner(fighter1, fighter2, first_attacker):
    # Code your solution here
    attacker = fighter1 if first_attacker == fighter1.name else fighter2
    defender = fighter2 if first_attacker == fighter1.name else fighter1
    
    while attacker.health > 0:
        defender.health -= attacker.damage_per_attack
        if defender.health <= 0:
            return attacker.name
        defender, attacker = attacker, defender
    