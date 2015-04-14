#!/bin/bash

for i in $(seq 10 99); do
    for j in $(seq 0 360); do
        for k in $(seq 0 360); do
            python Solution.py image.jpg.enc $i $j $k
        done
    done
done
