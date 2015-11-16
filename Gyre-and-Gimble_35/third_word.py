import os

jabberwocky = open("jabberwocky.txt", "r")

words = jabberwocky.read().split() # Split the words

ans = ""
for i in range(len(words)):
    if (i % 3 == 2):
        ans += words[i]
ans = ans.lower()

print "%s" % ans
