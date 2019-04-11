#!/usr/bin/python3
#Filename: 1_27.py
'''Άσκηση 27:

Στο μοντέλο του Bohr για το άτομο του υδρογόνου, τα ηλεκτρόνια μπορούν να
περιστρέφονται γύρω από τον πυρήνα (πρωτόνιο)σε (επιτρεπόμενες) κυκλικές τροχιές.
Αν μία τροχιά έχει ακτίνα r = 8 ∙ 10 -10m, να υπολογιστούν:
Α. Η δυναμική
Β. Η κινητική
Γ. Η μηχανική ενέργεια του ηλεκτρονίου στην τροχιά ακτίνας r.
'''
from const import k         #ηλεκτροστατική σταθερά  N*m^2/C^2
from const import Qp        #φορτίο πρωτονίου Qp σε C.
from const import Qe        #φορτίο ηλεκτρονίου Qe σε C.
from const import Me        #Μάζα ηλεκτρονίου Μe σε Kg.
from math import sqrt


#Δεδομένα
r= 8*10**(-10)             #ακτίνα τροχιάς σε m.

print('--------------A.--------------------')
print('H δυναμική ενέργεια δίνεται από την σχέση: U=k*Qp*Qe/r  ')
print('Άρα:')
U=k*Qp*Qe/r
print('U = {:.2e} Joule'.format(U))
print()

print('--------------B.--------------------')
print('Η Δύναμη που ασκείται στο ηλεκτρόνιο είναι η δύναμη Coulomb του ηλεκτρικού πεδιου και ταυτόχρονα αποτελεί και την κεντρομόλος δύναμη, ισχύει:')
print('Fc=Me*u²/r =>k*|Qp*Qe|/r² = Me*u²/r => u=√( (k*|Qp*Qe|)/ (Me*r) )')
print('Άρα:')
u=sqrt(k*abs(Qp*Qe)/(Me*r))
print('u = {:.2e} m/sec'.format(u))
print()
print('H κινητική ενέργεια Ek δίνεται από τη σχέση Ek=(1/2)*Me*u² ')
Ek=(1/2)*Me*u**2
print('Άρα:')
print('Ek = {:.2e} Joule'.format(Ek))
print()

print('--------------Γ.--------------------')
print('H Μηχανική ενέργεια είναι το άθροισμα της δυναμικής και κινητικής Ενέργειας')
print('Άρα:')
print('Eολ = {:.2e} Joule'.format(U+Ek))