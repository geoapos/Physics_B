#!/usr/bin/python3
# Filename: 1_23.py
'''Άσκηση 23:

Σε ποια απόσταση από φορτίο +2μC το δυναμικό έχει τιμή 4·10^4 Volt;
'''
from const import k

# Δεδομένα
Q = 2 * 10 ** (-6)  # φορτίο  Q σε C.
V = 4 * 10 ** 4  # Δυναμικό σε V.

print('-----------------------------------')
print('Το δυναμικό σε απόσταση r, δίνεται από τη σχέση: V =U/q => V= k*Q/r ')
print('Άρα: r=k*Q/V')
r = k * Q / V
print('r = {:.3f} m'.format(r))
