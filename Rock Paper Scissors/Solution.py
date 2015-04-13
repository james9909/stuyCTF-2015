import socket, random

SERVER = "stuyctf.me"
PORT = 50000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((SERVER, PORT))

print sock.recv(1024)
sock.sendall("RockBeatsScissorsBeatsPaper\n")
print sock.recv(1024)

moves = {"r": 0, "p": 1, "s": 2}

def throwPrediction(history):
    lastMove = history[-1]
    cloned = history
    history = history[:-1]

    numRock = 0
    numPaper = 0
    numScissors = 0

    sameMovesAsLast = [i for i, x in enumerate(history) if x == str(lastMove)]
    while (len(sameMovesAsLast) > 0):
        # No more index out of bounds!
        if (cloned[-1] == cloned[-2]):
            moveAfterLast = cloned[-1]
            history[-1] = 'a'
            if (moveAfterLast == 'r'):
                numRock += 1
            elif (moveAfterLast == 'p'):
                numPaper += 1
            else:
                numScissors += 1
            sameMovesAsLast = sameMovesAsLast[1:]

        else:
            moveAfterLast = history[sameMovesAsLast[0]+1]
            if (moveAfterLast == 'r'):
                numRock += 1
            elif (moveAfterLast == 'p'):
                numPaper += 1
            else:
                numScissors += 1
            sameMovesAsLast = sameMovesAsLast[1:]

    mostLikely = max(numRock, numPaper, numScissors)
    if (numRock == numPaper and numPaper == numScissors):
        return 'r'
    elif (numRock == numPaper):
        return 'tierp'
    elif (numRock == numScissors):
        return 'tiers'
    elif (numPaper == numScissors):
        return 'tieps'
    else:
        if (mostLikely == numRock):
            return 'p'
        elif (mostLikely == numPaper):
            return 's'
        else:
            return 'r'

history = []
output = ""

for i in range(0, 10):
    move = random.choice(moves.keys())
    sock.sendall(move + "\n")
    history.append(move)
    print sock.recv(1024)

while (output.find("stuyctf") == -1):
    compMove = throwPrediction(history)
    if (compMove == 'tierp'):
        move = 'p'
    elif (compMove == 'tiers'):
        move = 'r'
    elif (compMove == 'tieps'):
        move = 's'
    elif (compMove == 'r'):
        move = 'r'
    elif (compMove == 'p'):
        move = 'p'
    else:
        move = 's'

    sock.sendall(move + "\n")
    history.append(move)

    print sock.recv(1024)
    output = sock.recv(1024)
    print output
