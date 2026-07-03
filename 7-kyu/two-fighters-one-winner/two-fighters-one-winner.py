def declare_winner(fighter1, fighter2, first_attacker):
    # Code your solution here
    attacker = fighter1 if fighter1.name == first_attacker else fighter2
    defender = fighter2 if fighter1.name == first_attacker else fighter1
    
    while attacker.health > 0:
        defender.health -= attacker.damage_per_attack
        if defender.health <= 0:
            return attacker.name
        
        attacker, defender = defender, attacker
    