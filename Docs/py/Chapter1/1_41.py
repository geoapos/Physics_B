#!/usr/bin/python3
# Filename: 1_41.py
'''Άσκηση 41:

Η ένταση μεταξύ των οπλισμών ενός επίπεδου πυκνωτή είναι 5 ∙ 10^5 V/m.
Στο χώρο μεταξύ των οπλισμών του πυκνωτή αιωρείται σταγόνα λαδιού
που έχει βάρος 3,2 ∙ 10^(-13) Ν. Ποιο είναι το ηλεκτρικό φορτίο της σταγόνας;
'''

# Δεδομένα

E = 5 * 10 ** (5)  # Ένταση σε V/m
B = 3.2 * 10 ** (-13)  # βάρος σταγόνας σε Kg

print()
q = B / E
print('Αφού η σταγόνα αιωρείται τότε ΣF=0 => Fhl=B => E*q=B \n άρα: q=B/E => q={:.2e} C'.format(q))
