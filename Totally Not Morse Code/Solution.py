import binascii

# TODO: Clean up and while loop

# Original morse code
orig = open("not-morse-code.txt", "r")
origStream = orig.read()
# Take into account both possibilities
origBinary = origStream.replace(".", "1").replace("-", "0")
origBinaryAlt = origStream.replace(".", "0").replace("-", "1")

# Convert into decimal
num = int(origBinary, 2)
numAlt = int(origBinaryAlt, 2)

# Hex it
hexed = hex(num)
hexedAlt = hex(numAlt)

# Exclude non-hex characters
hexed = hexed[2:-1]
hexedAlt = hexedAlt[2:-1]

# Hex to ascii
# %x formats it into hex

# secondOrig = binascii.unhexlify(hexed)
secondOrigAlt =  binascii.unhexlify(hexedAlt) # Correct one

# 2-----------------------------------------------------------------------------
# Repeat until we get something meaningful

secondOrigBin = secondOrigAlt.replace(".", "1").replace("-", "0")
secondOrigBinAlt = secondOrigAlt.replace(".", "0").replace("-", "1")

secondNum = int(secondOrigBin, 2)
secondNumAlt = int(secondOrigBinAlt, 2)

secondHex = hex(secondNum)
secondHexAlt = hex(secondNumAlt)

secondHex = secondHex[2:-1]
secondHexAlt = secondHexAlt[2:-1]

thirdOrig = binascii.unhexlify(secondHex) # Correct one
# thirdOrigAlt = binascii.unhexlify(secondHexAlt)

# 3-----------------------------------------------------------------------------
# Repeat until we get something meaningful

thirdOrigBin = thirdOrig.replace(".", "1").replace("-", "0")
thirdOrigBinAlt = thirdOrig.replace(".", "0").replace("-", "1")

thirdNum = int(thirdOrigBin, 2)
thirdNumAlt = int(thirdOrigBinAlt, 2)

thirdHex = hex(thirdNum)
thirdHexAlt = hex(thirdNumAlt)

thirdHex = thirdHex[2:-1]
thirdHexAlt = thirdHexAlt[2:-1]

# fourthOrig = binascii.unhexlify(thirdHex)
fourthOrigAlt = binascii.unhexlify(thirdHexAlt) # Correct one

# 4-----------------------------------------------------------------------------
# Repeat until we get something meaningful

fourthOrigBin = fourthOrigAlt.replace(".", "1").replace("-", "0")
fourthOrigBinAlt = fourthOrigAlt.replace(".", "0").replace("-", "1")

fourthNum = int(fourthOrigBin, 2)
fourthNumAlt = int(fourthOrigBinAlt, 2)

fourthHex = hex(fourthNum)
fourthHexAlt = hex(fourthNumAlt)

fourthHex = fourthHex[2:-1]
fourthHexAlt = fourthHexAlt[2:-1]

fifthOrig = binascii.unhexlify(fourthHex) # Correct one
# fifthOrigAlt = binascii.unhexlify(fourthHexAlt)

# 5-----------------------------------------------------------------------------
# Repeat until we get something meaningful


sixthOrigBin = fifthOrig.replace(".", "1").replace("-", "0")
sixthOrigBinAlt = fifthOrig.replace(".", "0").replace("-", "1")

sixthNum = int(sixthOrigBin, 2)
sixthNumAlt = int(sixthOrigBinAlt, 2)

sixthHex = hex(sixthNum)
sixthHexAlt = hex(sixthNumAlt)

sixthHex = sixthHex[2:-1]
sixthHexAlt = sixthHexAlt[2:-1]

# seventhOrig = binascii.unhexlify(sixthHex)
seventhOrigAlt = binascii.unhexlify(sixthHexAlt) # Correct one

print seventhOrigAlt # odam it be flag
