import hashlib, sys

encrypted_flag = "76370c8b218eacfdf6a33bd4c311575a"
boroughs = ["queens", "manhattan", "staten island", "bronx", "brooklyn"]

for firstNums in range(0,1000):
    for borough in boroughs:
        for lastNums in range(10000, 15000):
            testing = "stuyctf{%s_%s_%s}" % (firstNums, borough, lastNums)
            print testing
            testHash = hashlib.md5(testing)
            if (testHash.hexdigest() == encrypted_flag):
                print "The flag is " + testing
                sys.exit(0)
