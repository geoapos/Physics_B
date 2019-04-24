#!/usr/bin/python3
# filename 4_1.py
"""
Άσκηση 4.1

Το άτομο του υδρογόνου βρίσκεται στη θεμελιώδη κατάσταση. Η ακτίνα της
τροχιάς του ηλεκτρονίου είναι r = 5,3x10 − 11 m. Να υπολογιστούν:
α. η ταχύτητα του ηλεκτρονίου,
β. η περίοδος της κίνησης του ηλεκτρονίου,
γ. η κινητική, η δυναμική και η ολική ενέργεια του ηλεκτρονίου.
"""

from const import Qe    # Το φορτίο του ηλεκτρονίου σε Coulomb
from const import k     # ηλεκτροστατική σταθερά  N*m^2/C^2
from const import Me    # Μάζα ηλεκτρονίου
from const import eV    # Ηλεκτρονιοβόλτ
from math import sqrt   # square root
import math

# Δεδομένα
r = 5.3 * 10**(-11)     # ακτίνα τροχιάς σε m

print()
print('α) Στο ηλεκτρόνιο ασκείται η δύναμη Coulomb η οποία είναι ίση με \n'
      '   την κεντρομόλο δύναμη, συνεπώς ισχύει: \n'
      '   Fc = Fk => k * Qe²/r² = m * u² / r =>\n'
      '   u=√(k*Qe²/(m*r)) => u=', end='')
u = sqrt ( k * Qe**2 / (Me * r))
print(f'{u:.3e} m/sec')

print()
print('β) Η περίοδος της κίνησης είναι T = 2 * pi * r / u => \n'
     f'   T={(2 * math.pi * r / u):.2e} s')

print()
print('γ) -- Η κινητική ενέργεια είναι Ek = 1/2 * Me * u² => Ek =', end='')
Ek = 1/2 * Me * u**2
print(f'{Ek/eV:.1f} eV')

print('   -- Η δυναμική ενέργεια είναι Eu = -k * Qe² / r => Eu =', end='')
Eu = (-k * Qe**2) / r
print(f'{Eu/eV:.1f} eV')

print('   -- Η ολική ενέργεια είναι E = Ek+ Eu => E =', end='')
E = Ek+ Eu
print(f'{E/eV:.1f} eV')