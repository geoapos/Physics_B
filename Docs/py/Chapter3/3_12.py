#!/usr/bin/python3
# filename 3_12.py
"""
Άσκηση 3.12

Ακτινοβολία συχνότητας 10 ΤΗz απορροφάται πλήρως από
μία ποσότητα νερού, οπότε αυξάνεται η θερμοκρασία του
νερού κατά 2° C.
Αν γνωρίζετε ότι για να αυξηθεί η θερμοκρασία της παραπάνω
ποσότητας κατά 1° C απαιτείται ενέργεια 21216 J, πόσα φωτόνια
της ακτινοβολίας απορροφώνται;
"""


# Δεδομένα
f = 10 * 10**(12)       # Συχνότητα ακτινοβολίας σε Hz
dT = 2                  # Διαφορά θερμοκρασίας σε °
Εο = 21216              # Ενέργεια σε J
h = 6.63 * 10**(-34)    # Σταθερά Planck σε J*sec
c = 3 * 10**8           # Ταχύτητα του φωτός σε m/sec.


print()
print(f'Αν για να αυξηθεί η θερμοκρασία του νερού κατά ΔΤ=1 °C χρειάζεται ενεργεια Εο={Εο} J,')
print(f'τότε για να αυξηθεί κατά dT = {dT} °C χρειάζεται E = dT * Εο = ', end='')
E = dT * Εο
print(f'{E} J')

print('Επειδή η Ενέργεια δίνεται από την σχέση Ε = N* h * f \tόπου Ν: αριθμός φωτονίων')
print('N = E / (h * f) => N = {:.3e} '.format(E / (h * f) ))


