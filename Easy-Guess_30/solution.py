#!/usr/bin/python2.7
import random #woohoo the random module is lots of fun
import math
random.seed(999999999999999999999999999999999999) #heheheh super high number so hax0rs will never get it
key=0
i=math.floor(random.random()*100)
while i > 0:
    random.random() #to mix it up a little
    i-=1
key=math.floor(random.random()*1000000)

print(key)

# If you know anything about how random works, you know that it generates pseudo-randomly.
# This means that even if the seed is super large, it will generate the same sequence of numbers
# each time. Knowing this, all we need to do is print out the key, which will be the same each time
# The key is 310295.0

# darnit.  here's the flag: stuyctf{Nevar_use_k0nstant_seeds}
