#!/usr/bin/python3
# filename 2_38.py
"""
Άσκηση 2.38

Στο παραπάνω κύκλωμα να βρείτε το φορτίο
του πυκνωτή.
"""

# Δεδομένα
R1 = 6  # Αντίσταση σε Ω
R2 = 3  # Αντίσταση σε Ω
r = 1  # Αντίσταση σε Ω
E = 20  # Τάση σε V
C = 4 * 10 ** (-6)  # Χωρητικότητα σε F

print()

print('Επειδή η χωρητικότητα του πυκνωτή δίνεται από την σχέση Q=C*V  (1)')
print('θα πρέπει να υπολογίσουμε την τάση V στα άκρα του.')
print()
print('Για την ηλεκτρεγερτική δύναμη εφαρμόζουμε τον νόμο του Ohm:')
print('E=I*R1+I*R2+I*r => I= E / (R1+R2+r) =>')
I = E / (R1 + R2 + r)
print('I={:.2f} A'.format(I))

V = I * R2
print('άρα η τάση V στα άκρα του πυκνωτή είναι V=I*R2 =>V={:.2f} V'.format(V))
print()
Q = C * V
print('Από την (1) => Q={:.2e} C'.format(Q))
