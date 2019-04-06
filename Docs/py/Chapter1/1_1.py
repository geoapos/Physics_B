#!/usr/bin/python3
#Filename:1_1.py

'''
Άσκηση 1:
Να υπολογίσετε τον αριθμό των ηλεκτρονίων που συναποτελούν
φορτίο ίσο με:
Α. -1,6C Β. -1,6mC Γ. -1,6μC Δ. -1,6nC Ε. -1,6pC
'''

from const import *

#Δεδομένα
qe=-1.6*10**(-19)
Qa=-1.6
Qb=-1.6*10**(-3)
Qc=-1.6*10**(-6)
Qd=-1.6*10*(-9)
Qe=-1.6*10**(-12)


print("Έστω φορτίο Q περιέχει n ηλεκτρόνια. θα έχουμε Q=n⋅qe, άρα n=Q/qe:")
print('και επειδή qe=-1.6*10^-19\n')

print('Α. n={:.1e} e'.format(Qa/qe))
print('B. n={:.1e} e'.format(Qb/qe))
print('Γ. n={:.1e} e'.format(Qc/qe))
print('Δ. n={:.1e} e'.format(Qd/qe))
print('Ε. n={:.1e} e'.format(Qe/qe))
