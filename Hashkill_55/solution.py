import hashlib, sys

enc = "76370c8b218eacfdf6a33bd4c311575a"
boroughs = ["queens", "manhattan", "staten island", "bronx", "brooklyn"]

for firstNums in range(0,1000):
    for borough in boroughs:
        for lastNums in range(10000, 15000):
            candidate = "stuyctf{%s_%s_%s}" % (firstNums, borough, lastNums)
            if (hashlib.md5(candidate).hexdigest() == enc):
                print candidate
                sys.exit(0)

# stuyctf{345_manhattan_10282}
