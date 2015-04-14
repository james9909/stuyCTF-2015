import socket, random

# Connect to that server
SERVER = "stuyctf.me"
PORT = 50000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((SERVER, PORT))

print sock.recv(1024)
sock.sendall("RockBeatsScissorsBeatsPaper\n")
print sock.recv(1024)

# Acquired from ai.py with minor adjustments:
ROCK = 100
PAPER = 101
SCISSORS = 102
toss_choices = {'r': ROCK, 'p': PAPER, 's': SCISSORS}
toss_choices_swapped = {n:t for (t, n,) in toss_choices.items()}
history = []
rng = random.SystemRandom()

def choose_best(scores):
    if scores[ROCK] == 0 and scores[PAPER] == 0 and scores[SCISSORS] == 0:
        return False
    choices = []
    max_score = max(scores.values())
    for choice in scores.keys():
        if scores[choice] == max_score:
            choices.append(choice)

    player_next_toss = rng.choice(choices)
    if player_next_toss == ROCK:
        return PAPER
    if player_next_toss == PAPER:
        return SCISSORS
    if player_next_toss == SCISSORS:
        return ROCK

def smart_choose_user_next_input():
    scores = {ROCK: 0, PAPER: 0, SCISSORS: 0}
    history_length = len(history)
    length = 4
    i = len(history) - length
    while i >= length - 1:
        if history[i] == history[(history_length - 1)]:
            if history[(i - 1)] == history[(history_length - 2)]:
                if history[(i - 2)] == history[(history_length - 3)]:
                    if history[(i - 3)] == history[(history_length - 4)]:
                        scores[history[i + 1]] += 1
        i -= 1

    best = choose_best(scores)
    if best:
        return best
    scores = {ROCK: 0, PAPER: 0, SCISSORS: 0}
    length = 3
    i = len(history) - length
    while i >= length - 1:
        if history[i] == history[(history_length - 1)]:
            if history[(i - 1)] == history[(history_length - 2)]:
                if history[(i - 2)] == history[(history_length - 3)]:
                    scores[history[i + 1]] += 1
        i -= 1

    best = choose_best(scores)
    if best:
        return best
    scores = {ROCK: 0, PAPER: 0, SCISSORS: 0}
    length = 2
    i = len(history) - length
    while i >= length - 1:
        if history[i] == history[(history_length - 1)]:
            if history[(i - 1)] == history[(history_length - 2)]:
                scores[history[i + 1]] += 1
        i -= 1

    best = choose_best(scores)
    if best:
        return best
    return toss_choices.values()[0]

# Beginning round is random to give some data
for i in range(0, 15):
    move = random.choice(toss_choices.keys())
    history.append(toss_choices[move])
    sock.sendall(move + "\n")
    print sock.recv(1024)

output = sock.recv(1024)
# Until we get the flag, run
while (output.find("stuyctf") == -1):
    compMove = smart_choose_user_next_input()
    if (compMove == ROCK):
        move = 'p'
    elif (compMove == PAPER):
        move = 's'
    elif (compMove == SCISSORS):
        move = 'r'

    history.append(toss_choices[move])
    sock.sendall(move + "\n")

    print sock.recv(1024)
    output = sock.recv(1024)
    print output
