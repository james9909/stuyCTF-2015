f = open("bulbasaur.in", "r").readlines()

BAtk = 216
BSPA = 251

SDef = 328
SSPD = 284

STAB = ["Grass", "Poison"]
superEffective = ["Fire"]
halfEffective = ["Normal", "Ice", "Psychic", "Bug", "Ghost", "Dragon", "Dark",
                 "Steel"]
fourthEffective = ["Grass"]
notEffective = ["Poison"]

def damage(_type, physical, base, accuracy):
    if physical:
        d = (210.0 * BAtk * base) / (250.0 * SDef) + 2
    else:
        d = (210.0 * BSPA * base) / (250.0 * SSPD) + 2
    modifier = 1.
    if _type in STAB:
        modifier *= 1.5
    if _type in superEffective:
        modifier *= 4.
    if _type in halfEffective:
        modifier *= 0.5
    if _type in fourthEffective:
        modifier *= 0.25
    if _type in notEffective:
        return 0
    return (accuracy / 100.) * d * modifier

damages = []

for move in f:
    info = move.split(" ")
    damages.append(damage(info[1], info[2] == "physical", int(info[3]), float(info[4])))

print round(sum(sorted(damages)[-4:]))

# stuyctf{139}
