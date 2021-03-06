#!/usr/bin/python3
# Filename: 1_22.py
'''Άσκηση 22:

Να βρεθεί το δυναμικό σε απόσταση 0,9m από φορτίο +6μC.
'''
from const import k

# Δεδομένα
Q1 = 6 * 10 ** (-6)  # φορτίο-πηγή  Q1 σε C.
r = 0.9  # Απόσταση σε m.

print('-----------------------------------')
print('Το συναμικό σε απόσταση r, δίνεται από τη σχέση: V =U/q => V= k*Q1/r ')
print('Άρα:')
V = k * Q1 / r
print('V = {:.3e} V'.format(V))
