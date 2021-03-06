#!/usr/bin/python3
# filename 2_22.py
"""
Άσκηση 2.22

Στο παρακάτω κύκλωμα, αν C = 20μF,
V = 100V και R1 = 40Ω, R3 = 10Ω, να βρείτε το
φορτίο του πυκνωτή.
"""

# Δεδομένα
R1 = 40  # Αντίσταση σε Ω
R3 = 10  # Αντίσταση σε Ω
C = 20 * 10 ** (-6)  # Χωρητικοτητα σε F
V = 100  # Τάση σε V

print()
print('Ο κλάδος ΒΔΓ δε διαρρέεται από ρεύμα.')
I = V / (R1 + R3)
print('Έτσι, I=V / (R1+R3) => I={:.2f} A'.format(I))
print('Η τάση στα άρα του πυκνωτή είναι Vc= I*R3 =>')
Vc = I * R3
print('Vc={:.2f} V'.format(Vc))
print('Ισχύει όμως ότι C=q/Vc =>')
q = C * Vc
print('q=C*Vc => q={:.0e} C'.format(q))
