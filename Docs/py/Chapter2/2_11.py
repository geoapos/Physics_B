#!/usr/bin/python3
# filename 2_11.py
"""
Άσκηση 2.11

Δύο αντιστάσεις συνδέονται παράλληλα και στις άκρες του συστήματος εφαρμόζε-
ται τάση V = 120V. Αν είναι R1 = 30Ω και R2 =60Ω,
να βρείτε την ολική αντίσταση του συστήματος και την ένταση του ρεύματος, που
διαρρέει το κύκλωμα και κάθε αντίσταση.
"""

# Δεδομένα
R1 = 30  # Αντίσταση σε Ω
R2 = 60  # Αντίσταση σε Ω
V = 120  # Τάση σε V

print()
Rol = (R1 * R2) / (R1 + R2)
print('Ισχύει Ιol=I1+I2 => V/Rol = V/R1 + V/R2 => 1/Rol = 1/R1 + 1/R2 => Rol={:.2f} Ω'.format(Rol))
Ι1 = V / R1
print('Ισχύει Ι1=V/R1 => I1={:.2f} A'.format(Ι1))
Ι2 = V / R2
print('Ισχύει Ι2=V/R2 => I2={:.2f} A'.format(Ι2))
print('Ιol=I1+I2 => Iol={:.2f} A'.format(Ι1 + Ι2))
