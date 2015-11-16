enc = [115, 116, 117, 121, 99, 116, 102, 123, 114, 97, 98, 99, 107, 108, 101, 102, 116, 95, 105, 36, 95, 112, 114, 51, 116, 116, 121, 95, 107, 108, 101, 102, 119, 108, 125]
print "".join([chr(char) for char in enc])

# Oh no, we have to look at some scheme code...
# The flag isn't even encrypted, so we can just print out the characters represented by the ascii values.
# Alternatively, changing #f to #t in the decryption algorithm will make it work.

# stuyctf{rabckleft_i$_pr3tty_klefwl}
