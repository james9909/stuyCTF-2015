import binascii

# Open and read the file
orig = open("not-morse-code.txt", "r")
origStream = orig.read()

# Loop 5 times because thats how many times it takes to fully decrypt
for i in range(0, 5):
    # We want to alternate the replacements so we do this
    if (i % 2 == 0):
        origStream = origStream.replace(".", "0").replace("-", "1")
    else:
        origStream = origStream.replace(".", "1").replace("-", "0")
    num = int(origStream, 2) # Binary to decimal
    hexed = hex(num) # Decimal to hex
    hexed = hexed[2:-1] # Slice off the parts that aren't hex

    origStream = binascii.unhexlify(hexed) # Hex to ascii

print origStream
