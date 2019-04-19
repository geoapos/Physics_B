#!/usr/bin/python3
#filename 2_2.py
'''
Άσκηση 2.2

Να βρείτε την ένταση του ρεύματος, λόγω της κίνησης του ηλεκτρονίου του
ατόμου του υδρογόνου, αν η συχνότητα περιστροφής του είναι ν = 5,8·10^15Ηz.
Δίνεται: qe= -1,6·10-19C.


'''

#Δεδομένα
ν=5.8*10**(15)      # Συχνότητα περιστροφής σε Hz
qe=-1.6*10**(-19)    # Φορτίο ηλεκτρονίου σε C


print()
print('Η συχνότητα είναι ν=1/Τ, όπου Τ η περίοδος δηλαδή ο χρόνος μιας περιστροφής, άρα:')
print('T=1/ν (1)')
print('Επίσης ισχύει ότι η ένταση i=qe/T (2)')
i=qe*ν
print('Από (1) και (2) έχουμε i=qe*ν =>i={:.2e} A'.format(i))