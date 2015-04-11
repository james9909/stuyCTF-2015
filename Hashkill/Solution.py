import md5

encrypted_flag = "76370c8b218eacfdf6a33bd4c311575a"
boroughs = ["Queens", "Manhatten", "Staten Island", "Bronx", "Brooklyn"]

for firstNums in range(0,1000):
    for borough in boroughs:
        for lastNums in range(10000, 15000):
            flag = "stuyctf{%s_%s_%s}" % (firstNums, borough, lastNums)
            print flag
            testHash = md5.new(flag)
            if (testHash.digest() == encrypted_flag):
                print flag
                sys.exit(0)
