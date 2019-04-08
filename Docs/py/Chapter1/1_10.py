#!/usr/bin/python3
#Filename: 1_10.py
'''
Άσκηση 10:
Φορτίο +9μC απέχει απόσταση 30cm από άλλο φορτίο +4μC. Να
βρεθεί η ένταση του ηλεκτρικού πεδίου στο μέσο της μεταξύ τους
απόστασης.
'''
from const import k

#Δεδομένα

Q1=9*10**(-6)               #Φορτίο σε C.
Q2=4*10**(-6)               #Φορτίο σε C.
r=0.30                      #Η απόσταση σε m.

print('Το μέτρο της έντασης του πεδίου σε απόσταση r δίνεται από την σχέση: Ε=k*|Q|/r^2')
print()
print('Στο μέσο της απόστασης υποθέτουμε ότι έχουμε ένα θετικό φορτίο.')
print('Η ένταση του πεδίου που προκαλεί το φορτίο Q1 είναι αντίρροπη,\nμιας και τα φορτία είναι θετικά.')
E1=k*abs(Q1)/((r/2)**2)      #Ενταση που προκαλεί το φορτίο Q1 
print('Εχουμε λοιπόν: E1={:.2e}'.format(E1))
print()
E2=k*abs(Q2)/((r/2)**2)      #Ενταση που προκαλεί το φορτίο Q2 
print('Ομοίως για το το φορτίο Q2 έχουμε: E2={:.2e}'.format(E2))
Eol=E1-E2               #Συνολική Ένταση
print('και οι εντάσεις Ε1 και Ε2 είναι αντίρροπες,/nη συνολική ενταση θα έχει μέτρο Εολ=Ε1-Ε2={:.2e} και φορά την φορά της Ε1.'.format(Eol))