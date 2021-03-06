#!/usr/bin/python3
# filename 4_2.py
"""
Άσκηση 4.2

Η ενέργεια του ατόμου του υδρογόνου, όταν αυτό βρίσκεται στη θεμελιώδη
κατάσταση, είναι –13,6eV:
α. Ποια θα είναι η ενέργεια του ατόμου στην πρώτη διεγερμένη κατάσταση (n=2)
και ποια στη δεύτερη διεγερμένη κατάσταση (n=3);
β. Το άτομο διεγείρεται και αποκτά ενέργεια –0,85eV. Σε ποιο κύριο κβαντικό
αριθμό αντιστοιχεί η διεγερμένη αυτή κατάσταση;
"""

from math import sqrt

# Δεδομένα
E1=-13.6    # Ενέργεια 1ης στάθμης σε eV
n2=2        # Κβαντικός αριθμός 2ης στάθμης
n3=3        # Κβαντικός αριθμός 3ης στάθμης
En=-0.85    # Ενέργεια στάθμης σε eV

print()
print('α) Η ενέργεια του ατόμου σε κατάσταση που αντιστοιχεί σε κβαντικό αριθμό\n'
      '   n είναι: En = E1 / n² , έτσι, ')
print('   για n2 είναι: E2 = E1 / n2² => E2 =', end='')
E2 = E1 / n2**2
print(f'{E2:.2f} eV')
print('   για n3 είναι: E3 = E1 / n3² => E3 =', end='')
E3 = E1 / n3**2
print(f'{E3:.2f} eV')


print('β) Πάλι από την σχέση En = E1 / n² προκύπτει n = √ (E1/En)), άρα:')
n = sqrt(E1/En)
print(f'   n={n}')
