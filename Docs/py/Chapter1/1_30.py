#!/usr/bin/python3
#Filename: 1_30.py
'''Άσκηση 30:

Το σωματίδιο «α» αποτελείται από δύο πρωτόνια και δύο νετρόνια (mp = mn).
Το σωματίδιο «α» επιταχύνεται σε ομογενές ηλεκτρικό πεδίο. Εάν το αφήσουμε
(υο = 0), να επιταχυνθεί μεταξύ δύο σημείων ΑΒ που έχουν διαφορά δυναμικού
ίση με 12.000V, να βρεθεί ποια είναι η ταχύτητά του στο σημείο Β.
'''
from const import k         #ηλεκτροστατική σταθερά  N*m^2/C^2
from const import Qp        #φορτίο πρωτονίου Qp σε C.
from const import Mp        #Μάζα προτωνίου σε Kg.
from math import sqrt


#Δεδομένα

V =12000                  #Διαφορά δυναμικού σε V


print('---------------------------------')
print()
print('Η μάζα του σωματιδίου είναι τετραπλάσια της μάζας του προτωνίου')
m=4*Mp

print('Το φορτίο του σωματιδίου είναι διπλάσιο του φορτίου του προτωνίου')
Q=2*Qp

print('Το έργο της δύναμης του πεδίου για την μετακίνηση του σωματιδίου "α" από το σημείο A στο B,')
print('Θα είναι ίσο με την κινητική Ενέργεια Εk που θα έχει το σωματίδιο στην θέση Β, δηλαδή:')
print('W = Εκ => V*Q = (1/2)*m*u² και λύνοντας ως προς u έχουμε:')
u=sqrt(2*Q*V/m)
print('u= {:.3e} m/sec'.format(u))
print()