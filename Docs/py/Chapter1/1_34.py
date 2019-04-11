#!/usr/bin/python3
#Filename: 1_34.py
'''Άσκηση 34:

Επίπεδος πυκνωτής έχει οπλισμούς με εμβαδόν 200cm² ο καθένας.
Εάν η χωρητικότητα του πυκνωτή είναι 17,7 ∙ 10^-11 F, πόση είναι
η απόσταση μεταξύ των δύο οπλισμών του;
'''
from const import e0 #H απόλυτη διηλεκτρική σταθερά του κενού

#Δεδομένα
S=200*10**(-4)              # Εμβαδό οπλισμού σε m².
C=17.7*10**(-11)            #χωρητικότητα πυκνωτή σε F.

print()
l=e0*S/C
print('Η χωρητικότητα του πυκνωτή είναι: l=e0*S/C => l={:.2} m'.format(l))