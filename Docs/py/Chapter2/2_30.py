#!/usr/bin/python3
# filename 2_30.py
"""
Άσκηση 2.30

Τέσσερις αντιστάτες με αντιστάσεις R1 = 2Ω,
R2 = 4Ω, R3 = 6Ω, R4 = 8Ω συνδέονται έτσι
ώστε,  η ολική αντίσταση να είναι Rολ = 11Ω.
Αν τροφοδοτήσουμε τη διάταξη με πηγή, η
ισχύς του αντιστάτη R3 είναι Ρ3 = 24W. Να
βρείτε την ισχύ του αντιστάτη R4.
"""

from math import sqrt

# Δεδομένα
R1 = 2  # Αντίσταση σε Ω
R2 = 4  # Αντίσταση σε Ω
R3 = 6  # Αντίσταση σε Ω
R4 = 8  # Αντίσταση σε Ω
Rol = 11  # Αντίσταση σε Ω
P3 = 24  # Ισχύς σε W

print()
R12 = R1 + R2
print('Οι αντιστάσεις R1 και R2 συνδέονται σε σειρά άρα R12=R1+R2 =>')
print('R1={:.2f} Ω'.format(R12))
print('Οι αντιστάσεις R12 και R3 συνδέονται παράλληλα, άρα:')
R123 = R12 * R3 / (R12 + R3)
print('R123=R12*R3/(R12+R3) => R123={:.2f} Ω'.format(R123))
print('Τέλος οι αντιστάσεις R123 και R4 συνδέονται σε σειρά,')
Rολ = R123 + R4
print('Rολ=R123+R4 => Rολ={:.2f} Ω'.format(Rολ))
print()
print('Η ισχύς στην αντίσταση R3 είναι P3=I3²*R3 => I3=√(P3/R3) =>')
I3 = sqrt(P3 / R3)
print('I3={:.2f} A'.format(I3))
print()
print('Ισχύει V=I3*R3+Iολ*R4 => V=I3*R3+(V/Rολ)*R4 =>')
V = (I3 * R3) / (1 - R4 / Rol)
print('V=(I3*R3)/(1-R4/Rol)=> V={:.2f} V'.format(V))
Iολ = V / Rol
print('Επειδή V=Iολ*Rολ=> Iολ=V/Rol=>Iολ={:.2f} Α'.format(Iολ))
P4 = (Iολ ** 2) * R4
print('Επειδή επίσης P4=Iολ²*R4 => P4={:.2f} W'.format(P4))
