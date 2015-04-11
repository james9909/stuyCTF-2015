import socket, random

SERVER = "stuyctf.me"
PORT = 50000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((SERVER, PORT))

print sock.recv(1024)
sock.sendall("RockBeatsScissorsBeatsPaper\n")
print sock.recv(1024)

moves = {"r": 1, "p": 2, "s": 3}

output = ""
while (output.find("stuy") == -1):
    move = random.choice(moves.keys())
    sock.sendall(move + "\n")
    print sock.recv(1024)
    output = sock.recv(1024)
    print output
