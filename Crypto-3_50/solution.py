f = open("rsa.txt", "r").readlines()

c = int(f[0].split(" ")[1].strip(), 16)
n = int(f[1].split(" ")[1].strip(), 16)
e = int(f[2].split(" ")[1].strip(), 16)
d = int(f[3].split(" ")[1].strip(), 16)

m = pow(c, d, n)
print hex(m)[2:-1].decode("hex")

# The numbers and the name of the file makes it clear that we need to decrypt some rsa.
# You can find some information about rsa over at https://en.wikipedia.org/wiki/RSA_(cryptosystem)
# In short, we need to do (c^d) % n to decrypt the message.

# stuyctf{rsa_large_primes_4_security}
