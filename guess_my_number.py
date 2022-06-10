#!/usr/bin/env python3
import numpy as np

rng = np.random.default_rng()

my_num = str(rng.integers(10) + 1)

print("I'm thinking of a number in the range of [1, 10]...")
num = input("What is my number? ").strip()
while num != my_num:
    print("WRONG")
    num = input("What is my number? ").strip()
    
print("Amazing.")