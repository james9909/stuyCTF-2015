#!/bin/bash

echo "stuyctf{"$(python third_word.py | sed 's/\([[:punct:]]\)//g')"}"
