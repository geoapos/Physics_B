#!/usr/bin/python3
# Filename: 1_11.py
'''Άσκηση 11:

Δοκιμαστικό ηλεκτρικό φορτίο q1=2μC βρίσκεται στη θέση (Σ) ηλεκτρικού πεδίου και δέχεται 2⋅10−3N, κατά τη θετική κατεύθυνση του άξονα x. Να βρεθούν:
Α. Η ένταση του πεδίου στη θέση (Σ).
Β. Η δύναμη που θα δεχτεί φορτίο q2=−4μC στη θέση (Σ).'''
from const import k

# Δεδομένα

q1 = 2 * 10 ** (-6)  # Δοκιμαστικό φορτίο σε C.
F = 2 * 10 ** (-3)  # Δύναμη που δέχεται το Φορτίο σε Ν.
q2 = -4 * 10 ** (-6)  # φορτίο σε C.

print('Το μέτρο της έντασης του πεδίου είναι: E=F/|q1|')
E = F / abs(q1)
print('Συνεπώς το μέτρο της έντασης θα είναι: Ε={:.2e} N/C'.format(E), 'με κατεύθυνση την θετική του άξονα x.')
print()
print('Η δύναμη που θα δεχθεί το φορτίο q2 στην ίδια θέση θα είναι: F2=E*|q2|')
F2 = E * abs(q2)
print('Tο μέτρο της δύναμης θα είναι: F2={:.2e} N/C'.format(F2), 'με κατεύθυνση την αρνητική του άξονα x.')
