f = open("reversed.jpg" ,"wb").write(open("tt.jpg", "rb").read()[::-1])

# Looking at the hex reveals reversed jpg headers, so to undo this, we need to
# reverse all the bytes of the jpg. Open reversed.jpg to view the flag (which is upside down)

# stuyctf{topsy_turvy}
