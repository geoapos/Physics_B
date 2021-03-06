#!/usr/bin/python3
# filename 2_15.py
"""
Άσκηση 2.15

Στο παρακάτω κύκλωμα η αντίσταση ανά μονάδα μήκους του σύρματος του τριγώνου
είναι R* = 5Ω/cm. Να βρείτε την ένταση του ρεύματος, που διαρρέει κάθε πλευρά
του τριγώνου.
"""
from math import sqrt

# Δεδομένα
r = 5 * 10 ** 2  # Αντίσταση ανά μονάδα μήκους σε Ω/m
AB = 8 * 10 ** (-2)  # Μήκος πλευράς ΑΒ σε m
AΓ = 6 * 10 ** (-2)  # Μήκος πλευράς ΑΓ σε m
V = 14  # Τάση ΒΓ σε V

print()
ΒΓ = sqrt(AB ** 2 + AΓ ** 2)
print('Αν εφαρμόσουμε Πυθαγόρειο Θεώρημα για το τρίγωνο ισχύει ότι ΒΓ={:.2f} m'.format(ΒΓ))

print()
RAB = AB * r
RAΓ = AΓ * r
RΒΓ = ΒΓ * r
print('H αντίσταση της πλευράς ΑΒ είναι RAB=AB*r => RAB={:.2f} Ω'.format(RAB))
print('H αντίσταση της πλευράς ΑΓ είναι RAΓ=AΓ*r => RAΓ={:.2f} Ω'.format(RAΓ))
print('H αντίσταση της πλευράς ΒΓ είναι RΒΓ=ΒΓ*r => RΒΓ={:.2f} Ω'.format(RΒΓ))

print()
IBAΓ = V / (RAB + RAΓ)
ΙΒΓ = V / RΒΓ
print(
    'Για την ένταση ισχύει στις πλευρές ΒΑΓ ισχύει V=IBAΓ*(RAB+RAΓ) => IBAΓ=V/(RAB+RAΓ) => IBAΓ={:.2f} A'.format(IBAΓ))
print('Για την ένταση ισχύει στην πλευρά   ΒΓ ισχύειV=ΙΒΓ*RΒΓ         => ΙΒΓ =V/(RΒΓ)     =>  IBΓ={:.2f} A'.format(ΙΒΓ))
