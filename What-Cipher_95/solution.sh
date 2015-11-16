#!/bin/bash

# Let's brute force these encryption methods
encMethods="
aes-128-cbc
aes-128-cbc-hmac-sha1
aes-128-cfb
aes-128-cfb1
aes-128-cfb8
aes-128-ctr
aes-128-ecb
aes-128-gcm
aes-128-ofb
aes-128-xts
aes-192-cbc
aes-192-cfb
aes-192-cfb1
aes-192-cfb8
aes-192-ctr
aes-192-ecb
aes-192-gcm
aes-192-ofb
aes-256-cbc
aes-256-cbc-hmac-sha1
aes-256-cfb
aes-256-cfb1
aes-256-cfb8
aes-256-ctr
aes-256-ecb
aes-256-gcm
aes-256-ofb
aes-256-xts
aes128
aes192
aes256
bf
bf-cbc
bf-cfb
bf-ecb
bf-ofb
camellia-128-cbc
camellia-128-cfb
camellia-128-cfb1
camellia-128-cfb8
camellia-128-ecb
camellia-128-ofb
camellia-192-cbc
camellia-192-cfb
camellia-192-cfb1
camellia-192-cfb8
camellia-192-ecb
camellia-192-ofb
camellia-256-cbc
camellia-256-cfb
camellia-256-cfb1
camellia-256-cfb8
camellia-256-ecb
camellia-256-ofb
camellia128
camellia192
camellia256
cast
cast-cbc
cast5-cbc
cast5-cfb
cast5-ecb
cast5-ofb
des
des-cbc
des-cfb
des-cfb1
des-cfb8
des-ecb
des-ede
des-ede-cbc
des-ede-cfb
des-ede-ofb
des-ede3
des-ede3-cbc
des-ede3-cfb
des-ede3-cfb1
des-ede3-cfb8
des-ede3-ofb
des-ofb
des3
desx
desx-cbc
"

function isFlag {
    if echo $CRACKED | grep "stuyctf" > /dev/null ; then
        echo "The password is $pass"
        echo "The encryption method is $enc"
        echo "Decrypted: $CRACKED"
        exit 0
    fi
}

function crack {
    for i in {a..z}; do
        for j in {a..z}; do
            for enc in $encMethods; do
                pass=$i$j
                CRACKED=$(openssl enc -d -$enc -pass pass:$pass -in ciphertext.txt 2> /dev/null)
                echo $pass
                isFlag $CRACKED
            done
        done
    done
}

crack
