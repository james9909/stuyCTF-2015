from moves import *

bulbasaur = {"TYPE": "Grass Poison", "ATTACK": 216.0, "SPATTACK": 251.0}

scizor = {"TYPE": "Bug Steel", "DEFENSE": 328.0, "SPDEFENSE": 284.0}

# Don't take into account fire type moves, which are super super effective, because
# bulbasaur can't use fire type moves
def typeEffectiveness(moveType):
    notRly = "NormalBugGhostSteelPsychicIceDragonDark"
    doubleNotRly = "Grass"
    if (notRly.find(moveType) != -1): # Not really effective...
        return .5
    elif (doubleNotRly.find(moveType) != -1): # Really really not effective...
        return .25
    elif (moveType == "Poison"):
        return 0
    else: # Normal
        return 1

def damageFormula(level, isSpecial, myAttack, enemyDefense, base, myType, enemyType, moveType, accuracy):
    if (isSpecial):
        myAttack = bulbasaur["SPATTACK"]
        enemyDefense = scizor["SPDEFENSE"]
        damage = (((2 * level + 10)/250.0) * (myAttack/enemyDefense) * base + 2)
        damage *= modifier(myType, enemyType, moveType)
        damage *= accuracy
    else:
        damage = (((2 * level + 10)/250.0) * (myAttack/enemyDefense) * base + 2)
        damage *= modifier(myType, enemyType, moveType)
        damage *= accuracy
    return damage

def modifier(myType, enemyType, moveType):
    if (myType.find(moveType) != -1): # STAB
        amount = 1.5
    else:
        amount = 1
    amount *= typeEffectiveness(moveType)
    print "modifier is %s" % amount
    return amount

maxDamage = [0, 0, 0, 0]
isSpecial = False
moveWithMostDamage = ["", "", "", ""]
for move in range(0, len(moves)):
    if (moves[move][2] == "Special"): # Special attacks
        isSpecial = True
    else:
        isSpecial = False
    currDamage = damageFormula(100, isSpecial, bulbasaur["ATTACK"], scizor["DEFENSE"], moves[move][3], bulbasaur["TYPE"], scizor["TYPE"], moves[move][1], moves[move][4])
    print currDamage
    # Update max damage
    if (currDamage >= maxDamage[0]):
        maxDamage[0] = currDamage
        moveWithMostDamage[0] = moves[move]
    elif (currDamage >= maxDamage[1]):
        maxDamage[1] = currDamage
        moveWithMostDamage[1] = moves[move]
    elif (currDamage >= maxDamage[2]):
        maxDamage[2] = currDamage
        moveWithMostDamage[2] = moves[move]
    elif (currDamage >= maxDamage[3]):
        maxDamage[3] = currDamage
        moveWithMostDamage[3] = moves[move]
    print moves[move]

print str(maxDamage) + " " + str(moveWithMostDamage)
print maxDamage[0] + maxDamage[1] + maxDamage[2] + maxDamage[3]
