import sys
import math
import struct

p = lambda x: struct.pack('f', x)
u = lambda x: struct.unpack('b', x)[0]

if len(sys.argv) != 5:
    sys.exit(1)

filename = sys.argv[1]
r = float(sys.argv[2])
keyx = int(sys.argv[3])
keyy = int(sys.argv[4])

enc = open(filename, 'rb')

lookup = {}
for k in xrange(256):
    for l in xrange(256):
        x = struct.unpack('b', chr(k))[0]
        y = struct.unpack('b', chr(l))[0]

        try:
            x1 = p(((r ** 2) * (x - keyx)) / ((x - keyx)** 2 + (y - keyy) ** 2))
            x2 = p(((r ** 2) * (y - keyy)) / ((x - keyx)** 2 + (y - keyy) ** 2))
            x3 = struct.unpack('<L', x1)[0]
            x4 = struct.unpack('<L', x2)[0]

            lookup[ (x3<<32)+x4 ] = (k, l)

        except ZeroDivisionError:
            print p(float(x)) + p(float(y))


going = 1
decoded = ""
while going:
    try:
        f1 = struct.unpack('<L', enc.read(4))[0]
        f2 = struct.unpack('<L', enc.read(4))[0]
        (x, y) = lookup[ (f1<<32)+f2 ]
        decoded += chr(x)
        decoded += chr(y)
    except:
        going = 0
        print decoded
