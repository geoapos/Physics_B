#!/usr/bin/python3
#filename 2_6.py
'''
Άσκηση 2.6

Ένα σύρμα από λευκόχρυσο έχει μήκος l=10m και μάζα m = 3,6g.
Να βρείτε την αντίσταση του σύρματος, αν η πυκνότητα του
λευκόχρυσου είναι d = 21g/cm^3 και η ειδική
του αντίσταση ρ = 9·10^-8 Ω·m.
'''

#Δεδομένα
l=10                                # Μήκος αγωγού σε m
m=3.6*10**(-3)                      # Μάζα σύσρματο σε Kg.
d=21*10**3                          # Πυκνότητα σε Kg/m3
ρ=9*10**(-8)                        # ειδική αντίσταση σε Ω*m



print()
print('Μπορούμε να υπολογίσουμε την αντίσταση από την σχέση R=ρ*l/S  (1) όπου S η διατομή.')
print('Επίσης από τον όγκο του σύρματος V=m/d όπου d η πυκνότητα και V=S*l προκύπτει:')
print('S=d*m/l (2)')
print('Από (1) και (2) έχουμε:')
R=(d*ρ*l**2)/m
print('R=(d*ρ*l**2)/m => R={:.2f}'.format(R))