# Basically the same as the encryption method so basically copy pasted

import sys
import math
import struct

p = lambda x: struct.pack('b', x)
u = lambda x: struct.unpack('f', x)[0]

if len(sys.argv) != 5:
	sys.exit(1)

filename = sys.argv[1]
r = float(sys.argv[2])
keyx = int(sys.argv[3])
keyy = int(sys.argv[4])

enc = open(filename, 'rb').read()
decrypted = open(filename + str(r) + ".jpg", 'wb')

# 8 because 8 bytes for each x and y
for i in range(0,len(enc),8):
        # Acquire the encrypted x and y values to decrypt
	(x, y) = u(enc[i:i+4]), u(enc[i+4:i+8])
        try:
            # wolfram alpha inversion formula
            decrypted.write(p(round(((r ** 2) * (x - keyx)) / ((x - keyx)** 2 + (y - keyy) ** 2))) \
                    + p(round(((r ** 2) * (y - keyy)) / ((x - keyx)** 2 + (y - keyy) ** 2))))
        except ZeroDivisionError:
            decrypted.write(p(round(x)) + p(round(y)))
        finally:
            pass
