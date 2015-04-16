import os

noPunc = open("jabberwocky.txt", "r")

words = noPunc.read().split() # Split the words

noPunc.close()
ans = ""
for i in range(len(words)):
    if (i % 3 == 2):
        ans += words[i]
ans = ans.lower()

print "%s" % ans
