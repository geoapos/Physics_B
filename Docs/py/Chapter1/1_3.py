#!/usr/bin/python3
# Filename:1_3.py

'''
Άσκηση 3:
Δύο μικρές φορτισμένες σφαίρες έχουν ίσα ηλεκτρικά φορτία
-0,02μC. Αν η δύναμη που ασκείται από τη μια σφαίρα στην άλλη
έχει μέτρο 9 · 10 -3 Ν, να υπολογιστεί η απόσταση μεταξύ των σφαι-
ρών.
'''
from math import sqrt
from const import k

# Δεδομένα

q = -0.02 * 10 ** (-6)  # φορτια
F = 9 * 10 ** (-3)  # Δύναμη

print("Από τον νόμο του Coulomb: ")
print('r=√(k*q*q/F')
print()
r = sqrt(k * q * q / F)

print('r={:.3f} m'.format(r))
