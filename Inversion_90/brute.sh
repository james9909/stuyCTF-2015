#!/bin/bash

for i in $(seq 10 99); do
    python decrypt.py image.jpg.enc $i 0 0
done
