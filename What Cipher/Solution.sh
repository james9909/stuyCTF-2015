#!/bin/bash

for i in {a..z}; do for j in {a..z}; do $(openssl enc -d -des3 -in test.enc -pass pass:$i$j -out plaintext.txt);done;done
