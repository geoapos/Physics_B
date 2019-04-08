#!/usr/bin/python3
#Filename: 1_24.py
'''Άσκηση 24:

Δοκιμαστικό φορτίο +2μC τοποθετείται σε σημείο (Σ) ηλεκτρικού πεδίου. Αν το δυναμικό στη θέση (Σ) είναι -10V να βρείτε:
Α. Τη δυναμική ενέργεια του δοκιμαστικού φορτίου.
Β. Πόσο έργο πρέπει να προσφερθεί στο δοκιμαστικό φορτίο για να φθάσει στο άπειρο χωρίς ταχύτητα;
'''

from const import k

#Δεδομένα
Q=2*10**(-6)               #φορτίο  Q σε C.
V=-10                      #Δυναμικό σε V.

print('--------------Α.--------------------')
print('H δυναμική ενέργεια δίνεται από την σχέση: V =U/Q => U=V*Q  ')
print('Άρα:')
U=V*Q
print('U = {:.2e} Joule'.format(U))
print()
print('--------------B.--------------------')
print('Εφόσον η δυναμική του ενέργεια είναι αρνητική πρέπει να του προσφερθεί ενέργεια ίση με +{:.2e} Joule για τη μεταφορά του φορτίου στο άπειρο.'.format(-U))
