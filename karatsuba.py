# Python implementation of the Karatsuba Algorithm

from math import log10, ceil
from unittest import result

def karatsuba(x, y):

    # Base Case for Recursion

    if x < 10 or y < 10:
        return x * y 

    # Set n as the highest number of digits in the input number

    n = max(int(log10(x) + 1), int(log10(y) + 1))

    # Round/Ceil on n/2

    median = int(ceil(n/2.0))

    # Add 1 if n is uneven 

    n = n if n % 2 == 0 else n + 1 

    # Split the input numbers

    a, b = divmod(x, 10 ** median)
    c, d = divmod(y, 10 ** median)

    # Apply the three recursive steps

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba((a + b), (c + d)) - ac - bd 

    # Performs the multiplication 

    return(((10 ** n) * ac) + bd + ((10 ** median) * (ad_bc)))

import random 

if __name__ == "__main__":
    for i in range(1000):
        x = random.randint(1, 10 ** 5)
        y = random.randint(1, 10 ** 5)

        expected = x * y 
        result = karatsuba(x, y)

        if result != expected:
            print("Failed!")
        print("Success!")