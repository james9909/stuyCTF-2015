import binascii

# Open and read the file
orig = open("not-morse-code.txt", "r")
enc = orig.read()

# Loop 5 times because thats how many times it takes to fully decrypt
for i in range(0, 5):
    # We want to alternate the replacements so we do this
    if (i % 2 == 0):
        enc = enc.replace(".", "0").replace("-", "1")
    else:
        enc = enc.replace(".", "1").replace("-", "0")
    num = int(enc, 2)
    hexed = hex(num)[2:-1]
    enc = hexed.decode('hex')

print enc

# stuyctf{morse_code_is_not_binary}
