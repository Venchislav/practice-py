import math


def declare_winner(fighter1, fighter2, first_attacker):
    fighter1roundsalive = math.ceil(fighter1.health / fighter2.damage_per_attack)
    fighter2roundsalive = math.ceil(fighter2.health / fighter1.damage_per_attack)
    if fighter1roundsalive == fighter2roundsalive:
        return first_attacker
    else:
        return fighter1.name if fighter1roundsalive > fighter2roundsalive else fighter2.name


# but it looks better

def declare_winner(fighter1, fighter2, first_attacker):
    cur, opp = (fighter1, fighter2) if first_attacker == fighter1.name else (fighter2, fighter1)
    while cur.health > 0:
        opp.health -= cur.damage_per_attack
        cur, opp = opp, cur
    return opp.name
