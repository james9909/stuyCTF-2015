# Borrowed from adventCTF
import sys
import math
import struct

p = lambda x: struct.pack('f', x)
u = lambda x: struct.unpack('b', x)[0]

key = math.radians(141975642814)

enc = open("Blah.enc", 'rb')

lookup = {}
for k in xrange(256):
    for l in xrange(256):
        x = struct.unpack('b', chr(k))[0]
        y = struct.unpack('b', chr(l))[0]

        x1 = p(x * math.cos(key) - y * math.sin(key))
        x2 = p(x * math.sin(key) + y * math.cos(key))

        x3 = struct.unpack('<L', x1)[0]
        x4 = struct.unpack('<L', x2)[0]

        lookup[ (x3<<32)+x4 ] = (k, l)

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

# This problem is very similar to one from adventCTF, so we just borrowed a script created to solve the problem.
# We get a compiled java file, which looks like garbage when printed out, but within it all is the flag.

# stuyctf{such_s3cret_s0_c1a55y}
