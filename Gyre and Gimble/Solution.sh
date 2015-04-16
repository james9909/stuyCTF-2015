#!/bin/bash

echo "stuyctf{"$(python thirdWord.py | sed 's/\([[:punct:]]\)//g')"}"
