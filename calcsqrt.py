#! /usr/bin/env python3

# Simon O'Sullivan
# Calulate the square root of a number

def sqrt(x):
    """
    Calulate the square root of argument x
    """
    # Intitial guess for the square root 
    z = x / 2.0

    #Continuously improve guess
    while abs(x - (z*z)) > 0.0000001:
        z = z - ((z*z -x) / (2*z))

    return z

print(sqrt(63.0))

